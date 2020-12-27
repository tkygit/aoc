TOTAL_ROWS=127
TOTAL_COLUMNS=7
MULTIPLIER=8

def binary_search(string, index, low, high, search_type):
    
    mid = (high + low) // 2
    N = len(string)

    if search_type == "row":
        first_half_marker = "F"
        second_half_marker = "B"
    else:
        first_half_marker = "L"
        second_half_marker = "R"

    if string[index] == first_half_marker:
        # print(f"upper half: {string[index]} at index: {index}; new low: {low}, new high: {mid}")
        if index == N - 1:
            return low
        else:
            return binary_search(string, index + 1, low, mid, search_type)
    elif string[index] == second_half_marker:
        # print(f"lower half: {string[index]} at index: {index}; new low: {mid + 1}, new high: {high}")
        if index == N - 1:
            return high
        else:
            return binary_search(string, index + 1, mid + 1, high, search_type)
    else:
        raise Exception(f"Invalid character: {string[index]} in string")

def get_seat_id(row_string, col_string):
    # print(f"Row String {row_string} and Column String {col_string}")

    row_res = binary_search(row_string, 0, 0, TOTAL_ROWS, 'row')
    col_res = binary_search(col_string, 0, 0, TOTAL_COLUMNS, 'col')

    # print(f"Row Result: {row_res}")
    # print(f"Col Result: {col_res}")

    return row_res * MULTIPLIER + col_res

def get_my_seat_id(array, low):
    curr = low
    for char in array:
        if char != curr:
            return curr
        else:
            curr+=1

def get_req_seat_ids(array):
    seat_ids = []
    for string in array:
        seat_ids.append(get_seat_id(string[:7], string[7:]))

    sorted_seats = sorted(seat_ids)

    return {
        "max_seat_id": max(seat_ids),
        "my_seat_id": get_my_seat_id(sorted_seats, sorted_seats[0])
    }

if __name__ == "__main__":

    test_input = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    print(get_req_seat_ids(test_input))

    with open("input.txt") as f:
        lines = [line.strip() for line in f]
    print(get_req_seat_ids(lines))