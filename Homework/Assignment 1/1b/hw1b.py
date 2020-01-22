#BT3051 Assignment 1b
#Roll number: BE17B037
#Collaborators: none
#Time: 1:45:00

import sys
import doctest

def read_FASTA(fname):
    """
    Read FASTA file to return a list of (sequence_name, sequence) tuples
    """
    seq_dict = dict()
    fn_obj = open(fname)
    for line in fn_obj:
        line = line.rstrip()
        if line[0] == ">":
            seq_name = line[1:]
            seq_dict[seq_name] = ""
        else:
            seq_dict[seq_name] = seq_dict[seq_name] + line
    fn_obj.close()
    sequences = []
    for seq_name, seq in seq_dict.items():
        sequences.append((seq_name, seq))
    return sequences

def identify_orfs(dnaStrand):
    """
    Return a list of orf strings from a dnaStrand (could be more than 6 as well)
    """
    frames = []
    
    temp_frame = ""
    read_bp = False
    start_codons = 0
    for i in range(0, len(dnaStrand)-2, 3):
        base = dnaStrand[i:i+3]
        if base == "ATG":
            read_bp = True
            start_codons += 1
        if base == "TAA" or base == "TAG" or base == "TGA":
            read_bp = False
            while(start_codons > 0):
                index = temp_frame.find("ATG")
                temp_frame = temp_frame[index::]
                if not temp_frame in frames:
                    frames.append(temp_frame)
                temp_frame = temp_frame[2::]
                start_codons -= 1
        if read_bp == True:
            temp_frame = temp_frame + base
        
    temp_frame = ""
    read_bp = False
    start_codons = 0
    for i in range(1, len(dnaStrand)-2, 3):
        base = dnaStrand[i:i+3]
        if base == "ATG":
            read_bp = True
            start_codons += 1
        if base == "TAA" or base == "TAG" or base == "TGA":
            read_bp = False
            while(start_codons > 0):
                index = temp_frame.find("ATG")
                temp_frame = temp_frame[index::]
                if not temp_frame in frames:
                    frames.append(temp_frame)
                temp_frame = temp_frame[2::]
                start_codons -= 1
        if read_bp == True:
            temp_frame = temp_frame + base
    
    temp_frame = ""
    read_bp = False
    start_codons = 0
    for i in range(2, len(dnaStrand)-2, 3):
        base = dnaStrand[i:i+3]
        if base == "ATG":
            read_bp = True
            start_codons += 1
        if base == "TAA" or base == "TAG" or base == "TGA":
            read_bp = False
            while(start_codons > 0):
                index = temp_frame.find("ATG")
                temp_frame = temp_frame[index::]
                if not temp_frame in frames:
                    frames.append(temp_frame)
                temp_frame = temp_frame[2::]
                start_codons -= 1
        if read_bp == True:
            temp_frame = temp_frame + base
    
    r_dnaStrand = dnaStrand[::-1]
    rc_dnaStrand = ""
    for i in r_dnaStrand:
        rc_dnaStrand = rc_dnaStrand + "TACG"["ATGC".find(i)]
    
    temp_frame = ""
    read_bp = False
    start_codons = 0
    for i in range(0, len(rc_dnaStrand)-2, 3):
        base = rc_dnaStrand[i:i+3]
        if base == "ATG":
            read_bp = True
            start_codons += 1
        if base == "TAA" or base == "TAG" or base == "TGA":
            read_bp = False
            while(start_codons > 0):
                index = temp_frame.find("ATG")
                temp_frame = temp_frame[index::]
                if not temp_frame in frames:
                    frames.append(temp_frame)
                temp_frame = temp_frame[2::]
                start_codons -= 1
        if read_bp == True:
            temp_frame = temp_frame + base
    
    temp_frame = ""
    read_bp = False
    start_codons = 0
    for i in range(1, len(rc_dnaStrand)-2, 3):
        base = rc_dnaStrand[i:i+3]
        if base == "ATG":
            read_bp = True
            start_codons += 1
        if base == "TAA" or base == "TAG" or base == "TGA":
            read_bp = False
            while(start_codons > 0):
                index = temp_frame.find("ATG")
                temp_frame = temp_frame[index::]
                if not temp_frame in frames:
                    frames.append(temp_frame)
                temp_frame = temp_frame[2::]
                start_codons -= 1
        if read_bp == True:
            temp_frame = temp_frame + base
    
    temp_frame = ""
    read_bp = False
    start_codons = 0
    for i in range(2, len(rc_dnaStrand)-2, 3):
        base = rc_dnaStrand[i:i+3]
        if base == "ATG":
            read_bp = True
            start_codons += 1
        if base == "TAA" or base == "TAG" or base == "TGA":
            read_bp = False
            while(start_codons > 0):
                index = temp_frame.find("ATG")
                temp_frame = temp_frame[index::]
                if not temp_frame in frames:
                    frames.append(temp_frame)
                temp_frame = temp_frame[2::]
                start_codons -= 1
        if read_bp == True:
            temp_frame = temp_frame + base
    
    return frames

def translate_DNA(dnaStrand):
    """
    Return the translated protein from the DNA strand
    >>> translate_DNA("ATGTATGATGCGACCGCGAGCACCCGCTGCACCCGCGAAAGCTGA")
    MYDATASTRCTRES
    """
    dna_table = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
                 "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
                 "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
                 "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
                 "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
                 "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
                 "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
                 "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
                 "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
                 "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
                 "TAA" :  "", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
                 "TAG" :  "", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
                 "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
                 "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
                 "TGA" :  "", "CGA" : "R", "AGA" : "R", "GGA" : "G",
                 "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G",
                 }
    protein = ""
    for i in range(0, len(dnaStrand)-2, 3):
        protein = protein + dna_table[dnaStrand[i:i+3]]
    return protein

def compute_protein_mass(protein_string):
    """
    Return the mass of a protein string as a float
    >>> compute_protein_mass("SKADYEK")
    821.392
    """
    mass_table = {"A" : 71.03711,
                  "C" : 103.00919,
                  "D" : 115.02694,
                  "E" : 129.04259,
                  "F" : 147.06841,
                  "G" : 57.02146,
                  "H" : 137.05891,
                  "I" : 113.08406,
                  "K" : 128.09496,
                  "L" : 113.08406,
                  "M" : 131.04049,
                  "N" : 114.04293,
                  "P" : 97.05276,
                  "Q" : 128.05858,
                  "R" : 156.10111,
                  "S" : 87.03203,
                  "T" : 101.04768,
                  "V" : 99.06841,
                  "W" : 186.07931,
                  "Y" : 163.06333,
                  }
    mass = 0
    for i in protein_string:
        mass = mass + mass_table[i]
    return mass

if __name__ == '__main__':
    for seq_name, seq in read_FASTA("hw1b_dataset.faa"):
        print (seq_name + ":")
        for orf in identify_orfs(seq):
            protein = translate_DNA(orf)
            print(protein, compute_protein_mass(protein))
