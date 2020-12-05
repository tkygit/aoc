import re

def password_count_check(password, letter, min_occurence, max_occurence):
    count = password.count(letter)

    if count >= int(min_occurence) and count <= int(max_occurence):
        return True

def password_pos_check(password, letter, pos_1, pos_2):

    pos_count = 0

    if letter == password[int(pos_1) - 1]:
        pos_count+=1
    
    if letter == password[int(pos_2) - 1]:
        pos_count+=1

    if pos_count == 1:
        return True

def count_valid_pws(passwords):

    count_result = 0
    pos_result = 0

    for password in passwords:
        regex = r"([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)"
        match = re.search(regex, password)
        min_occurence = match.group(1)
        max_occurence = match.group(2)
        letter = match.group(3)
        pw = match.group(4)

        if password_count_check(pw, letter, min_occurence, max_occurence):
            count_result+=1
        
        if password_pos_check(pw, letter, min_occurence, max_occurence):
            pos_result+=1
    
    return {"count": count_result, "pos": pos_result}

if __name__ == "__main__":

    test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

    print(count_valid_pws(test_input))

    # open input file
    with open("input.txt", "r") as f:
        passwords = [line.strip() for line in f]
    
    print(count_valid_pws(passwords))