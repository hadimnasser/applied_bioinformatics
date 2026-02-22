def FrequentWords(Text, k):
    freqmap = {}
    for i in range(0, len(Text) - k + 1):
        Pattern = Text[i:i+k]
        if Pattern not in freqmap:
            freqmap[Pattern] = 1
        else:
            freqmap[Pattern] += 1
    max_count = max(freqmap.values())
    
    words = []
    for Pattern in freqmap:
        if freqmap[Pattern] == max_count:
            words.append(Pattern)
            
    return words

text = "" #enter dna fragment
k = #k-mer number
print(FrequentWords(text, k))