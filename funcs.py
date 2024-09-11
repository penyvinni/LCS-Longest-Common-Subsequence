from itertools import product
def brute_force(seq1, seq2):
    max = 0
    max_sub = str()
    true_false_list = [x for x in product([True, False], repeat=len(seq1))]  #oloi oi sindiasmoi true false me to megethos ths seq1
    for true_false in true_false_list:
        subsequence = str()
        for index, boolean in enumerate(true_false):
            if boolean == True:
                subsequence += seq1[index]
        if len(subsequence) == 0:
            continue

        found = 0
        for letter in seq2:
            if letter == subsequence[found]:
                found += 1
            if found == len(subsequence):
                if len(subsequence) > max:
                    max = len(subsequence)
                    max_sub = subsequence
                break
            
    #print("BruteForse of " + seq1 + " and " + seq2 + " is " + max_sub)       
    return max, max_sub  #epistrefei ton max aritho kai thn max ipoakolouthia 



def lcs_method(seq1, seq2, m, n):
    
    L = [[0 for x in range(n+1)] for x in range(m+1)] # h lista me th max ypoakolouthia
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif seq1[i-1] == seq2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
                
    index = L[m][n]
    lcs = [""] * (index+1)
    lcs[index] = ""
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i-1] == seq2[j-1]:
            lcs[index-1] = seq1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
                
    #print("LCS of " + seq1 + " and " + seq2 + " is " + "".join(lcs))
    lcs_max = " "   
    lcs_str = lcs_max.join(lcs)
    ls = str(lcs_str).replace(" ", "")  #metatropi tou join se str gia na to emfanizei lo mazi
    return L[m][n], ls
    
      
    
# seq1 = "AATCGAG"
# seq2 = "CCATCGG"
# m = len(seq1)
# n = len(seq2)
# print("Brute Forse Method is:")
# print(brute_force('AATCGAG', 'CCATCGG')) 
# print("LCS method is:")
# print(lcs_method(seq1, seq2, m, n))