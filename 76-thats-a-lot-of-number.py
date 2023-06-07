with open("/Users/alfielong/programming/ocr-challenges/76-thats-a-lot-of-number/nums.txt", "r") as f:
    nums = [int(i) for i in f]

nums = sum(nums)

nums = str(nums)

print(nums[:10])
