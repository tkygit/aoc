import string

def get_all_yes(group):
    num_people = group.count('\n') + 1
    num_yes = 0
    sorted_answers = group.replace('\n', '')
    for letter in string.ascii_lowercase:
        if sorted_answers.count(letter) == num_people:
            num_yes+=1
    return num_yes

def get_set(group):
    answers = group.replace('\n', '')
    return set(answers)

if __name__ == "__main__":

    with open("input.txt", "r") as f:
        file_input = f.read()
        groups = file_input.split("\n\n")

    yes_sum = 0
    all_yes_sum = 0

    for group in groups:
        yes_sum+=len(get_set(group))
        all_yes_sum+=get_all_yes(group)

    print(yes_sum)
    print(all_yes_sum)