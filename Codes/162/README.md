# Solution:

本题其实是在找"刚要下降"的那个点。

可以用二分的方法来找：有点类似不断倒逼mid点，使其往"上"走。如nums[mid] < nums[mid + 1], 则说明"刚要下降点"在右边，所以缩紧左边：left = mid + 1.
否则缩紧右边：right = mid