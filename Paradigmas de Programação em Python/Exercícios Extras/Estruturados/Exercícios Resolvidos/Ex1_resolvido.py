
def fibonnaci_sequence(term1:int, term2:int) -> list:
    sequence:list = [term1, term2]
    while len(sequence) < 10:
        next_term:int = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

term1:int = 1
term2:int = 0

print(fibonnaci_sequence(term1, term2))
