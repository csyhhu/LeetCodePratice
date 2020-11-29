# Description

Find the top K frequent elements

# Solution

- Quicksort: o(nlog(n)), o(n)
- Minheap sort: (o(nlog(k))), o(n)
- Bucket sort: o(n), o(n)

本题本质上都需要记录所有数的频率，然后或是频率进行排序：快排、堆排、桶排。