import os
import glob
import argparse

from os.path import exists

parser = argparse.ArgumentParser(description="Composizione file da lista di pk_consumers", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-p", "--path", default="/Users/emanuelebergonzini/Desktop/jpf1", help="percorso del file che contiene i pk_consumers")
parser.add_argument("-f", "--filename", default="query_result.csv", help="nome del file che contine i pk_consumers")
parser.add_argument("-o", "--out", default="out", help="cartella di output")
parser.add_argument("lenght", type=int, help="numero di pk_consumers da includere in un file")
args = parser.parse_args()
config = vars(args)

def write_file(count_file, lista_pk_consumers):
    with open("{}/{}/{}".format(config['path'], config['out'], "split_pk_consumer_{}.csv".format(count_file)), 'w') as file_out:
        file_out.write(",".join(lista_pk_consumers))
        file_out.close()
    print("Scrittura completata file split_pk_consumer_{}.csv".format(count_file))

def remove_out_file():
    files = glob.glob("{}/{}/*.csv".format(config['path'], config['out']))
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))
    print("Eliminazione complatata dei file di output precedenti all'esecuzione")

## STARTING PROCEDURE ##

print("Inizio procedura di lettura/scrittura files")

file_exists = exists("{}/{}".format(config['path'], config['filename']))
print("Ricerco {}/{}".format(config['path'], config['filename']))
if not file_exists:
    print("Il percorso o il file non è stato trovato")
    exit(1)
print("File trovato! Continuo esecuzione...")

count_pk = 0
count_file = 0
lista_pk_consumers = []

remove_out_file()

with open("{}/{}".format(config['path'], config['filename']), 'r') as file_in:
    while True:
        pk_consumer = file_in.readline().replace('\n', '')
        lista_pk_consumers.append(pk_consumer)
        if pk_consumer == '': #eof
            write_file(count_file, lista_pk_consumers)
            break
        count_pk += 1
        if count_pk >= config['lenght']:
            write_file(count_file, lista_pk_consumers)
            lista_pk_consumers = []
            count_pk = 0
            count_file += 1
    file_in.close()

print("Script eseguito con successo")
