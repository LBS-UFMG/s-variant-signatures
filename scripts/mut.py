from Bio import SeqIO
import os 

# Sequência de referência 7CWL
reference_seq = (
    "MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT"
)

# Função para comparar duas sequências e retornar as mutações
def compare_sequences(reference, query):
    mutations = []
    for i, (ref_aa, query_aa) in enumerate(zip(reference, query)):
        if ref_aa != query_aa:
            mutations.append(f"{ref_aa}{i+1}{query_aa}")
    return mutations

# Caminho para a pasta com os arquivos FASTA
fasta_folder = './Modelagens/fasta_files'

# Lista para armazenar as mutações de cada arquivo
mutations_per_file = {}

# Loop pelos arquivos FASTA na pasta
for fasta_file in os.listdir(fasta_folder):
    if fasta_file.endswith('.fasta') or fasta_file.endswith('.fa'):
        fasta_path = os.path.join(fasta_folder, fasta_file)
        
        # Lê a sequência do arquivo FASTA
        for record in SeqIO.parse(fasta_path, "fasta"):
            query_seq = str(record.seq)
            
            # Compara com a sequência de referência
            mutations = compare_sequences(reference_seq, query_seq)
            
            # Armazena as mutações
            mutations_per_file[fasta_file] = mutations

# Exibe as mutações para cada arquivo
for fasta_file, mutations in mutations_per_file.items():
    print(f"Mutações no arquivo {fasta_file}:")
    if mutations:
        print(", ".join(mutations))
    else:
        print("Nenhuma mutação encontrada")
    print()
