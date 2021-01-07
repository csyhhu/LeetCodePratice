def findKthBit(n: int, k: int):

    def recursion(_n:int, _k:int, sign_unchanged:bool=True):

        # print(_n, _k, sign_unchanged)

        if _n == 1:
            return "0" if sign_unchanged else "1"
        if _k == _n // 2 + 1:
            return "1" if sign_unchanged else "0"
        elif _k < _n // 2 + 1:
            return recursion(_n//2, _k, sign_unchanged)
        else:
            return recursion(_n//2, _n - _k + 1, not sign_unchanged)

    return recursion(2**n-1, k, True)


def generation(n, k):

    def inverse():
        pass

    path = '0'
    while n >= 0:
        path = path + '1' + path.reverse()



print(findKthBit(n = 4, k = 12))
print(findKthBit(3, 1))
print(findKthBit(n = 4, k = 11))
print(findKthBit(n = 1, k = 1))
print(findKthBit(n = 2, k = 3))