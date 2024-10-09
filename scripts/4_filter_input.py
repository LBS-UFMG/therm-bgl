import glob
import os

w = open("../data/input_metadata_filtered.csv","w")
w.write("class,uniprot_id,description,len,dataset\n")
folder1 = "../data/pdb/train"
folder2 = "../data/pdb/test"

tr = open("../data/uniprot_id_train.csv").readlines()
te = open("../data/uniprot_id_test.csv").readlines()

files1 = glob.glob(folder1+"/*.pdb")
files2 = glob.glob(folder2+"/*.pdb")

fails_tr = 0
fails_te = 0
tr_neg = 0
tr_pos = 0
te_neg = 0
te_pos = 0
print(len(files1), len(files2))

for i in files1:
	continue
	pdb = i[:-4].replace("../data/pdb/train/","")
	for j in tr:
		metadata = j.strip().split(',')

		if metadata[1] == pdb:
			with open(i) as p:
				lines = p.readlines()
				for line in lines:
					if line[0:4] == 'ATOM':
						last_atom = int(line[22:26].strip())
			if last_atom <= 800 and last_atom > 200:
				w.write(j.strip()+","+str(last_atom)+",train\n")

				os.system("cp ../data/pdb/train/"+pdb+".pdb ../data/pdb_filtered/train/"+pdb+".pdb")
				if metadata[0] == "negative":
					tr_neg += 1
				elif metadata[0] == "positive":
					tr_pos += 1
			else: 
				print("ERROR:",metadata,"Len:",last_atom)		
				fails_tr+=1


for i in files2:
	pdb = i[:-4].replace("../data/pdb/test/","")
	for j in te:
		metadata = j.strip().split(',')

		if metadata[1] == pdb:
			with open(i) as p:
				lines = p.readlines()
				for line in lines:
					if line[0:4] == 'ATOM':
						last_atom = int(line[22:26].strip())
			if last_atom <= 800 and last_atom > 200:
				w.write(j.strip()+","+str(last_atom)+",test\n")

				os.system("cp ../data/pdb/test/"+pdb+".pdb ../data/pdb_filtered/test/"+pdb+".pdb")
				if metadata[0] == "negative":
					te_neg += 1
				elif metadata[0] == "positive":
					te_pos += 1
			else: 
				print("ERROR:",metadata,"Len:",last_atom)		
				fails_te+=1

print("Total fails tr:",fails_tr, "- fails_te:",fails_te)
print("tr_neg = ",tr_neg)
print("tr_pos = ", tr_pos)
print("te_neg = ", te_neg)
print("te_pos = ", te_pos)
print("tr=",tr_neg+tr_pos, "- te=",te_neg+te_pos)
