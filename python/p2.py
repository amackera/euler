# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

def fib_even_sum():
    def progress_sequence(prev1, prev2):
        return prev1 + prev2

    prev1 = 1
    prev2 = 1
    head = 1
    even_sum = 0
    while head <= 4000000:
        if head % 2 == 0:
            print '%s + %s' %(even_sum, head)
            even_sum = even_sum + head
        head = progress_sequence(prev1, prev2)
        prev1 = prev2
        prev2 = head

    return even_sum

if __name__ == '__main__':
    # EZPZ
    print fib_even_sum()
