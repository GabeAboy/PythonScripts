input_amount = int(raw_input())
second_last = input_amount - 2

input_list = map(int, raw_input().strip().split(" "))
input_list.sort()

print input_list[second_last]
    
