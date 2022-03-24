# FUNCTIONS
def max_num(*args):
    return max(args)

def mult_list(*args):
    product = 1
    for num in args:
        product *= num
    return product

def rev_string(string):
    ret = list(string)
    ret.reverse()
    return ''.join(ret)

def fib(n):
    if(n <= 1):
        return n
    else: 
        return fib(n - 1) + fib(n - 2)

def num_within(num, begin, end):
    return num >= begin and num <= end

def pascal(n):
    if n == 1:
        return [[1]]
    else:
        triangle = pascal(n - 1)
        current = [1]
        previous = triangle[-1]
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        current += [1]
        triangle.append(current)
        return triangle

# TESTS
print(max_num(34, 63, 111))
print(mult_list(3, 4, 5, 2))
print(rev_string('bananas'))
print(fib(10))
print(num_within(10, 2, 5))
for row in pascal(5):
    print(*row)