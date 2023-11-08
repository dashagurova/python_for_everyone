fhand = open('mailbox.txt')

for line in fhand:
    line = line.rstrip()
    wrd = line.split()
    if len(wrd) < 3 or wrd[0] != 'From':
        continue
    print(wrd[2])

