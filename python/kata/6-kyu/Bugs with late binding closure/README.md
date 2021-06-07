# [Codewars Bugs with late binding closure](https://www.codewars.com/kata/60b775debec5c40055657733)

### Details
You have a function that takes an integer `n` and returns a list of length `n` of function objects that take an integer `x` and return `x` multiplied by the index of that object in this list(remember that in python the indexes of elements start from 0):

```
[f_0, f_1, ... f_n]
```

```
f_0 returns x * 0,
f_1 returns x * 1,
...
f_n returns x * n,
```

```python
def create_multiplications(n):
    return [lambda x : i * x for i in range(n)]
```

This code:

```python
for m in create_multiplications(3):
    print(m(3), ' ... ')
```

should output:
```python
>>> 0 ... 3 ... 6 ... 
```

But it outputs:

```python
>>> 6 ... 6 ... 6 ... 
```
You need to fix this bug.

### Input/Output
All inputs will be integers, output must be list of `function` objects.

**Good luck!**
Please rate this kata.
