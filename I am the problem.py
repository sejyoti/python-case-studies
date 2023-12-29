#Problem: Accurately align two DNA sequences to identify similarities and potential functional relationships.
#explain the code in python
#Needleman-Wunsch (global alignment): Aligns entire sequences, finding best overall match. Ideal for comparing sequences of similar length and expected overall similarity.
#Smith-Waterman (local alignment): Focuses on finding best-matching segments, even within dissimilar sequences. Suitable for identifying conserved regions or motifs.

from Bio import pairwise2
from Bio.Seq import Seq
from Bio.Align import PairwiseAligner

seq1 = Seq("ACTAGGGTT")
seq2 = Seq("AGGTT")

aligner = PairwiseAligner()

alignments = aligner.align(seq1, seq2)

best_alignment = alignments[0]
print(best_alignment)
