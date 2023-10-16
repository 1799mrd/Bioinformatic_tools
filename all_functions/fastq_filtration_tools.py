import os

def main(input_path, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0):
    seqs = read_fastq_file(input_path)
    filtered_seqs = filter_fastq_sequences(seqs, gc_bounds, length_bounds, quality_threshold)
    output_filename = get_output_filename(input_path)
    write_filtered_fastq(filtered_seqs, output_filename)

def read_fastq_file(input_path):
    seqsdi = {}
    tuple_seqs = []
    id_seq = []
    with open('myfile.txt', 'r') as file:
        seq_id = ''
        seq = ''
        qual = ''
        for line in file:
            line = line.strip()
            if line.startswith('@'):
                seq_id = line
                id_seq.append(seq_id)
            elif line.startswith('+'):
                pass
            else:
                if seq_id not in seqsdi:
                    seqsdi[seq_id] =  {'seq': '', 'qual': ''}
                if seq == '':
                    seq = line
                else:
                    qual = line
                    seqsdi[seq_id]['seq'] = seq
                    seqsdi[seq_id]['qual'] = qual
                    tuple_seqs.append((seq, qual))
                    seq_id = ''
                    seq = ''
                    qual = ''
        seqs = dict(zip(id_seq, tuple_seqs))
    return seqs

def filter_fastq_sequences(seqs, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0):
    filtered_seqs = {}
    
    for name, (sequence, quality) in seqs.items():
        gc_content = calculate_gc_content(sequence)
        seq_length = len(sequence)
        avg_quality = calculate_avg_quality(quality)
        
        if is_within_bounds(gc_content, gc_bounds) and is_within_bounds(seq_length, length_bounds) and avg_quality >= quality_threshold:
            filtered_seqs[name] = (sequence, quality)
    return filtered_seqs

def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    total_count = len(sequence)

    return (gc_count / total_count) * 100

def calculate_avg_quality(quality):
    total_quality = sum(ord(q)-33 for q in quality)
    seq_length = len(quality)

    return total_quality / seq_length

def is_within_bounds(value, bounds):
    if type(bounds) in (int, float):
        return value < bounds
    else:
        lower_bound, upper_bound = bounds
        return lower_bound <= value <= upper_bound

def get_output_filename(input_path):
    output_dir = 'fastq_filtrator_results'
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.basename(input_path)
    output_filename = os.path.splitext(filename)[0]
    return os.path.join(output_dir, output_filename)

def write_filtered_fastq(filtered_seqs, output_filename):
    with open(f'{output_filename}.fastq', 'w') as file:
        for seq_id, seq_data in filtered_seqs.items():
            file.write(f'{seq_id}\n')
            file.write(f'{seq_data[0]}\n')
            file.write('+\n')
            file.write(f'{seq_data[1]}\n')
