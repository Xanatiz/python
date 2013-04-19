def reverse(string):

    if not string:
        return ''
    else:
        return reverse(string[1:])+string[0]

def main(inputInt):
    binary=bin(inputInt)[2:]
    print(int(reverse(binary), 2))
