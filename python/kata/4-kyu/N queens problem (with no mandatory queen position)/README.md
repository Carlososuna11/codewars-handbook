# [Codewars N queens problem (with no mandatory queen position)](https://www.codewars.com/kata/52cdc1b015db27c484000031)

### Details
This is a classic needing (almost) no further introduction.

Given a N x N chess board, place N queens on it so none can attack another: I.e. no other queens can be found horizontally, vertically or diagonally to the current.

On the board below, no further queens can be positioned.
```
+-+-+
|Q| |
+-+-+
| | |
+-+-+
```

In this example a queen can be located in position a or position b - but not in both, thereby making (0,0) an invalid first position:
```
+-+-+-+
|Q| | |
+-+-+-+
| | |a|
+-+-+-+
| |b| |
+-+-+-+
```

Return value must by an array of N x-positions. That is, the y position is given by the index. For following board, expected answer is `[1, 3, 0, 2]`:

Only one solution per N is expected. If no solution can be found, return an empty array. That is, for a 1 x 1 board, the output is [0].

Input is a value positive number (N>0) and can be quite large, so try to make your solution efficient. See sample tests to check how large `N` can be.

Have fun :)