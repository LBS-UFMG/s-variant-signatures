import os
from Bio import SeqIO

# Caminho para a pasta com os arquivos FASTA
fasta_folder = './Modelagens/fasta_files'

# Nome do arquivo de saída onde todas as sequências serão concatenadas
output_file = 'todos.fasta'

# Abre o arquivo de saída no modo de escrita
with open(output_file, 'w') as output_handle:
    # Loop pelos arquivos FASTA na pasta
    for fasta_file in os.listdir(fasta_folder):
        if fasta_file.endswith('.fasta') or fasta_file.endswith('.fa'):
            fasta_path = os.path.join(fasta_folder, fasta_file)
            
            # Lê e escreve cada sequência no arquivo de saída
            with open(fasta_path, 'r') as input_handle:
                for record in SeqIO.parse(input_handle, "fasta"):
                    SeqIO.write(record, output_handle, "fasta")

print(f"Todas as sequências foram concatenadas em {output_file}")
