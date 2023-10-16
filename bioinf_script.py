from all_functions.amino_acid_tools import amino_acid_tools
from all_functions.dna_rna_tools import run_dna_rna_tools
from all_functions.fastq_filtration_tools import filter_fastq_sequences

def filter_fastq_sequences(seqs, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0):
    filtered_seqs = {}

    for seq_name, (sequence, quality) in seqs.items():
        # Фильтрация по GC составу
        gc_content = calculate_gc_content(sequence)
        if isinstance(gc_bounds, tuple):
            if not gc_bounds[0] <= gc_content <= gc_bounds[1]:
                continue
        elif isinstance(gc_bounds, (int, float)):
            if gc_content > gc_bounds:
                continue

        # Фильтрация по длине
        sequence_length = len(sequence)
        if isinstance(length_bounds, tuple):
            if not length_bounds[0] <= sequence_length <= length_bounds[1]:
                continue
        elif isinstance(length_bounds, (int, float)):
            if sequence_length > length_bounds:
                continue

        # Фильтрация по качеству
        average_quality = calculate_average_quality(quality)
        if average_quality < quality_threshold:
            continue

        # Добавление отфильтрованной последовательности в результат
        filtered_seqs[seq_name] = (sequence, quality)

    return filtered_seqs

def run_dna_rna_tools(*args):
    sequences = args[:-1]
    procedure = args[-1]

    results = []
    for seq in sequences:
        if procedure == 'transcribe':
            result = transcribe(seq)
        elif procedure == 'reverse':
            result = reverse(seq)
        elif procedure == 'complement':
            result = complement(seq)
        elif procedure == 'reverse_complement':
            result = reverse_complement(seq)
        else:
            result = "Unknown procedure"

        results.append(result)

    if len(results) == 1:
        return results[0]
    else:
        return results

def amino_acid_tools(*args: str):
    """
    Performs functions for working with amino acid sequences.

       Parameters:
            The function should accept an unlimited number of protein sequences (str) as input,
        the last variable should be the function (str) that you want to execute.
            The amino acid sequence can consist of both uppercase and lowercase letters.
      Input example:
            amino_acid_tools('LVElkPL','CpUPQWhmrY','McgMmLcTTG','molecular_weight')

            or

            amino_acid_tools('LVElkPL','CpUPQWhmrY','random','molecular_weight')


      Function:
            molecular weight: calculates the molecular weight of an amino acid chain
            long_amino_code: converts translations from one letter to translations
            from three letters
            amino_to_rna translates a sequence of amino acids into a possible sequence of nucleic acids
            amino_seq_charge: estimates the total charge of the amino acid chain in a neutral aqueous solution (pH = 7)

        Returns:
            If one sequence is supplied, a string with the result is returned.
            If several are submitted, a list of strings is returned.
            Depending on the function performed, the following returns will occur:
                long_amino_code (str) or (list): translated sequence from one-letter in three-letter code
                molecular_weight (int) or (list): amino acid sequence molecular weight number or list of numbers
                amino_to_rna (str) or (list): possible RNA sequence
                amino_seq_charge (str) or (list): "positive", "negative" or "neutral"
    """
    *seqs, function = args
    d_of_functions = {'long_amino_code' : long_amino_code,
                      'molecular_weight': molecular_weight,
                      'amino_to_rna' : amino_to_rna,
                      'amino_seq_charge' : amino_seq_charge}
    answer = []
    aminoacid_seqs = amino_seqs(seqs)
    for sequence in aminoacid_seqs:
        answer.append(d_of_functions[function](sequence))
    if len(answer) == 1:
        return answer[0]
    else:
        return answer
