def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None):
    if output_fasta is None:
        output_fasta = f"{input_fasta}.fasta"

    with open(input_fasta, "r") as input_file, open(output_fasta, "w") as output_file:
        sequence = ""
        for line in input_file:
            line = line.strip()
            if line.startswith(">"):
                if sequence:
                    output_file.write(sequence + "\n")
                    sequence = ""
                output_file.write(line + "\n")
            else:
                sequence += line
        if sequence:
            output_file.write(sequence + "\n")


def select_genes_from_gbk_to_fasta(input_gbk, genes, n_before=1, n_after=1, output_fasta=None):
    if output_fasta is None:
        output_fasta = f"{input_gbk}.fasta"

    selected_genes = set(genes)

    with open(input_gbk, "r") as input_file, open(output_fasta, "w") as output_file:
        sequence = ""
        gene_name = ""
        gene_start = 0
        gene_end = 0
        for line in input_file:
            line = line.strip()
            if line.startswith("LOCUS"):
                if sequence and gene_name in selected_genes:
                    output_file.write(f">{gene_name}|{gene_start}-{gene_end}\n{sequence}\n")
                sequence = ""
                gene_name = ""
                gene_start = 0
                gene_end = 0
            elif line.startswith("ORIGIN"):
                if sequence and gene_name in selected_genes:
                    output_file.write(f">{gene_name}|{gene_start}-{gene_end}\n{sequence}\n")
                break
            elif line.startswith("     gene"):
                parts = line.split()
                gene_name = parts[1]
                gene_start = int(parts[2])
                gene
