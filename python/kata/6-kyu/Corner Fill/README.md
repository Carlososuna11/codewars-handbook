# [Codewars Corner Fill](https://www.codewars.com/kata/60b7d7c82358010006c0cda5)

### Details
You receive a two dimensional array of size `n x n` and you want to fill in the square in one stroke while starting from `0:0` and ending on `n-1:0`.

If `n = 3` then:
```
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

Starting from left to right and then top to bottom we can grab the first corner! We then return on the inside of this corner to get the next one, and so on (see image below).

![image](https://files.gitter.im/55db43670fc9f982beae700d/koKc/corners.svg)

Resulting in the sequence `[1, 2, 3, 6, 9, 8, 5, 4, 7]`.

Another example:
```
# 4x4 (Mixed numbers)
[
  [4,  1, 10,  5],
  [7,  8,  2, 16],
  [15, 14, 3,  6],
  [11, 9, 13, 12]
]

#=> [4, 1, 10, 5, 16, 6, 12, 13, 3, 2, 8, 7, 15, 14, 9, 11]
```

#### Inputs
The input array can be of size `n=0`, in which case we want to return `[]`

