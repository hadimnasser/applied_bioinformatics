def FindClumps(Genome, k, L, t):
    all_clumps = set()
    freq_map = {}
    
    first_window = Genome[0:L]
    for i in range(L - k + 1):
        pattern = first_window[i:i+k]
        freq_map[pattern] = freq_map.get(pattern, 0) + 1
        if freq_map[pattern] >= t:
            all_clumps.add(pattern)
            
    for i in range(1, len(Genome) - L + 1):
        out_pattern = Genome[i-1 : i-1+k]
        freq_map[out_pattern] -= 1
        in_pattern = Genome[i + L - k : i + L]
        freq_map[in_pattern] = freq_map.get(in_pattern, 0) + 1
        if freq_map[in_pattern] >= t:
            all_clumps.add(in_pattern)
            
    return list(all_clumps)

def load_genome(filename):
    """Loads and cleans the genome file."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        if lines and lines[0].startswith('>'):
            return "".join(line.strip() for line in lines[1:])
        return "".join(line.strip() for line in lines)

file_name = '/Users/nasserhadi/Downloads/hadi_protfolio/E_coli_genome.txt'

try:
    genome = load_genome(file_name)
    # Use the specific parameters assigned to your dataset
    k, L, t = 9, 500, 3 
    
    results = FindClumps(genome, k, L, t)
    
    print(f"Success! Found {len(results)} distinct clumps.")
    print(*(results))

except FileNotFoundError:
    print(f"Error: Could not find '{file_name}'. Check the sidebar for the file name.")