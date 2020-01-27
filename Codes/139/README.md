# Solution

网上说解法是DP，但我觉得只是记录了搜索结果的穷举。

我一开始提出了一个idea, 穷举wordDict里面的组合，超时了。第二个idea, 将s穷举分块然后看有没有符合wordDict里面的，但是也超时了。
最后能过的解法跟第二个idea接近，只是记录下每次s分块是否在wordDict里面。