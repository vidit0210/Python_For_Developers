list()
set()
tuple()
dict()

# point = {'x': 1, 'y': 2}
point = dict(x=dict(q=3, w=8), y=2)
point['z'] = 3
print(point['x']['q'])
print(point.get())
