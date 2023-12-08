# Write your code here :-)
f = open('input.txt')
lines = f.readlines()
total = 0
nums = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight' , 'nine']
for line in lines:
    digits = []
    for i, chr in enumerate(line):
        if chr.isdigit():
            digits.append(chr)
        for j, num in enumerate(nums):
            if line[i:].startswith(num):
                digits.append(str(j+1))
    x = int(digits[0]+digits[-1])
    total += x
print(total)
