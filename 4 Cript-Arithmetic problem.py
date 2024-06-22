import itertools

def is_solution_valid(s1, s2, s3, mapping):
    def word_to_number(word):
        return int("".join(str(mapping[char]) for char in word))

    num1 = word_to_number(s1)
    num2 = word_to_number(s2)
    num3 = word_to_number(s3)
    
    return num1 + num2 == num3

def solve_cryptarithmetic(s1, s2, s3):
    unique_chars = set(s1 + s2 + s3)
    if len(unique_chars) > 10:
        raise ValueError("Too many unique characters for digits 0-9")

    for perm in itertools.permutations(range(10), len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        
        # Ensure that no word starts with a zero
        if mapping[s1[0]] == 0 or mapping[s2[0]] == 0 or mapping[s3[0]] == 0:
            continue
        
        if is_solution_valid(s1, s2, s3, mapping):
            return {char: digit for char, digit in zip(unique_chars, perm)}

    return None

if __name__ == "__main__":
    s1 = "SEND"
    s2 = "MORE"
    s3 = "MONEY"

    solution = solve_cryptarithmetic(s1, s2, s3)
    
    if solution:
        print("Solution found:")
        for char, digit in solution.items():
            print(f"{char} = {digit}")
    else:
        print("No solution found.")
