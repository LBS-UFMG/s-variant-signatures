import os
from Bio import PDB
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Função para extrair a sequência de aminoácidos de um arquivo PDB
def extract_sequence_from_pdb(pdb_file):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('pdb_structure', pdb_file)
    sequence = []
    
    for model in structure:
        for chain in model:
            for residue in chain:
                # Ignora heteroátomos e solventes
                if PDB.is_aa(residue, standard=True):
                    sequence.append(residue.resname)

    # Converte os nomes dos resíduos em uma sequência de letras
    aa_sequence = Seq("".join([PDB.Polypeptide.three_to_one(res) for res in sequence]))
    return aa_sequence

# Caminho para a pasta com os arquivos PDB
pdb_folder = './Modelagens'

# Cria a pasta para salvar os arquivos FASTA
fasta_folder = os.path.join(pdb_folder, 'fasta_files')
os.makedirs(fasta_folder, exist_ok=True)

# Loop pelos arquivos PDB na pasta
for pdb_file in os.listdir(pdb_folder):
    if pdb_file.endswith('.pdb'):
        pdb_path = os.path.join(pdb_folder, pdb_file)
        sequence = extract_sequence_from_pdb(pdb_path)
        
        # Cria um SeqRecord para o FASTA
        record = SeqRecord(sequence, id=pdb_file.split('.')[0], description="")

        # Caminho para salvar o arquivo FASTA
        fasta_file = os.path.join(fasta_folder, f"{pdb_file.split('.')[0]}.fasta")
        
        # Salva o arquivo FASTA
        with open(fasta_file, 'w') as output_handle:
            SeqIO.write(record, output_handle, "fasta")

print("Arquivos FASTA gerados com sucesso!")
