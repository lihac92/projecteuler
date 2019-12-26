def sum_even_num(num):
    first_num = 1
    second_num = 2
    counter = 3
    sum_num = 0
    while counter < num:
        counter = first_num + second_num
        if counter >= num:
            break
        if counter % 2 == 0:
            sum_num = sum_num + counter
        first_num = second_num
        second_num = counter
    return sum_num

print(sum_even_num(4000000))
