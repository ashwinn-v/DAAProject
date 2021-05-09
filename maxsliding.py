import collections
def maxSlidingWindow(nums,k):
    
    # Constructing the Monotonic decreasing queue
    queue = collections.deque()
    for i in range(k-1):

        # When queue[-1] < nums[i], pop queue[-1] to maintain the  decreasing order
        while queue and queue[-1] < nums[i]:
            queue.pop()
        queue.append(nums[i])
    
    arr = []
    for i in range(k-1, len(nums)):
        # Add the new element of the window 
        while queue and queue[-1] < nums[i]:
            queue.pop()
        queue.append(nums[i])
        
        # Append the max value (queue[0]) to the arrult
        arr.append(queue[0])
        
        # Pop the old element of the window
        # Pop only when queue[0] == nums[i-k+1], since it may already be popped 
        if queue[0] == nums[i-k+1]:
            queue.popleft()
    
    return arr

nums = [1,3,-1,-3,5,3,6,7]
k = 3
val = maxSlidingWindow(nums,k)
print(val)
