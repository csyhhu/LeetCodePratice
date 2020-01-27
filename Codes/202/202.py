def isHappy(n):
    def goNext(n):
        str_n = str(n)
        happy_n = 0
        for char in str_n:
            happy_n += (int(char)**2)
        return happy_n

    first = n
    second = goNext(n)
    while first != second:
        # print(first, second)
        first = goNext(first)
        second = goNext(goNext(second))
    if first == 1:
        return True
    else:
        return False

inputs = 19
print(isHappy(inputs))