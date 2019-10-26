def divisible_palindromes(max, divisor):
    """
    Function returns palindrome numbers within given range that are also divisible by provided number.
    :param max: upper limit of the range
    :param divisor: the number the returned palindrome numbers have to be divisible by
    :return: list of palindrome numbers
    """
    result = []
    if divisor > 0 and max >= divisor and max > 10:
        num = divisor
        while num <= max:
            if num > 10 and num % divisor == 0 and str(num) == str(num)[::-1]:
                result.append(num)
            num += divisor
    return result
