import sys
input = lambda: sys.stdin.readline().rstrip()  # Remove the newline character at the end of the line
II = lambda: int(input())
lii = lambda: list(map(int, input().split()))

# function to find the number of subarrays with sum = X
def solve(arr, X, N):
    # Dictionary to store the frequency of prefix sums
    pref_sums = {0: 1}
    pref = 0
    cnt = 0
    
    # Calculate the prefix sum at every index, and find the
    # count of subarrays with sum = pref - X
    for i in range(N):
        pref += arr[i]
        cnt += pref_sums.get(pref - X, 0)
        pref_sums[pref] = pref_sums.get(pref, 0) + 1
    
    return cnt
  
# Driver code  

if __name__ == "__main__":

    nx = lii()
    n = nx[0]
    x = nx[1]
    arr = lii()

    print(solve(arr, x, n))