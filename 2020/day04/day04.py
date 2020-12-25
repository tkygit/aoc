import re

# This could be neater, if using the all() function in Python
# See Joel Grus' solution: https://github.com/joelgrus/advent2020/blob/master/advent2020/day04.py
def check_valid_passports(input_file):
    with open(input_file, "r") as f:
        passport_file = f.read()
        passports = passport_file.split("\n\n")
        valid_passports = len(passports)
        req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

        for passport in passports:
            pp_to_check = {}
            pairs = passport.split()
            for pair in pairs:
                key, value = pair.split(":")
                pp_to_check[key] = value
            
            valid_fields = True
            for req_field in req_fields:
                if req_field not in pp_to_check:
                    valid_passports-=1
                    valid_fields = False
                    break

            if valid_fields:
                for field in pp_to_check:
                    if pp_to_check[field] == "" and field != "cid":
                        valid_passports-=1
                        break

                    if field == "byr":
                        if int(pp_to_check[field]) < 1920 or int(pp_to_check[field]) > 2002:
                            valid_passports-=1
                            break

                    if field == "iyr":
                        if int(pp_to_check[field]) < 2010 or int(pp_to_check[field]) > 2020:
                            valid_passports-=1
                            break

                    if field == "eyr":
                        if int(pp_to_check[field]) < 2020 or int(pp_to_check[field]) > 2030:
                            valid_passports-=1
                            break

                    if field == "hgt":

                        if "cm" not in pp_to_check[field] and "in" not in pp_to_check[field]:
                            valid_passports-=1
                            break

                        regex = r"([0-9]*)"
                        match = re.search(regex, pp_to_check[field])
                        value = match.group(1)
                        if "cm" in pp_to_check[field]:
                            if int(value) < 150 or int(value) > 193:

                                valid_passports-=1
                                break
                        elif "in" in pp_to_check[field]:
                            if int(value) < 59 or int(value) > 76:

                                valid_passports-=1
                                break
                    
                    if field == "hcl":
                        if len(pp_to_check[field]) != 7:
                            valid_passports-=1
                            break                  

                        regex = r"#([0-9|a-f]){6}"
                        match = re.search(regex, pp_to_check[field])
                        if not match:
                            valid_passports-=1
                            break
                    
                    if field == "ecl":
                        eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

                        if pp_to_check[field] not in eye_colors:
                            valid_passports-=1
                            break
                    
                    if field == "pid":
                        if len(pp_to_check[field]) != 9:
                            valid_passports-=1
                            break

                        regex = r"[0-9]{9}"
                        match = re.search(regex, pp_to_check[field])
                        if not match:
                            valid_passports-=1
                            break
                
                
    return valid_passports
                
if __name__ == "__main__":
    # print(check_valid_passports("test_input.txt"))
    print(check_valid_passports("input.txt"))