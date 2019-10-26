def divisible_palindromes(max, divisor):
    result = []
    if divisor > 0 and max >= divisor and max > 10:
        num = divisor
        while num <= max:
            if num > 10 and num % divisor == 0 and str(num) == str(num)[::-1]:
                result.append(num)
            num += divisor
    return result
