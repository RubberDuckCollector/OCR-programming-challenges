# OCR-programming-challenges
https://www.ocr.org.uk/Images/260930-coding-challenges-booklet.pdf

## Challenges completed:

* 5 - Fruit Machine
* 6 - Unit Converter
* 8 - Arithmetic Test
* 9 - Happy Numbers
* 12 - Quiz Maker
* 15 - Pangrams
* 20 - Palindromes
* 22 - Simple Life Calculator
* 23 - Fibbing
* 24 - Hack Proof
* 25 - Ordering
* 30 - Year Addition
* 33 - Mor-se Coding
* 36 - Triangulate (Not finished extension, WIP)
* 37 - Fizz Buzz
* 39 - Sing Along

## Notes

### 5 - Fruit Machine

This had some if statements I needed to get my head around which took a long time, but overall it wasn't too bad with the exception of the money part. Figuring out when to subtract or add on money to the user's balance was difficult and I resorted to trial and error. The fruit machine had some very difficult sequence for my level when and how I completed it

### 6 - Unit Converter

The unit converter wasn't too hard. I just had to make sure to keep my code reasonably modular by pre-defining functions that return the converted units so I could call them when the user is prompted for an input

### 8 - Arithmetic Test

This was pretty easy. I wrote repetitive code but it doesn't really matter for me. I did extension 1 but not extension 2 because extension 2 was too hard for me

### 9 - Happy Numbers

I figured out how to determine a happy number very quickly, and then got stuck trying to use a for loop to test many numbers to see if they're a happy number or not. That took me a very long time and I couldn't do it. All of my attempts were long winded and never going to work

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

### 12 - Quiz Maker

This was easy for me. The only tricky parts are reading the questions and answers from the file in the correct way (as sublists in a bigger list) and correctly processing each element in the sublists with the list comprehension

### 15 - Pangrams

This was quite easy for me because brute forcing it is easy.

### 20 - Palindromes

Palindromes in Python are very easy. There are 2 shorthand techniques where:
```Python
message = message[::-1] # reverses the string

return msg[::-1] == msg # this will return either True or False due to the "=="
```

### 22 - Simple Life Calculator

easy

### 23 - Fibbing

This was pretty easy for me. I remmebered the recursive solustion to the fibonacci sequence so I used that and the rest was knowledge of for loops and the builtin `reversed` and `sum` keywords

### 24 - Hack Proof

Pretty easy

### 25 - Ordering

This wasn't hard other than `msg = "".join([i for i in msg])` which converts the list into a string while joining each element with the data in quotes

### 30 - Year Addition

Easy

### 33 - Mor-se Coding

Challenge 33 was definitely hard. I found decoding morse code to be much harder than encoding. This was a fun challenge and it's one of the more practical ones I've tried.

### 36 - Triangulate (WIP)

I used the internet to learn about the triangle inequality theorem so I could complete the non-extension part of the challenge. I then re-learned the sine rule to help me figure out how to do the extension, but coming up with solutions confused me so I left the extension for later

### 37 - Fizz Buzz
Easy

### 39 - Sing along

This is very easy in python if you know the reversed for loop
