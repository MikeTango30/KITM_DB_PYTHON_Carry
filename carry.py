def carry(a, b):
    count = 0
    temp = 0
    digit_count = max((len(str(a))), (len(str(b))))
    for i in range(digit_count):
        last_a = a % 10
        last_b = b % 10
        if last_a + last_b + temp >= 10:
            temp = 1
            count += 1
        a //= 10
        b //= 10

    return count


carry_count = carry(190101, 909909)
print(carry_count)
