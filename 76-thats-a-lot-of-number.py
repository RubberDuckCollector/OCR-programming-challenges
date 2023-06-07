with open("76-thats-a-lot-of-number.txt", "r") as f:
    nums = [int(i) for i in f]

nums = sum(nums)

nums = str(nums)

print(nums[:10])
