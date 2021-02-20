# Needed to look the code up on the internet because I don't know how it works
def k_mer(dna, k):
    dictionary = {}
    total_kmers = len(dna) - k + 1
    for i in range(total_kmers):
        kmer = dna[i:i + k]
        if kmer not in dictionary:
            dictionary[kmer] = 0
        dictionary[kmer] += 1
    return dictionary


if __name__ == "__main__":
    dna_str = "GTAGAGCTGT"
    k_val = int(input("Input value of k: "))
    print(k_mer(dna_str, k_val))
