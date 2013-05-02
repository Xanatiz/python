def main():
    value=[]
    data = input()
    data = splitToList(data)
    for i in range (0, int(data[0])):
        read=input()
        listOfTwo=splitToList(read)
        value.append((i+1, int(listOfTwo[0])/(1/(i+1)), listOfTwo[1]))
    sort(value)
    for j in range(0, int(data[1])):
        print(value[j][2])

def sort(listOfTuple):
    for i in range (1, len(listOfTuple)):
        for j in range(len(listOfTuple)-1,0,-1):
            if listOfTuple[j][1]>listOfTuple[j-1][1] or \
                    (listOfTuple[j][1]==listOfTuple[j-1][1] and \
                         listOfTuple[j][0]>listOfTuple[j-1][0]):
                temp=listOfTuple[j]
                listOfTuple[j]=listOfTuple[j-1]
                listOfTuple[j-1]=temp

def splitToList(string):
    for I in range (0, len(string)):
        if string[I] == ' ':
            return [string[0:I], string[I+1:]]


if __name__=="__main__":
    main()
