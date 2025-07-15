squares = set([x*x for x in range(1, 32)])

def main():
    for i in range(1, 1001):
        if i in squares:
            continue


if __name__ == "__main__":
    main()
