# [Calculator](https://www.codewars.com/kata/5235c913397cbf2508000048/python)

### Details
Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression

Example:
```
Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
```

Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.

**Note**: python `[eval()](https://docs.python.org/3/library/functions.html#eval)`solves this problem but it is forbidden, when placing it, the code will throw an error and say that it cannot be used, just like the `[ast](https://docs.python.org/3/library/ast.html)` library