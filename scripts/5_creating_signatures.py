import Signa.signa as signa

# Obtaining the labels
#labels_example = signa.labels(signa_type='acsm', cutoff_step=0.1, cutoff_limit=10, separator=",", cumulative=True)
#print(labels_example)
#exit()

# Multiple files - Folder
signa.read_folder(
 	folder='../data/pdb_filtered/train', 
 	signa_type='acsm-all', 
    #forcefield='AMBER',
    cumulative=True,
 	output='../input/train_acsm_all_10_0.1.csv',
    cutoff_limit=10,
    cutoff_step=0.1,
    format='pdb'
)

signa.read_folder(
    folder='../data/pdb_filtered/test', 
    signa_type='acsm-all', 
    #forcefield='AMBER',
    cumulative=True,
    output='../input/test_acsm_all_10_0.1.csv',
    cutoff_limit=10,
    cutoff_step=0.1,
    format='pdb'
)

# SSV - Comparisons between signatures
#ssv = signa.ssv(entry, entry)
#print(ssv)
# signature = signa.read("./docs/case_studies/cs4/pdb/AAGAATTAAGAASGA.pdb", 'signa-charge', forcefield='AMBER',cutoff_limit=12, cutoff_step=0.2, separator=",", cumulative=True)

#print(signature)