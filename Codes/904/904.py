def totalFruit_wrong(tree):
    max_amount = 0
    basket = {}
    end = 1
    first = tree[0]
    second = tree[end]
    """
    prev_first = first
    basket[first] = 1
    while end < len(tree):
        print(basket, first, second)
        if second in basket:
            basket[second] += 1
        else:
            if len(basket) <= 1:
                basket[second] = 1
            else:
                basket.pop(prev_first)
                basket[second] = 1
        end += 1

        prev_first = first
        first = second
        second = tree[end] if end < len(tree) else None
    """
    basket[first] = 1
    while end < len(tree):
        print(basket, first, second)
        if tree[end] in basket:
            basket[tree[end]] += 1
            first = second
            second = tree[end]
        else:
            if len(basket) <= 1:
                basket[tree[end]] = 1
            else:
                # Change the first and pop, put
                basket.pop(first)
                first = second
                second = tree[end]
                basket[tree[end]] = 1
        end += 1

        if max_amount < sum(basket.values()):
            max_amount = sum(basket.values())
    return max_amount


def totalFruit_wrong2(tree):
    max_amount = 0
    basket = {}
    head_element = tree[0]
    end = 1
    while end < len(tree):
        print(basket, head_element)

        if tree[end] in basket:
            basket[tree[end]] += 1
        else:
            if len(basket) <= 1:
                basket[tree[end]] = 1
            else:
                basket.pop(head_element)
                head_element = list(basket.keys())[0]
                basket[tree[end]] = 1

        end += 1
        if tree[end] != head_element:
            head_element = tree[end]

        if max_amount < sum(basket.values()):
            max_amount = sum(basket.values())
    return max_amount


def totalFruit(tree):
    max_amount = 0
    basket = {}
    left = 0
    right = 0
    while right < len(tree):

        if tree[right] not in basket:
            basket[tree[right]] = 1
        else:
            basket[tree[right]] += 1
        while (len(basket)) > 2:
            basket[tree[left]] -= 1
            if basket[tree[left]] == 0:
                basket.pop(tree[left])
            left += 1
        right += 1

        max_amount = max(max_amount, sum(basket.values()))
    return max_amount


inputs = [3,3,3,1,2,1,1,2,3,3,4]
print(totalFruit(inputs))
inputs = [1,2,3,2,2]
print(totalFruit(inputs))
inputs = [0,1,2,2]
print(totalFruit(inputs))
inputs = [1,0,1,4,1,4,1,2,3]
print(totalFruit(inputs))