mark = {'Johnny':67, 'Canny':80, 'Alex':32, 'Ganny':14, 'David':78}
mark_rev = {}

print(mark)

names = reversed(mark.keys())
scores = reversed(mark.values())

mark_rev.update(zip(names,scores))

for i in range (len(mark_rev),-1,-1):
    if len(mark_rev) > 0:
        print(mark_rev)
        mark_rev.popitem()
    else:
        print(mark_rev)


