import re
f = open("input.txt", "r")
tones_file = open("notes.txt", "r")
# 5-6 dashes == 1 second
# 1 dash == 0.2 seconds

notesDict = {}

for line in tones_file:
    line = line.split()
    notesDict[line[0]] = line[1]


# all lines until \n

text = f.read()

buzzers = 5


# split when there is a line with only \n
splitted = re.split("\n\n", text)

# read until end of file
for block in splitted:
    #print(block)
    lines = block.split("\n")
    # split line into list of words
    # print(words)

    for i in range(len(lines[0]) - 3):
        blank = True
        notes = []
        for j in range(len(lines)):
            compo = lines[j].split("|")
            #print(compo)
            line = compo[1]
            tone = compo[0]


            if line[i].isalpha():
                if line[i].isupper():
                    note = line[i] + "S" + tone
                elif line[i].islower():
                    note = line[i].upper() + tone
                notes.append(int(notesDict[note]))
                print(f"tone(0,{notesDict[note]}, 25);")
                got_note = False



        notes.sort()
        # take middle note
        
        if len(notes) > 0:
            print(f"tone(0,{notes[0]}, 25);")
             
        print("delay(125);")


