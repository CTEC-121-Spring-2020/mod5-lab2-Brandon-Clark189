

# Practice 2


def ageClass(age):
    if (0 <= age <= 1):
        return "I"
    elif (1 < age < 13):
        return "C"
    elif (13 <= age <= 18):
        return "T"
    elif (18 < age < 150):
        return "A"
    else:
        return "U"


def main():

    print(ageClass(0), "expect I: 0 input")
    print(ageClass(1000), "expect U: 1000 input")

main()

