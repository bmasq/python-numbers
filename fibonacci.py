def fibonacci(n):
    sequence = [0, 1]
    for i in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    print(", ".join(str(n) for n in fibonacci(int(input("Number: ")))))