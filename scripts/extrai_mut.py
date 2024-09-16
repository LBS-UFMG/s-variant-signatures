from Bio import AlignIO

# Caminho para o arquivo de alinhamento no formato "aln-clustal"
alignment_file = 'clustal.aln'

# Nome da sequência de referência no alinhamento
reference_name = "Wild_Variant_4294e"

# Função para comparar a sequência com a referência e identificar mutações
def find_mutations(reference_seq, target_seq):
    mutations = []
    for i, (ref_aa, target_aa) in enumerate(zip(reference_seq, target_seq)):
        if ref_aa != target_aa and target_aa != "-":  # Ignora gaps no alinhamento
            mutations.append(f"{ref_aa}{i+1}{target_aa}")
    return mutations

# Lê o alinhamento no formato Clustal
alignment = AlignIO.read(alignment_file, "clustal")

# Encontra a sequência de referência no alinhamento
reference_seq = None
for record in alignment:
    if record.id == reference_name:
        reference_seq = str(record.seq)
        break

if reference_seq is None:
    raise ValueError(f"Sequência de referência '{reference_name}' não encontrada no arquivo de alinhamento.")

# Loop por todas as sequências no alinhamento, exceto a referência
mutations_per_sequence = {}
for record in alignment:
    if record.id != reference_name:
        target_seq = str(record.seq)
        mutations = find_mutations(reference_seq, target_seq)
        mutations_per_sequence[record.id] = mutations

# Exibe as mutações para cada sequência
for sequence_id, mutations in mutations_per_sequence.items():
    print(f"Mutações na sequência {sequence_id}:")
    if mutations:
        print(", ".join(mutations))
    else:
        print("Nenhuma mutação encontrada")
    print()
