#Write a program to compute and output the frequency of each nucleotide in a
#DNA sequence using a dictionary (see lec. 9).
#   Output the frequencies in most-occurrences to least-occurrences order

#seq = "ACCCGTTGGCATAAATGCAGTTCAG"
seq = "ACTG"

totalNuc = len(seq)

counts = {'A':0, 'T':0, 'C':0, 'G':0}

for nuc in seq:
    if nuc in counts:
        counts[nuc] += 1

sorted_counts = sorted(counts.items(), key=lambda item: item[1])
rev_sorted = reversed(sorted_counts)

for nuc, count in rev_sorted:
    frequency = round(100*count/totalNuc,2)
    print(nuc,"Frequencies",frequency,"%")
