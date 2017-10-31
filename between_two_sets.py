#https://www.hackerrank.com/challenges/between-two-sets?h_r=next-challenge&h_v=zen

lenA, lenB = map(int, raw_input().split())
setA = map(int, raw_input().split())
setB = map(int, raw_input().split())


# Python with comprehension lists,
# for each number between max(setA) and min(setB),
# it will create a list that will hold boolean values,
# and 'all' checks that all the boolean values in a list are true.

maxA = max(setA)
minB = min(setB)
count = 0

for num in range(maxA, minB + 1):
    left = all([num % numA == 0 for numA in setA])
    right = all([numB % num == 0 for numB in setB])

    # True*True = 1
    # True*False = 0
    # False*False = 0
    count += left*right

print count