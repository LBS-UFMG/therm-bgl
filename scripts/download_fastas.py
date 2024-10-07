import requests

# used to download fasta files

with open("ids.txt") as fid:
        linhas = fid.readlines()

        for linha in linhas:
                uniprot_id = linha.strip()
                base_url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
                response = requests.get(base_url)

                if response.status_code == 200:
                        with open(f'{uniprot_id}.fasta', 'wb') as file:
                                file.write(response.content)
                                #time.sleep(1)
                else:
                        fails_test.append(uniprot_id)
                        print(f'Falha TEST ao baixar o arquivo. Código de status: {response.status_code}')