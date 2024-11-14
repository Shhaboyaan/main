# Task 1
- import json
- with open('data.json', 'r') as f:
    - lst = json.load(f)
- div3 = [num for num in lst if num % 3 == 0]
- print(sum(div3) / len(div3))

# Task 2
- dict1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
- dict2 = {}
- for i in dict1.values():
-     dict2[i] = len(i)
- print(dict2)

# Task 3
- d = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
-for a,s in d.items():
-     d[a] = [i for i in s if i % 2 != 0]
- print(d)
