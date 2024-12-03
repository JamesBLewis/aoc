import re

with open("input") as input:
    input_string = ""
    for line in input:
        input_string += line.strip()
    total = 0
    # Find all words that end with 'ain'
    matches = re.findall(r"(mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\))|(do\(\))|(don't\(\))", input_string)
    print(matches)
    on=True
    for match in matches:
        # determine match kind
        if match[0] != '': # it's a mul
            if not on: # skip
                continue
            n1 = 0
            n2 = 0
            for c in range(len(match[0])):
                if match[0][c] == ',':
                    n1 = int(match[0][4:c])
                    n2 = int(match[0][c+1:-1])
                    working = True
                    break
            total += (n1 * n2)
        elif match[1] != '':
            on=True
        elif match[2] != '':
            on=False
        else:
            print(match)
            raise Exception("this should not happen")
    print(total)


# incorrect 8133565