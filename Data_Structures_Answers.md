Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O(1).

2. What is the space complexity of your ring buffer's `append` function?

O(1). Unless you are counting the bits allocated through appending itself, which you might be, in which case I suppose it would be technically O(n), but within such a tiny range of n, and you've already allocated it, that who cares? There is no real additional space cost to store the reference.

3. What is the runtime complexity of your ring buffer's `get` method?

O(n) because it temporarily allocates a new list to use for purging None entries.

4. What is the space complexity of your ring buffer's `get` method?

O(n) because it temporarily allocates a new list to use for purging None entries. This only affects RAM though, so I would not even count it when discussing disk space complexity, as it were.


5. What is the runtime complexity of the provided code in `names.py`?

O(n * n') because it iterates over the entire second list for every instance in the first list. Though it's kind of weird to call it n^2, I believe it's correct nonetheless, because n implies it's a single variable, whereas there are "two" n's here.

6. What is the space complexity of the provided code in `names.py`?

O(n), because it just reads out two lists.

7. What is the runtime complexity of your optimized code in `names.py`?

O(n). After reading in the lists, I iterate over both lists once.

8. What is the space complexity of your optimized code in `names.py`?

O(1.5n) because I do allocate an additional dictionary for half of it. I am going to try to see if I can optimize away that problem and read it initially into a dictionary.