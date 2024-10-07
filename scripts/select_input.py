# this script random select the input files
import random

fasta_file = "../data/uniprotkb_ec_3_2_1_21_2024_10_04.fasta" # unzip file before
w = open("../data/uniprot_id_train.csv", "w")
w_test = open("../data/uniprot_id_test.csv", "w")

print("class,uniprot_id,name",file=w)
print("class,uniprot_id,name",file=w_test)


n_train = 1000  # 1000 for each class
n_test = 500    # 500 for each class

data_pos = {} # uniprot_id : organism name
data_neg = {} # uniprot_id : organism name

with open(fasta_file) as ff:
	lines = ff.readlines()

	for line in lines:
		if line.startswith(">"):
			cells = line.split("|")
			uniprot_id = cells[1]
			name = cells[2]

			is_therm = name.lower().find("therm")

			if is_therm != -1:
				data_pos[uniprot_id] = name.replace(",","-").strip()
			else:
				data_neg[uniprot_id] = name.replace(",","-").strip()

print("selecting train data")
for i in range(n_train):

	print(i+1, "/", n_train)

	# positive
	random_key = random.choice(list(data_pos.keys()))
	print("positive", random_key, data_pos[random_key], file=w, sep=",")
	data_pos.pop(random_key) # remove

	#negative
	random_key = random.choice(list(data_neg.keys()))
	print("negative", random_key, data_neg[random_key], file=w, sep=",")
	data_neg.pop(random_key) # remove


print("selecting test data")
for i in range(n_test):

	print(i+1, "/", n_test)

	# positive
	random_key = random.choice(list(data_pos.keys()))
	print("positive", random_key, data_pos[random_key], file=w_test, sep=",")
	data_pos.pop(random_key) # remove

	#negative
	random_key = random.choice(list(data_neg.keys()))
	print("negative", random_key, data_neg[random_key], file=w_test, sep=",")
	data_neg.pop(random_key) # remove
