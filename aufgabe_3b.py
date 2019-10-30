x = int(input('Geschätze ankunft in Stunden(berreich von 1-24): '))
y = int(input('Geschätze ankunft minuten: '))

z = 7 * 60
s = x * 60
m = s - z

if m < 0:
	b = m // 60
	a = 24 + b
	print('Vorraussätzliche Ankunft',a,':',y)
else:
	b = m // 60
	print('Vorraussätzliche Ankunft',b,':',y)