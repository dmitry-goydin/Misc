def divisible_palindrome(max, divisor):
    result = 0
    num = max - 1
    while num > 10:
        if num % divisor == 0 and str(num) == str(num)[::-1]:
            result = num
            break
        num -= 1
    return result

def divisible_palindromes(max, divisor):
    result = []
    num = max - 1
    while num > 10:
        if num % divisor == 0 and str(num) == str(num)[::-1]:
            result.append(num)
        num -= 1
    return result
