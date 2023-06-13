def is_prime(n):

    if n < 2:
        return False
    else:
        # it's (2, n) because we want to test from 2 to n-1
        # this will mean that anything n is divisble by won't be 1 or itself
        for i in range(2, n):
            # if n is divisible by i then it cannot be prime
            # because prime numbers can only be divisible by 1 and themselves
            # the for loop does not touch on 1 or n
            if n % i == 0:
                return False

        return True

def product_of_list(l):
    total = 1

    for i in range(len(l)):
        total *= l[i]

    return total

def prime_factors(n):

    prime_factors = []
    i = 2

    while i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    return prime_factors

    # prime_factors_list = []

    # # get all nums between 2 and n-1 inclusive
    # nums_less_than_n = [i for i in range(2, n)]

    # # test for the primes
    # # this list contains every prime within 2 and n-1 inclusive
    # primes_less_than_n = [i for i in range(len(nums_less_than_n)) if is_prime(i)]
    # print(f"primes_less_than_n: {primes_less_than_n}")

    # product = 1
    # i = 0
    # found = False # not found the prime factors

    # while found is False:
    #     break
    

    # try smallest prime
    # check if this is equal to n
    # if yes then done
    
    # else
    # make a copy.deepcopy() of the current prime factors list
    # if 2 != n, append the next biggest prime that's divisible (this should be 3 because the primes will be ordered)
    # check if the product == n
    # repeat while product is less than n
    # if product is more than n:
    #     remove largest prime in use, replace with next prime smaller than that
    #     try again until prime factors are in prime_factors_list




    # try the smallest divisible prime

    # if the product of it doesn't equal n
    # then try the product of the same number squared, if not, try adding the next biggest prime
    # if THAT one is divisble then append it
    # check the product == n
    # repeat

    # USE BACKTRACKING
    # maybe copies of a variable (product?????????????????? then choose a different prime)
    # maybe select primes until the product is larger than n
    # then use another one of the smallest prime instead one largest prime

    # for i in range(len(primes_less_than_n)):
    #     if n % primes_less_than_n[i] == 0:
    #         prime_factors_list.append(primes_less_than_n[i])
    #         print(f"prime_factors_list: {prime_factors_list}")

    #         if product_of_list(prime_factors_list) == n:
    #             return prime_factors_list
    #         else:

    # return prime_factors_list
    # return primes_less_than_n
    # return nums_less_than_n

print(prime_factors(20))
print(prime_factors(40))

# TODO: NOT ENOUGH NUMBERS ARE BEING APPENDED INTO prime_factors_list
# TODO: BUT THEY ARE THE CORRECT ONES (prime factors of 20 are 5, 2, 2 OR 5 * 2 squared)
# TODO: IN prime_factors_list YOU NEED TO TAKE THE PRODUCT OF THE WHOLE LIST ON EACH ITERATION AND COMPARE IT TO N

# print(is_prime(5))
# print(is_prime(7))
# print(is_prime(9))
# print(is_prime(11))
# print(is_prime(13))

# even_number = [i for i in range(1000)]


# for i in range(len(even_number)):
#     print(f"{even_number[i]}: {is_prime(even_number[i])}")

