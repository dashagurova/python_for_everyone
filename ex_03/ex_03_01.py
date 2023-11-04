xh = input('Enter hours: ')
xr = input('Enter rate: ')
fh = float(xh)
fr = float(xr)
overr = fr * 1.5
print(overr)

if fh < 40:
    xp = fh * fr
else:
    overh = fh - 40
    print(overh)
    xp = (overh * overr) + (fh * fr)
print('Pay: ',xp)