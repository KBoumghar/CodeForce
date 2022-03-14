def codeforceParse(str):
    arr = str.split()

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr


def codeforce1650(l, r, a):
    l = int(l)
    r = int(r)
    a = int(a)
    temp = r%a
    value1 = r//a + temp

    value2 = 0
    temp2 = r - temp - 1

    if temp2 >= l:
        value2 = temp2//a + a-1
    return max(value1, value2)



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