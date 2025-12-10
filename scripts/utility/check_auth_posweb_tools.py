
# num_iniziale = input("numero a video: ")
num_iniziale = '29'
if len(num_iniziale) != 2:
	raise Exception(u"Errore")

prima_cifra = int(num_iniziale[0])
print(prima_cifra)
seconda_cifra = int(num_iniziale[1])
print(seconda_cifra)
risultato = (int(prima_cifra) * int(seconda_cifra)) + int(prima_cifra) + int(seconda_cifra)
print(risultato)
print(f"il codice da scrivere è {risultato}00")


# se 009 in realtà è 0900