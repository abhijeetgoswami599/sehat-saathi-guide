from collections import Counter
#Driver Code Ends

def topKFreq(arr, k):
    n = len(arr)

    mp = Counter(arr)

    # Store the elements of 'mp' in the list 'freq'
    freq = list(mp.items())

    # Sort the list 'freq' on the basis of the
    # 'compare' function
    freq.sort(key=lambda x: (x[1], x[0]), reverse=True)
    
    res = []
    
    # Extract and store the top k frequent elements
    for i in range(k):
        res.append(freq[i][0])
        
    return res

#Driver Code Starts
if __name__ == "__main__":
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    k = 2
    res = topKFreq(arr, k)
    
    for val in res:
        print(val, end=" ")

#Driver Code Ends
