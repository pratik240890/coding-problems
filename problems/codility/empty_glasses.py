# There are N empty glasses with a capacity of 1,2,…,N liters(there is exactly one glass of each unique capacity)
# You want to pour exactly K liters of water into glasses.
# Each glass may be either full or empty(a glass cannot be partially filled).
# What is the minimum number of glasses that you need to contain K liters of water?

# Example1
#      Given N=5, K=8, should return 2.You can use 2 glasses with capacity 3,5 to hold 8 liters of water
# Example2
#      Given N=4, K=10, should return 4. (1,2,3,4)
# Example3
#      Given N=1, K=2, should return -1.
# Example4
#      Given N=10, K=5, should return 1. (5)


# Solution with greedy algorithm


def solution(N, K):
    if N < 1 or N > 1000000:
        raise ValueError("Invalid glass number")
    
    if K < 1 or K > 1000000000:
        raise ValueError("Invalid number for liters")

    if N >= K:
        return 1

    sum_n = N*(N+1)/2
    if sum_n < K:
        return -1
    else:
        water = N
        max_capacity = K
        used_glasses = set()
        while max_capacity > 0:
            to_fill = min(water, max_capacity)
            i = to_fill
            while i > 0:
                if i not in used_glasses:
                    used_glasses.add(i)
                    max_capacity = max_capacity - i
                    break
                i = i - 1
        print(used_glasses)
        return len(used_glasses)

if __name__ == "__main__":
    total = solution(4,10)
    print("Number of glasses required = ", total)