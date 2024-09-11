from funcs import *
import random
from itertools import combinations


if __name__ == "__main__":
    x = 10  # 100 akolouthies DNA
    chars = 20 # 200 xaraktires h kathe mia
    available_chars = "AGCT"  #oi 4 xaraktires pou mporei na exei kathe akolouthia

    # Create dna sequences
    dna_sequences = list()
    for _ in range(x):
        new_sequence = str()
        for _ in range(chars):
            new_sequence += available_chars[random.randint(0, 3)]  #dimiourgei tixaies akolouthies DNA
        dna_sequences.append(new_sequence)


    # Create all combinations and run algorithm
    combs = combinations(dna_sequences, 2)
    max_length = 0
    result = list()
    for seq1, seq2 in combs:
        max, maxsub = brute_force(seq1, seq2)  #kanei upack kai epistrefei 1 tupple
        if max > max_length:
            result = list()
            result.append((seq1, seq2, maxsub, max))
            max_length = max
        elif max == max_length:
            result.append((seq1, seq2, maxsub, max))


    
    # Create all combinations and run algorithm
    combs = combinations(dna_sequences, 2)
    max_lcs = 0
    result = list()
    for seq1, seq2 in combs:
        m = len(seq1)  #megethos twn akolouthiwn
        n = len(seq2)
        max, sequence = lcs_method(seq1, seq2, m, n)  #kanei upack kai epistrefei 1 tupple
        if max > max_lcs:
            result = list()
            result.append((seq1, seq2, sequence, max))
            max_lcs = max
        elif max == max_lcs:
            result.append((seq1, seq2, sequence, max))

    print(dna_sequences)  #oles oi ypoakolouthies
    print("Brute forse method:")
    print(result) # to apotelesma tou brute forse
    print("LCS method:")
    print(result)  #to apotelesma tou lcs
    print("\nLength of longest common sub-sequence: ")
    print(max_lcs) #to megethos tis max ypoakolouthias
    print("Longest commmon sub-sequence")
    print(sequence)  # h max ypoakolouthia 
    