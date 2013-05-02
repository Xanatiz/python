def reverse(string):
    if not string:
        return ''
    else:
        return reverse(string[1:])+string[0]

def main(inputInt):
    return (int(reverse(bin(inputInt)[2:]), 2))
