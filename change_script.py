from bio_files_processor import change_fasta_start_pos

input_fasta = "my_change.fasta"
shift = 2
output_fasta = "my_change_output.fasta"
change_fasta_start_pos(input_fasta, shift, output_fasta)
