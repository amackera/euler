def even(n):
    return n / 2

def odd(n):
    return 3 * n + 1

def main(n):
    current = n
    chain = 1
    while (current != 1):
        if current % 2 == 0:
            current = even(current)
        else:
            current = odd(current)
        chain = chain + 1
    return chain

if __name__ == '__main__':
    current_num = 1
    current_max = 0
    for i in range(1, 1000000):
        chain_length = main(i)
        if chain_length > current_max:
            current_num = i
            current_max = chain_length
            print(current_num, current_max)

    print(current_num, current_max)
