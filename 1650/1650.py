def codeforceParse(str):
    arr = str.split()

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr



def main():
    max = input()

    counter = 0

    while (counter < int(max)):
        size = input()
        str = input()
        arr = codeforceParse(str)
        codeforce1638(size, arr)
        counter += 1

    return 0


if __name__ == "__main__":
    main()