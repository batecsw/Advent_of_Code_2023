# Write your code here :-)
import sys
import re
from collections import defaultdict

f = open('input3.txt')
lines = f.readlines()

GRID = [[col for col in line] for line in lines]
ROWS = len(GRID)
COLS = len(GRID[0])

total = 0
nums = defaultdict(list)
for row in range(ROWS):
  gears = set() # positions of '*' characters next to the current number
  num = 0
  has_part = False
  for col in range(COLS+1):
    if col < COLS and GRID[row][col].isdigit():
      num = num*10+int(GRID[row][col])
      for rr in [-1,0,1]:
        for cc in [-1,0,1]:
          if 0<=row+rr<ROWS and 0<=col+cc<COLS:
            ch = GRID[row+rr][col+cc]
            if not ch.isdigit() and ch != '.':
              has_part = True
            if ch=='*':
              gears.add((row+rr, col+cc))
    elif num>0:
      for gear in gears:
        nums[gear].append(num)
      if has_part:
        total += num
      num = 0
      has_part = False
      gears = set()

print(total)
p2 = 0
for k,v in nums.items():
  if len(v)==2:
    p2 += v[0]*v[1]
print(p2)
