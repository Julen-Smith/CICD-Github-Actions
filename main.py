def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("El número debe ser no negativo")
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    print("Factorial de 5:", factorial(5))