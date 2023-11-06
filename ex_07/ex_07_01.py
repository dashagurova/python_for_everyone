filename = input('Enter filename: ')
try:
    fhandle = open(filename,"r")
except:
    print('Bad file name')
    quit()
count = 0
sum = 0

for line in fhandle:
    if line.startswith('X-DSPAM-Confidence'):
        start = line.find(':')
        num = float(line[start+1:])
        sum = sum + num
        count = count + 1
        
print('Avrg spam confidence: ',sum/count)