Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O1.

2. What is the space complexity of your ring buffer's `append` function?

O1.

3. What is the runtime complexity of your ring buffer's `get` method?

O(n) because it temporarily allocates a new list to use for purging None entries.

4. What is the space complexity of your ring buffer's `get` method?

O(n) because it temporarily allocates a new list to use for purging None entries.


5. What is the runtime complexity of the provided code in `names.py`?

O(n * n') because it iterates over the entire second list for every instance in the first list. Though it's kind of weird to call it n^2, I believe it's correct nonetheless, because n implies it's a single variable, whereas there are "two" n's here.

6. What is the space complexity of the provided code in `names.py`?

O(n), because it just reads out two lists.

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
