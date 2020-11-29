def topKFrequent_quicksort(nums, k):
    num_freq = {}
    for num in nums:
        if num not in num_freq:
            num_freq[num] = 1
        else:
            num_freq[num] += 1

    sorted_num_freq = sorted(num_freq.items(), key=lambda kv: kv[1])
    sorted_num_freq.reverse()

    results = []
    for i in range(k):
        results.append(sorted_num_freq[i][0])

    return results


def topKFrequent_heap(nums, k):

    num_freq = {}
    for num in nums:
        if num not in num_freq:
            num_freq[num] = 1
        else:
            num_freq[num] += 1

    import heapq
    min_heaq = list()
    for num, freq in num_freq.items():
        if len(min_heaq) < k:
            heapq.heappush(min_heaq, (freq, num))
        else:
            if freq > min_heaq[0][0]:
                heapq.heapreplace(min_heaq, (freq, num)) # More efficient than pop and push according to the document.

    results = []
    for freq, num in min_heaq:
        results.append(num)
    return results


def topKFrequent(nums, k):
    num_freq = {}
    # max_freq = 0
    min_freq = 10000
    for num in nums:
        if num not in num_freq:
            num_freq[num] = 1
        else:
            num_freq[num] += 1
        # if num_freq[num] > max_freq:
        #     max_freq = num_freq[num]
        if num_freq[num] < min_freq:
            min_freq = num_freq[num]

    # Bucket sort
    # Put all numbers (with same frequency) in one bucket
    bucket = [[] for _ in range(len(nums))]
    for num, freq in num_freq.items():
        bucket[freq - min_freq].append(num) # [1:[5,6], 2:[3,4], 4:[1]]: Number 5&6 appear one time, 3&4 for two times and 1 for 4 times.

    results = []
    # Gather results from high frequency to low, thus we reverse the bucket
    for num_list in bucket[::-1]:
        if len(num_list) != 0:
            for num in num_list:
                results.append(num)
        # The above append can be replaced more efficiently as:
        # if len(num_list) != 0:
        #     results.extend(num)
        # Since extend accept list as input
        if len(results) >= k:
            break
    return results


# nums = [1,1,1,2,2,3]
# k = 2
# nums = [3,0,1,0]
# k = 1
nums = [4,1,-1,2,-1,2,3]
k = 2
print(topKFrequent(nums, k))
