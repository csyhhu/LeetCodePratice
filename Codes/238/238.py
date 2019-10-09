def productExceptSelf(nums):
    # preorder = [1]
    # postorder = [1]
    #
    # for idx, value in enumerate(nums):
    #     if idx > 0:
    #         preorder.append(preorder[idx-1] * value)
    # for idx, value in enumerate(nums[::-1]):
    #     if idx > 0:
    #         postorder.insert(0, postorder[idx-1] * value)
    # print(preorder)
    # print(postorder)
    #
    # results = []
    # N = len(nums)
    # for idx, value in enumerate(nums):
    #     results.append(preorder[idx] * postorder[idx])
    # return results

    preorder = [1] #  pre[i]  = A[0] * A[1] * ... * A[i-1]
    postorder = [1] # post[i] = A[n-1] * A[n-2] * ... * A[i+1]
    N = len(nums)
    for idx in range(N):
        if idx > 0:
            preorder.append(preorder[idx-1] * nums[idx-1])
    for idx in range(N):
        if idx > 0:
            postorder.insert(0, postorder[0] * nums[N-idx])

    # print(preorder)
    # print(postorder)
    results = []
    for idx in range(N):
        results.append(preorder[idx] * postorder[idx])
    return results

inputs = [1,2,3,4]
outputs = productExceptSelf(inputs)
print(outputs)