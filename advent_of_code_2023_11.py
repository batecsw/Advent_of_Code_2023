# Write your code here :-)
f = open('input11.txt')
L = f.readlines()
Grid = [[c for c in row] for row in L]
ROWS = len(Grid)
COLS = len(Grid[0])

# search for empty rows and append another when found
EMPTY_ROW = []
row = 0
while row<ROWS:
  empty = True
  for col in range(COLS):
    if Grid[row][col] == '#':
      empty = False
  if empty:
    EMPTY_ROW.append(row)
  row += 1

# search for empty columns and append another when found
EMPTY_COL = []
col = 0
while col<COLS:
  empty = True
  for row in range(ROWS):
    if Grid[row][col]=='#':
      empty = False
  if empty:
    EMPTY_COL.append(col)
  col += 1

# Search for all "galaxies" and note their grid coordinates
GAL = []
for row in range(ROWS):
  for col in range(COLS):
    if Grid[row][col]=='#':
      GAL.append((row,col
      ))

# calaculate distance between each galaxy pair
# and for "part2" increase distance by 10exp6-1
for part2 in [False,True]:
  expansion_factor = 1
  if part2:
     expansion_factor = 10**6-1
  ans = 0
  for i,(row,col) in enumerate(GAL):
    for j in range(i,len(GAL)):
      row2,col2 = GAL[j]
      dij = abs(row2-row)+abs(col2-col)
      for er in EMPTY_ROW:
        if min(row,row2)<=er<=max(row,row2):
          dij += expansion_factor
      for ec in EMPTY_COL:
        if min(col,col2)<=ec<=max(col,col2):
          dij += expansion_factor
      ans += dij
  print(ans)
