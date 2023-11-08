file = open('romeo.txt')
bag = dict()
for line in file:
    line = line.rstrip()
    line = line.split()
    for wrd in line:
        bag[wrd] = bag.get(wrd,0) + 1

count = -1
word = None
for k,v in bag.items():
    if v > count : 
        count = v
        word = k

print (word, count)
