def generate_seating_sequence(group1,group2,seats_p_row) :

    lenght_all = 4 * seats_p_row
    lenght_diff = len(group1) - len(group2)
    lenght_both = len(group1) + len(group2)
    lenght_add = lenght_all - (lenght_both + lenght_diff)

    group2 = group2 + ([" -"] * lenght_diff)

    result = ["-"] * (lenght_both + lenght_diff)
    result[::2] = group1
    result[1::2] = group2
    result = result + ([" -"] * lenght_add)

    return result

def group_reverse_order(group) :

    group = group[::-1]

    return group

def display_exam_seating(seating_sequence) :

    row_seat1 = seating_sequence[:(len(seating_sequence) // 4)]
    row_seat2 = seating_sequence[(len(seating_sequence) // 4):2 * (len(seating_sequence) // 4)]
    row_seat3 = seating_sequence[2 * (len(seating_sequence) // 4):3 * (len(seating_sequence) // 4)]
    row_seat4 = seating_sequence[3 * (len(seating_sequence) // 4):(len(seating_sequence))]

    row1 = "|" + "|".join(row_seat1) + "|"
    row2 = "|" + "|".join(row_seat2) + "|"
    row3 = "|" + "|".join(row_seat3) + "|"
    row4 = "|" + "|".join(row_seat4) + "|"

    row_lenght = len(row1)
    underline = "-" * row_lenght

    print(underline)
    print("|" + (" " * ((row_lenght - 11) // 2)) + "Exam Room" + (" " * ((row_lenght - 11) // 2))+ "|")
    print(underline)
    print(row1)
    print(underline)
    print(row2)
    print(underline)
    print(row3)
    print(underline)
    print(row4)
    print(underline)
    
  
def main() :
    
    group1 = input().split(",")
    group2 = input().split(",")
    seats_p_row = int(input())
    is_reverse = int(input())
    
    if is_reverse:
        group1 = group_reverse_order(group1)
        group2 = group_reverse_order(group2)
        
    if len(group1) > 2*seats_p_row or len(group2) > 2*seats_p_row:
        print("Room is too small. Get a bigger exam room!")
        return
    
    if seats_p_row < 4 or seats_p_row % 2 != 0:
        print("seats_p_row has to be more than 4 and has an even number.")
        return
    
    seating_sequence = generate_seating_sequence(group1,group2,seats_p_row)
    display_exam_seating(seating_sequence)

main()