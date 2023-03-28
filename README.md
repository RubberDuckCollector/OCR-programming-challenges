# OCR-programming-challenges
https://www.ocr.org.uk/Images/260930-coding-challenges-booklet.pdf

## Notes

### 5 - Fruit Machine

This had some if statements I needed to get my head around which took a long time, but overall it wasn't too bad with the exception of the money part. Figuring out when to subtract or add on money to the user's balance was difficult and I resorted to trial and error. The fruit machine had some very difficult sequence for my level when and how I completed it
* No Chat-GPT used, I solved this before it released

### 6 - Unit Converter

The unit converter wasn't too hard. I just had to make sure to keep my code reasonably modular by pre-defining functions that return the converted units so I could call them when the user is prompted for an input
* No Chat-GPT used

### 8 - Arithmetic Test

This was pretty easy. I wrote repetitive code but it doesn't really matter for me. I did extension 1 but not extension 2 because extension 2 was too hard for me
* No Chat-GPT used

### 9 - Happy Numbers

I figured out how to determine a happy number very quickly, and then got stuck trying to use a for loop to test many numbers to see if they're a happy number or not. That took me a very long time and I couldn't do it. All of my attempts were long winded and never going to work

• Chat-GPT used for this part of the code
```Python
def find_happy_numbers(b):
    happy_list = []
    count = 0

    while b not in happy_list and count < 50:
        happy_list.append(b)
        b = happy_numbers(b)
        count += 1
    return b == 1
```

### 39 - Sing along
This is very easy in python if you know the reversed for loop
* No Chat-GPT used, I solved this before it released
