

nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]

iterator = iter(nums)
total = 0
while True:
    try:
        num = next(iterator)
        if num % 2 == 0:
            total += num
    except StopIteration:
        break

print("Juft sonlar yig'indisi:", total)


