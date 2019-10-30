x = int(input('Stunden der momentanen Uhrzeit(berreich von 1-24): '))
y = int(input('Minuten der Momentanen Uhrzeit: '))
z = int(input('Wie viele Minuten FLiegen sie schon?: '))

xm = x * 60
w = xm + y
a = w - z
c=z+30
boarding = w - c

if a < 0 :
	b = 24 * 60 + a
	print('i',b//60,':',b%60)
else:
	print('i',a//60,':',a%60)

if boarding < 0 :
	b = 24 * 60 + boarding
	print('ii',b//60,':',b%60)
else:
	print('ii',boarding//60,':',boarding%60)