amino_acid = 'ARNDCEQGHILKMFPSTWYVUOarndceqghilkmfpstwyvuo'
short_code = list(amino_acid)
long_code = ['Ala', 'Arg', 'Asn', 'Asp', 'Cys', 'Glu', 'Gln', 'Gly', 'His', 'Ile', 'Leu', 'Lys', 'Met', 'Phe', 'Pro',
             'Ser', 'Thr', 'Trp', 'Tyr', 'Val', 'Sec', 'Pyl',
             'Ala', 'Arg', 'Asn', 'Asp', 'Cys', 'Glu', 'Gln', 'Gly', 'His', 'Ile', 'Leu', 'Lys', 'Met', 'Phe', 'Pro',
             'Ser', 'Thr', 'Trp', 'Tyr', 'Val', 'Sec', 'Pyl']
codon_table = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'N': ['AAU', 'AAC'],
    'D': ['GAU', 'GAC'],
    'C': ['UGU', 'UGC'],
    'Q': ['CAA', 'CAG'],
    'E': ['GAA', 'GAG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'K': ['AAA', 'AAG'],
    'M': ['AUG'],
    'F': ['UUU', 'UUC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'W': ['UGG'],
    'Y': ['UAU', 'UAC'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'STOP': ['UAA', 'UAG', 'UGA'],
    'f': ['uuu', 'uuc'],
    'l': ['uua', 'uug', 'cuu', 'cuc', 'cua', 'cug'],
    's': ['ucu', 'ucc', 'uca', 'ucg', 'agu', 'agc'],
    'y': ['uau', 'uac'],
    'c': ['ugu', 'ugc'],
    'w': ['ugg'],
    'p': ['ccu', 'ccc', 'cca', 'ccg'],
    'h': ['cau', 'cac'],
    'q': ['caa', 'cag'],
    'r': ['cgu', 'cgc', 'cga', 'cgg', 'aga', 'agg'],
    'i': ['auu', 'auc', 'aua'],
    'm': ['aug'],
    't': ['acu', 'acc', 'aca', 'acg'],
    'n': ['aau', 'aac'],
    'k': ['aaa', 'aag'],
    'v': ['guu', 'guc', 'gua', 'gug'],
    'a': ['gcu', 'gcc', 'gca', 'gcg'],
    'd': ['gau', 'gac'],
    'e': ['gaa', 'gag'],
    'g': ['ggu', 'ggc', 'gga', 'ggg'],
    'stop': ['uaa', 'uag', 'uga']
}
weight_amino = [71.08, 156.2, 114.1, 115.1, 103.1, 129.1, 128.1, 57.05, 137.1, 113.2, 113.2, 128.2, 131.2, 147.2, 97.12, 87.08,
         101.1, 186.2, 163.2, 99.13, 168.05, 255.3,
         71.08, 156.2, 114.1, 115.1, 103.1, 129.1, 128.1, 57.05, 137.1, 113.2, 113.2, 128.2, 131.2, 147.2, 97.12, 87.08,
         101.1, 186.2, 163.2, 99.13, 168.05, 255.3]

import random

def long_amino_code(sequence):
    """
        Function translates a given sequence of one-letter amino acids
    into a more understandable sequence of amino acids consisting of three letters

        Parameters:
            sequence (str): each letter refers to one-letter coded proteinogenic amino acids or "random"
        Returns:
            (str) translated in three-letter code
    """
    if sequence != 'random':
        d_names = dict(zip(short_code, long_code))
        recording = sequence.maketrans(d_names)
        return sequence.translate(recording)
    else:
        len = int(input("введите желаемую длину: "))
        bases = list(amino_acid)
        amino_sequencqe = ''.join(random.choice(bases) for i in range(len))
        d_names = dict(zip(short_code, long_code))
        recording = amino_sequencqe.maketrans(d_names)
        return "рандомная последовательнсть", amino_sequencqe, amino_sequencqe.translate(recording)

def molecular_weight(sequence):
    """
    Function calculates molecular weight of the amino acid chain
        Parameters:
            sequence (str): each letter refers to one-letter coded proteinogenic amino acids or "random"
        Returns:
            weight (float) Molecular weight of tge given amino acid chain in Da
        """
    if sequence != 'random':
        molecular_weights = dict(zip(short_code, weight_amino))
        weight = sum(molecular_weights.get(aa, 0) for aa in sequence)
        return weight
    else:
        len = int(input("введите желаемую длину: "))
        bases = list(amino_acid)
        amino_sequencqe = ''.join(random.choice(bases) for i in range(len))
        molecular_weights = dict(zip(short_code, weight_amino))
        weight = sum(molecular_weights.get(aa, 0) for aa in amino_sequencqe)
        return "рандомная последовательнсть", amino_sequencqe, weight

def amino_to_rna(amino_sequence):
    """
    Function translates an amino acid sequence into a possible RNA sequence
        Parameters:
                amino_sequence (str) or "random"
        Returns:
                (str) possible RNA sequence
    """
    if amino_sequence != 'random':
        rna_sequence = ""

        for aminoacid in amino_sequence:
            if aminoacid in codon_table:
                codons = codon_table[aminoacid]
                # Selecting one random codon
                codon = random.choice(codons)
                rna_sequence += codon
            else:
                print("Unknown amino acid code: ", aminoacid)

        return rna_sequence
    else:
        len = int(input("введите желаемую длину: "))
        bases = list(amino_acid)
        amino_sequencqe = ''.join(random.choice(bases) for i in range(len))
        rna_sequence = ""

        for aminoacid in amino_sequencqe:
            if aminoacid in codon_table:
                codons = codon_table[aminoacid]
                # Selecting one random codon
                codon = random.choice(codons)
                rna_sequence += codon
            else:
                print("Unknown amino acid code: ", aminoacid)
        return "рандомная последовательнсть", amino_sequencqe, rna_sequence


def amino_seq_charge(amino_sequence):
    """
    Function evaluates the overall charge of the aminoacid chain in neutral aqueous solution (pH = 7)
        Parameters:
            amino_sequence (str): amino acid sequence of proteinogenic amino acids or "random"
        Returns:
            (str): "positive", "negative" or "neutral"
    """
    if amino_sequence != 'random':
        aminoacid_charge = {'R': 1, 'D': -1, 'E': -1, 'K': 1, 'O': 1}
        charge = 0
        for aminoacid in amino_sequence.upper():
            if aminoacid in 'RDEKO':
                charge += aminoacid_charge[aminoacid]
        if charge > 0:
            return 'positiv'
        elif charge < 0:
            return 'negativ'
        else:
            return 'neutral'
    else:
        len = int(input("введите желаемую длину: "))
        bases = list(amino_acid)
        amino_sequencqe = ''.join(random.choice(bases) for i in range(len))
        aminoacid_charge = {'R': 1, 'D': -1, 'E': -1, 'K': 1, 'O': 1}
        charge = 0
        for aminoacid in amino_sequencqe.upper():
            if aminoacid in 'RDEKO':
                charge += aminoacid_charge[aminoacid]
        if charge > 0:
            return "рандомная последовательнсть", amino_sequencqe, 'positiv'
        elif charge < 0:
            return "рандомная последовательнсть", amino_sequencqe, 'negativ'
        else:
            return "рандомная последовательнсть", amino_sequencqe, 'neutral'

def amino_seqs(amino_sequence):
    """
    Leaves only the amino acid sequences from the fed into the function.
        Parameters:
            amino_sequence (list): amino acid sequence list or "random"
        Returns:
            amino_seqs (list): amino acid sequence list without non amino acid sequence
    """
    if amino_sequence != 'random':
        aminoac_seqs = []
        for seq in amino_sequence:
            unique_chars = set(seq)
            amino_acids = set(amino_acid)
            if unique_chars <= amino_acids:
                aminoac_seqs.append(seq)
        return aminoac_seqs
    else:
        len = int(input("введите желаемую длину: "))
        bases = list(amino_acid)
        amino_sequencqe = ''.join(random.choice(bases) for i in range(len))
        aminoac_seqs = list(amino_sequencqe)
        return "рандомная последовательнсть", amino_sequencqe, aminoac_seqs

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
