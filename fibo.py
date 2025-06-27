def fibonacci_recursive(n):

    if n < 0:
    
        raise ValueError("Input cannot be a negative number.")

    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def main():

    n=20
    print(f"F({n}) = {fibonacci_recursive(n)}")

if __name__ == "__main__":
    main()
