import os
import subprocess
import argparse
import sys
sys.path.extend(["/Users/emanuele.bergonzini/Documents/Documents/scripts"])
sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/CREDENZIALI'])

from pathlib import Path
from credenziali_cloud import MAPPING_CLOUD

def aggiorna_repo(repo_dir):
	if repo_dir.is_dir() and repo_dir.name != '.idea':
		print(f'Aggiornamento in {repo_dir}')
		result = subprocess.run(
			['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
			cwd=repo_dir,
			capture_output=True,
			text=True
		)
		branch = result.stdout.strip()
		print(f'Branch attuale: {branch}')
		subprocess.run(['git', 'pull'], cwd=repo_dir)
	else:
		print(f'Skipping {repo_dir}, non è una directory git valida.')


paths = [
	'/Users/emanuele.bergonzini/repos/',
	'/Users/emanuele.bergonzini/repos/kube',
	'/Users/emanuele.bergonzini/repos/poslite'
]

# crea un metodo come all_repos_to_master che elimina le branches master_py312 e porting_python3
def elimina_repos_indesiderati(guest_path):
	branches_to_delete = ['master_py312', 'porting_python3']
	for branch in branches_to_delete:
		result = subprocess.run(
			['git', 'branch', '--list', branch],
			cwd=guest_path,
			capture_output=True,
			text=True
		)
		if result.stdout.strip():
			print(f'Eliminazione branch {branch} in {guest_path}')
			subprocess.run(['git', 'branch', '-D', branch], cwd=guest_path)
		else:
			print(f'Branch {branch} non trovato in {guest_path}, skipping.')

def all_repos_to_master(repo_dir):
	bms_list = list(set(MAPPING_CLOUD.values()))
	sub_repos = ['posws', 'poswsfe', 'storebackoffice']

	for bms in bms_list:
		guest_path = repo_dir / bms / 'guest'
		if guest_path.exists():
			for sub_repo in sub_repos:
				sub_repo_path = guest_path / sub_repo
				if sub_repo_path.exists():
					elimina_repos_indesiderati(sub_repo_path)
					print(f'Aggiornamento {sub_repo} in {sub_repo_path} alla branch master')
					subprocess.run(['git', 'checkout', 'master'], cwd=sub_repo_path)
					subprocess.run(['git', 'pull'], cwd=sub_repo_path)
				else:
					print(f'Skipping {sub_repo_path}, non esiste.')
		else:
			print(f'Skipping {guest_path}, non esiste.')


def main():
	parser = argparse.ArgumentParser(description="Aggiorna repository git in una directory.")
	parser.add_argument('-m', action="store_true", help="Numero della directory di base da aggiornare (1, 2, 3...)")
	args = parser.parse_args()

	if args.m:
		base_dir = Path(paths[0])
		os.chdir(base_dir)
		repo_dir = base_dir
		all_repos_to_master(repo_dir)
		return

	print("Scegli la directory di base:")
	for idx, p in enumerate(paths, 1):
		print(f"{idx}) {p}")

	scelta = None
	try:
		scelta = input("Inserisci il numero della directory: ")
		if not scelta or int(scelta) - 1 >= len(paths):
			print("Scelta non valida. Uscita.")
			exit(1)
	except ValueError:
		print("Input non valido. Uscita.")
		exit(1)

	scelta_num = int(scelta) - 1
	base_dir = Path(paths[scelta_num])
	os.chdir(base_dir)

	if scelta_num == 0:
		cartella = input("Vuoi aggiornare solo una cartella specifica? (lascia vuoto per tutte): ").strip()
		if cartella:
			repo_dir = base_dir / cartella
			aggiorna_repo(repo_dir)
		else:
			for repo_dir in base_dir.iterdir():
				aggiorna_repo(repo_dir)
	else:
		for repo_dir in base_dir.iterdir():
			aggiorna_repo(repo_dir)


if __name__ == "__main__":
	main()
