import math

def main():
    x_values = [i * 2 / 999 for i in range(1000)]

    print("x\tsin(x)")
    for x in x_values:
        print(f"{x}\t{math.sin(x)}")

if __name__ == "__main__":
    main()
