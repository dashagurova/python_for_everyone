xh = input('Enter hours: ')
xr = input('Enter rate: ')
fh = float(xh)
fr = float(xr)

def computepay(fh,fr):
    if fh < 40:
        xp = fh * fr
        return xp
    else:
        overr = fr * 1.5
        overh = fh - 40
        xp = (overh * overr) + (fh * fr)
        return xp


print('Pay: ',computepay(fr,fh))