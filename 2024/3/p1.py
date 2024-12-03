import re

with open("input") as input:
    input_string = ""
    for line in input:
        input_string += line.strip()
    total = 0
    # Find all words that end with 'ain'
    matches = re.findall(r'mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)', input_string)
    #print(matches)
    for match in matches:
        n1 = 0
        n2 = 0
        for c in range(len(match)):
            if match[c] == ',':
                n1 = int(match[4:c])
                n2 = int(match[c+1:-1])
                working = True
                break
        total += (n1 * n2)
    #print(total)


# incorrect 31341460