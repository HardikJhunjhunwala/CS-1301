nums = [1, 2, -3, 4, -5, 6]
sum_positives = 0
for num in nums:
    if num < 0:
        continue
    sum_positives+= num

print(f'Sum of positive numbers {sum_positives}')
