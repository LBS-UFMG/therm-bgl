# download pdbs models from alphafold
import requests
import time

continuar = -1

pdb_list_train = "../data/uniprot_id_train.csv"
pdb_list_test = "../data/uniprot_id_test.csv"

fails_train = []
fails_test = []

cont = 0

with open(pdb_list_test) as ftest:

	lines = ftest.readlines()

	for line in lines:
		cont+=1
		if cont < continuar:
			continue
		cells = line.split(",")

		uniprot_id = cells[1]
		print(cont, uniprot_id)

		if uniprot_id == "uniprot_id":
			continue # first line

		base_url = f'https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.pdb'

		response = requests.get(base_url)

		if response.status_code == 200:
			with open(f'../data/pdb/test/{uniprot_id}.pdb', 'wb') as file:
				file.write(response.content)
				#time.sleep(1)
		else:
			fails_test.append(uniprot_id)
			print(f'Falha TEST ao baixar o arquivo. Código de status: {response.status_code}')



with open(pdb_list_train) as ftrain:

	lines = ftrain.readlines()

	for line in lines:
		cont+=1
		if cont < continuar:
			continue

		cells = line.split(",")

		uniprot_id = cells[1]
		print(cont, uniprot_id)

		if uniprot_id == "uniprot_id":
			continue # first line

		base_url = f'https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.pdb'

		response = requests.get(base_url)

		if response.status_code == 200:
			with open(f'../data/pdb/train/{uniprot_id}.pdb', 'wb') as file:
				file.write(response.content)
				#time.sleep(1)
		else:
			fails_train.append(uniprot_id)
			print(f'Falha TRAIN ao baixar o arquivo. Código de status: {response.status_code}')

print("---\nLIST OF FAILS TRAIN")
print(fails_train)

print("---\nLIST OF FAILS TEST")
print(fails_test)