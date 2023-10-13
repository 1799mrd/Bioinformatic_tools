def transcribe(seq):
    transcribed_seq = ""
    for base in seq:
        if base == 'T':
            transcribed_seq += 'U'
        elif base == 't':
            transcribed_seq += 'u'
        else:
            transcribed_seq += base
    return transcribed_seq

def reverse(seq):
    return seq[::-1]

def complement(seq):
    complement_seq = ""
    for base in seq:
        if base == 'A':
            complement_seq += 'T'
        elif base == 'T':
            complement_seq += 'A'
        elif base == 'C':
            complement_seq += 'G'
        elif base == 'G':
            complement_seq += 'C'
        elif base == 'a':
            complement_seq += 't'
        elif base == 't':
            complement_seq += 'a'
        elif base == 'c':
            complement_seq += 'g'
        elif base == 'g':
            complement_seq += 'c'
        else:
            complement_seq += base
    return complement_seq

def reverse_complement(seq):
    return complement(reverse(seq))
