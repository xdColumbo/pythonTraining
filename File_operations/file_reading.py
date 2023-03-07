# file = open("sentences.txt", "r", encoding="utf-8")

# The r is for reading and encoding is important because there may be foreign characters in the text

# for line in file:
#    print(line.strip())

# line = file.readline()

# while line:
#    print(line.strip())
#    line = file.readline()

# file.close()


# if you use with method you don't have to close the file manually it will close itself

with open("sentences.txt", "r", encoding="utf-8") as file:
    # readlines() - sorts the rows into a list
    # read() - Read the whole file at once (Not recommended for large files)
    # readline() - Read one line and write out
    line = file.read()
    print(line)

    # while line:
    #     print(line.strip())
    #     line = file.readline()
