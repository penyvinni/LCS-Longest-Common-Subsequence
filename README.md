# LCS-Longest-Common-Subsequence

The solution of the maximum common subsequence problem, among others, has application in bioinformatics, and in particular in the analysis of similarities in DNA sequences. DNA sequences are represented by strings formed by 4 characters (A,G,C,T) representing the nucleotides adenine, guanine, cytosine and thymine.

# Περιγραφή Εργασίας

Το πρόβλημα της Longest Common Subsequence είναι ένα πρόβλημα στο οποίο δίνονται οι ακολουθίες DNA (στην περίπτωση μας βγαινουν τυχαία μέσω της random) και ζητείται να βρεθεί η max κοινή υποακολουθία από όλες τις ακολουθίες και το μέγεθός της. Για τη σχεδίαση του χρησιμοποιήθηκαν 2 αλγόριθμοι. Πρώτος είναι ο άπλοϊκός αλγόριθμος Brute Forse (ωμής δύναμης), ο οποίος δημιουργεί όλες τις υποακολουθίες της μίας ακολουθίας DNA και ελέγχει αν υπάρχει στην άλλη.Και τέλος, είναι ο αλγόριθμος LCS (δυναμικού προγραμματισμού), όπου κάνει ακριβώς την ίδια διαδικασία απλά φτιάχνει επιπλέον και έναν πίνακα απομνημόνευσης αποτελεσμάτων με ακέραιους αριθμούς, οι οποίοι αυξάνονται κάθε φορά που είναι κοινό το γράμμα στις ακολουθίες.

# Αποτελέσματα

Για την συγγραφή της εργασίας χρησιμοποιήθηκε η Python 3.9.2 και το Visual Studio Code.
Τα χαρακτηριστικά του υπολογιστή είναι Intel Core i7-1065G7 (1.30GHz - 1.50 GHz), 8 GB DDR3 (2667 MHz), λειτουργικό σύστημα Windows 10 Home x64. 
Τέλος, οδηγίες για την εκτέλση του κώδικα: python main.py και για την εκτέλεση των tests : python tests.py

