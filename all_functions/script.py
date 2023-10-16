from fastq_filtration_tools import main
input_path = 'myfile.txt'
gc_bounds = (20, 80)
length_bounds = (0, 100)
quality_threshold = 30
main(input_path, gc_bounds, length_bounds, quality_threshold)
