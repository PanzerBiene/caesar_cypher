def read_letters(file_name,c):
    f = open(file_name)


    contents = f.read()
    i = 0
    output = []
    cypher = create_cypher(c)
    while i < len(contents):
        letter = contents[i]
        output.append(caeser_cypher(letter, cypher))
        i += 1
    print(cypher)
    return output
def create_cypher(c):
    cypher = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]
    print(cypher)
    if c > 0:
        while c > 0:
            a = cypher.pop(0)
            cypher.append(a)
            c -= 1
    elif c < 0:
        while c > 0:
            a = cypher.pop()
            cypher.insert(a,0)
            c += 1
    else:
        return cypher
    return cypher

def caeser_cypher(letter, cypher):
    cypher_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]
    try:
        index = cypher_letters.index(letter)
        new_letter = cypher[index]
    except:
        new_letter = letter
    return new_letter

print(read_letters("letter.txt",4))

#