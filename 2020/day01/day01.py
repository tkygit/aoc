
RESULT=2020

# O(N^2) solution
def brute_find_multiple(nums):
    for x in nums:
        for y in nums:
            if x + y == RESULT:
                return x * y

# O(N^3) solution
def brute_find_three_multiple(nums):
    for x in nums:
        for y in nums:
            for z in nums:
                if x + y + z == RESULT:
                    return x * y * z

# More efficient O(N) solution from Joel Grus (https://github.com/joelgrus/advent2020)
def find_multiple(nums):
    complements = [RESULT - x for x in nums]

    for y in nums:
        if y in complements:
            return y * (2020 - y)

# More efficient O(N^2) solution from Joel Grus (https://github.com/joelgrus/advent2020)
def find_three_multiples(nums):

    complements = {}

    for x in nums:
        for y in nums:
            complements[RESULT - x - y] = (x, y)
    
    for x in nums:
        if x in complements:
            y, z = complements[x]
            return x * y * z
            

if __name__ == "__main__":

    test_input = [1721, 979, 366, 299, 675, 1456]
    print(brute_find_multiple(test_input))
    print(brute_find_three_multiple(test_input))
    # print(find_multiple(test_input))
    # print(find_three_multiples(test_input))

    # open input file
    with open("input.txt", "r") as f:
        nums = [int(line.strip()) for line in f]

    print(brute_find_multiple(nums))
    print(brute_find_three_multiple(nums))
    # print(find_multiple(nums))
    # print(find_three_multiples(nums))
    
