# Problem Description:
Find words that match certain pattern:

- Pattern: 'abb'
- Possible Words: 'acc', 'qee'
- Not Possible Words: 'aca', 'bbb'

# Solutions:

## Naive
It is easy to think of construction of mapping betweeen pattern and words. 
Take 'abb' (pattern) and 'qcc' (word) as example: 'a'->'q', 'b'->'c'. 

2 mappings (HashMap or Dict) are constructed. ```word_dict``` maps character in word to pattern, 
such as ```word_dict['q'] = 'a'```, ```pat_dict['a']='q'```. Once we find / construct a mapping
, the rest characters in this word / pattern will be judge whether they satisfy the mapping.

However, I stuck here for quite a long time. Especially in the judgement. Here is 
the right way to think:

- If current characters in word / pattern exist in ```word_dict / pat_dict```. We directly judge it.
- Otherwise, we judge by: 
    - ```p in pat_dict and pat_dict[p] != w``` or 
    - ```w in word_dict and word_dict[w] != p```
    
### Advanced
Official solution provides a method that only use one dict: