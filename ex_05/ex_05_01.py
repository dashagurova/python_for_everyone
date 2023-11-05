num = 0
total = 0.0

while True :
    sval = input('Enter number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Bad Value')
        continue
    num = num + 1
    total = total + fval

print(total,num,total/num)