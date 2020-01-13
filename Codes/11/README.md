# Description
Given an array, find the maximum of ```(i-j) * min(a[i], a[j])```.

# Solution
当我们知道了```r_{i,j} = (i-j) * min(a[i], a[j])```的结果之后，有可能比```r_{i,j}```大的是```i+=1```或者```j-=1```，且新结果中```min(a[i], a[j])```要比之前的大。
所以我们比较```a[i]```和```a[j]```，小的那个往前/后移动一位。这是唯一可能比之前结果还要大的可能性。