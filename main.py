import random

file1 = open('nouns.txt', 'r')
Lines = file1.readlines()


qualified_nouns = []
count = 0
for line in Lines:
    cleaned_line = line.strip()
    if any(x.isupper() for x in cleaned_line) or any(x.isdigit() for x in cleaned_line) or any(x.isspace() for x in cleaned_line):
        continue
    else:
        qualified_nouns.append(cleaned_line)

file1 = open('nouns_qualified.txt', 'w')
file1.writelines(qualified_nouns)
file1.close()

print(random.choices(qualified_nouns, k=10))