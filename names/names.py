import time

start_time = time.time() # Leave the timer,

f = open('names_1.txt', 'r')
'''
Does this seem faster? 'cause it's not!
suspected_doppelgangers = {}
while True:
    name = f.readline().rstrip()
    suspected_doppelgangers[name] = True
    if name == '':
        break
'''
# Actually faster:
suspected_doppelgangers = { n: True for n in f.read().split("\n") }
f.close() # I think we have to read this.

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close() # I think we have to read this too...

duplicates = []

'''
Original Solution:
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

# suspected_doppelgangers = { n: True for n in names_1 }
for name in names_2:
    if suspected_doppelgangers.get(name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")