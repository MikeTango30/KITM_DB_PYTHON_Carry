def carry(a, b):
    count = 0
    temp = 0
    digit_count = max((len(str(a))), (len(str(b))))
    for i in range(digit_count):
        if a % 10 + b % 10 + temp >= 10:
            temp = 1
            count += 1
            a //= 10
            b //= 10
        else:
            break

    return count


carry_count = carry(9, 999989999)
print(carry_count)