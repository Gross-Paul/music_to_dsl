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



# split when there is a line with only \n
splitted = re.split("\n\n", text)

# read until end of file
for block in splitted:
    #print(block)
    lines = block.split("\n")
    # split line into list of words
    # print(words)

    for i in range(len(lines[0])):
        dominant_letter = ""
        
        


        for j in range(len(lines)):
            if lines[j][i].isalpha():
                tone = lines[j][0]
                dominant_letter = lines[j][i]
            if lines[j][i] == "-" and not dominant_letter.isalpha():
                dominant_letter = "-"

            
        if dominant_letter == "-":
            print("noTone(7);\ndelay(100);")

        elif str(dominant_letter).isalpha():
            note = ""
            if dominant_letter.isupper():
                note = dominant_letter + "S" + tone
            elif dominant_letter.islower():
                note = dominant_letter.upper() + tone
            print(f"tone(7,{notesDict[note]});\ndelay(100);")


