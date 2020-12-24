import math

RIGHT=3
DOWN=1

def count_trees(input_file, right, down):
  with open (input_file, "r") as f:
    lines = [line.strip() for line in f]
    x = right
    num_trees = 0
    for y in range(down, len(lines), down):
      multiply = math.ceil((len(lines) * right)/len(lines[y]))
      extend = lines[y]*multiply
      if extend[x] == "#":
        num_trees+=1
      x+=right
  return num_trees

if __name__ == "__main__":

  print(count_trees("test_input.txt", 3, 1))
  print(count_trees("input.txt", 3, 1))

  # This is really ugly code ...
  # print(count_trees("test_input.txt", 1, 1) * count_trees("test_input.txt", 3, 1) * count_trees("test_input.txt", 5, 1) * count_trees("test_input.txt", 7, 1) * count_trees("test_input.txt", 1, 2))
  # print(count_trees("input.txt", 1, 1) * count_trees("input.txt", 3, 1) * count_trees("input.txt", 5, 1) * count_trees("input.txt", 7, 1) * count_trees("input.txt", 1, 2))

  # Make the above more readable (based on Joel Grus' solution: https://github.com/joelgrus/advent2020/blob/master/advent2020/day03.py)
  slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
  test_input_product = 1
  product = 1

  for x,y in slopes:
    test_input_product *= count_trees("test_input.txt",x,y)
    product *= count_trees("input.txt",x,y)
  
  print(f"Test input product:{test_input_product}")
  print(f"Input product:{product}")
