def collatz(n):
    sequence = [n]
    while n != 1:
        # if even
        if n % 2 == 0:
            n /= 2
        # if odd
        else:
            n = 3*n + 1

        sequence.append(int(n))

    return {
        "sequence":sequence,
        "steps":(len(sequence) - 1),
        "highest":max(sequence)
    }

if __name__ == "__main__":
    col = collatz(int(input("Number: ")))
    print(", ".join((str(n) for n in col["sequence"])))
    print(f"Highest: {col['highest']}")
    print(f"Steps: {col['steps']}")
