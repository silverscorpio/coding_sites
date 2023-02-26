### Exercise - 17 - RNA Transcription

def to_rna(dna_strand):
    code = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = []
    if dna_strand == '':
        return ''
    else:
        for i in dna_strand:
            rna.append(code[i])
        return ''.join(rna)