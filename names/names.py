import time

start_time = time.time() # Leave the timer,

'''
# Original Solution:

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close() # I think we have to read this too...

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close() # I think we have to read this too...

duplicates = []

for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

# My Fast Solution:
f = open('names_1.txt', 'r')

# Does this seem faster? 'cause it's not!
# suspected_doppelgangers = {}
# while True:
#     name = f.readline().rstrip()
#     suspected_doppelgangers[name] = True
#     if name == '':
#         break
# Actually faster:
suspected_doppelgangers = { n: True for n in f.read().split("\n") }
f.close() # I think we have to read this.

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close() # I think we have to read this too...

# suspected_doppelgangers = { n: True for n in names_1 }
for name in names_2:
    if suspected_doppelgangers.get(name):
        duplicates.append(name)


'''
# Memory Constrained Solution:

f = open('names_1.txt', 'r')
names_1 = sorted(f.read().split("\n"))  # List containing 10000 names
f.close() # I think we have to read this too...

f = open('names_2.txt', 'r')
names_2 = sorted(f.read().split("\n"))  # List containing 10000 names
f.close() # I think we have to read this too...

j = 0
k = 0

duplicates = []

while True:
    try:
        if names_1[j] == names_2[k]:
            duplicates.append(names_2[k])
            j +=1
            k +=1
        elif names_1[j] < names_2[k]:
            j +=1
        elif names_1[j] > names_2[k]:
            k += 1
    except IndexError:
        break
'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")