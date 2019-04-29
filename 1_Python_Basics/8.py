# loops strings are terable ,List are iterable,


for x in range(0, 11, 2):
    print(x)

names = ["Vidit", "Elon"]

for name in names:
    if(name.startswith("V")):
        print(name, "Name has been found")
        break
else:
    print('No name Found')

for i in range(3, 0):
    print(i)
