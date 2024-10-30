path = "/storage/emulated/0/Documents/Project Euler/Text/0067_triangle.txt"


def read_in():
    # Read the text in from the file path
    global path
    file = open(path)
    lines = file.readlines()

    # Sanitise
    output = list()
    for line in lines:
        numbers = line[:-1].split(" ")
        current_row = list()
        for number in numbers:
            current_row.append(int(number))
        output.append(current_row)

    return output


def main():
    triangle = read_in()
    triangle.reverse()
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i]) - 1):
            triangle[i + 1][j] += max(triangle[i][j], triangle[i][j + 1])
    print(triangle[99][0])


if __name__ == "__main__":
    main()

