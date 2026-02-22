def HammingDistance(p, q):
    return sum(1 for a, b in zip(p, q) if a != b)

def GetScore(Motifs):
    k = len(Motifs[0])
    t = len(Motifs)
    score = 0
    for j in range(k):
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for i in range(t):
            counts[Motifs[i][j]] += 1
        score += (t - max(counts.values()))
    return score

def GetProfile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    # Initialize 4xK matrix with zeros
    profile = [[0.0] * k for _ in range(4)]
    nuc_to_idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
    for j in range(k):
        for i in range(t):
            nuc = Motifs[i][j]
            profile[nuc_to_idx[nuc]][j] += 1
        for r in range(4):
            profile[r][j] /= t
    return profile

def ProfileMostProbable(Text, k, Profile):
    max_prob = -1.0
    most_probable = Text[0:k] 
    nuc_to_idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
    for i in range(len(Text) - k + 1):
        pattern = Text[i:i+k]
        prob = 1.0
        for j in range(k):
            prob *= Profile[nuc_to_idx[pattern[j]]][j]
        
        if prob > max_prob:
            max_prob = prob
            most_probable = pattern
    return most_probable

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = [string[0:k] for string in Dna]
    first_string = Dna[0]
    for i in range(len(first_string) - k + 1):
        Motifs = [first_string[i:i+k]]
        
        for j in range(1, t):
            current_profile = GetProfile(Motifs)
            next_motif = ProfileMostProbable(Dna[j], k, current_profile)
            Motifs.append(next_motif)
            
        if GetScore(Motifs) < GetScore(BestMotifs):
            BestMotifs = Motifs
            
    return BestMotifs

k_val, t_val = 3, 5 #k,t vals
dna_list = "   ".split() #dna sample

result = GreedyMotifSearch(dna_list, k_val, t_val)
print(*(result))