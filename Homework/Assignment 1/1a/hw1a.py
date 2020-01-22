#BT3051 Assignment 1a
#Roll number: BE17B037
#Collaborators: none
#Time: 30:00

class Gene:
    def __init__(self, geneID = "", sequence = ""):
        self.geneID = geneID
        self.sequence = sequence
        self.length = len(sequence)
    def __add__(self, other):
        geneID = self.geneID + other.geneID
        sequence = self.sequence + other.sequence
        return Gene(geneID, sequence)
    def __neg__(self):
        comp_seq = ""
        for i in self.sequence:
            comp_seq = comp_seq + "TACG"["ATGC".find(i)]
        return comp_seq

def GC_content(a):
    GC_bases = 0
    for i in a.sequence:
        if i in "GC":
            GC_bases += 1
    return round((GC_bases*100/a.length), 1)
