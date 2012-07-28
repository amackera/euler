# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_map():
    def multiple(num):
        if num % 3 == 0 or num % 5 == 0:
            return num
        else:
            return 0

    multiples = map(multiple, range(0, 1000))
    return sum(multiples)

def sum_filter():
    multiples = [int for int in range(0, 1000) if int % 3 == 0 or int % 5 == 0]
    return sum(multiples)

if __name__ == '__main__':
    print sum_map()
    print sum_filter()
