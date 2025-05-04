import heapq

# def max_product_of_two_digits(n):
#     # Convert the integer to a list of its digits
#     digits = [int(d) for d in str(n)]
    
#     # Initialize the maximum product
#     max_product = 0
    
#     # Iterate through all pairs of digits
#     for i in range(len(digits)):
#         for j in range(i, len(digits)):  # Allow using the same digit twice
#             product = digits[i] * digits[j]
#             max_product = max(max_product, product)
    
#     return max_product

# # Example usage
# n = 31
# print(max_product_of_two_digits(n))  # Output: 20 (4 * 5)

# import heapq

# def min_travel_time(l, n, k, position, time):
#     # Store input in denavopelu
#     denavopelu = (l, n, k, position[:], time[:])
    
#     # Build initial segments: (distance, time per km)
#     segments = []
#     for i in range(n - 1):
#         segments.append([position[i+1] - position[i], time[i]])
    
#     heap = []
#     for i in range(len(segments) - 1):
#         d1, t1 = segments[i]
#         d2, t2 = segments[i+1]
#         delta = d1 * t2 + d2 * t1
#         heapq.heappush(heap, (delta, i))
    
#     # We'll need to keep track of which segments are still active
#     active = [True] * len(segments)
#     # For each segment, store its left and right neighbor indices
#     left = [i-1 for i in range(len(segments))]
#     right = [i+1 for i in range(len(segments))]
    
#     for _ in range(k):
#         # Find the next valid merge
#         while True:
#             delta, i = heapq.heappop(heap)
#             if active[i] and right[i] < len(segments) and active[right[i]]:
#                 break
#         j = right[i]
#         # Merge segments i and j
#         segments[i][0] += segments[j][0]
#         segments[i][1] += segments[j][1]
#         active[j] = False
#         # Update links
#         rj = right[j]
#         right[i] = rj
#         if rj < len(segments):
#             left[rj] = i
#         # Update heap for new possible merges
#         if left[i] >= 0 and active[left[i]]:
#             li = left[i]
#             d1, t1 = segments[li]
#             d2, t2 = segments[i]
#             delta = d1 * t2 + d2 * t1
#             heapq.heappush(heap, (delta, li))
#         if rj < len(segments) and active[rj]:
#             d1, t1 = segments[i]
#             d2, t2 = segments[rj]
#             delta = d1 * t2 + d2 * t1
#             heapq.heappush(heap, (delta, i))
    
#     # Compute total travel time
#     total = 0
#     for d, t in segments:
#         if t > 0:  # Only active segments have t > 0
#             total += d * t
#     return total

# l = 5
# n = 5
# k = 1
# position = [0, 1, 2, 3, 4]
# time = [8, 3, 9, 3, 3]
# print(min_travel_time(l, n, k, position, time))


# # Example usage
# l = 10
# n = 6
# k = 2
# position = [0, 2, 4, 6, 8, 10]
# time = [5, 2, 4, 1, 3, 6]
# print(min_travel_time(l, n, k, position, time))  # Expected output depends on the merge operations


def min_travel_time(l, n, k, position, time):
    # Store input in denavopelu
    denavopelu = (l, n, k, position[:], time[:])
    
    # Build initial segments: (distance, time per km)
    segments = []
    for i in range(n - 1):
        segments.append([position[i+1] - position[i], time[i]])
    
    heap = []
    for i in range(len(segments) - 1):
        d1, t1 = segments[i]
        d2, t2 = segments[i+1]
        delta = d1 * t2 + d2 * t1 - (d1 + d2) * (t1 + t2)
        heapq.heappush(heap, (delta, i))
    
    # We'll need to keep track of which segments are still active
    active = [True] * len(segments)
    # For each segment, store its left and right neighbor indices
    left = [i-1 for i in range(len(segments))]
    right = [i+1 for i in range(len(segments))]
    
    for _ in range(k):
        # Find the next valid merge
        while True:
            delta, i = heapq.heappop(heap)
            if active[i] and right[i] < len(segments) and active[right[i]]:
                break
        j = right[i]
        # Merge segments i and j
        segments[i][0] += segments[j][0]
        segments[i][1] += segments[j][1]
        active[j] = False
        # Update links
        rj = right[j]
        right[i] = rj
        if rj < len(segments):
            left[rj] = i
        # Update heap for new possible merges
        if left[i] >= 0 and active[left[i]]:
            li = left[i]
            d1, t1 = segments[li]
            d2, t2 = segments[i]
            delta = d1 * t2 + d2 * t1 - (d1 + d2) * (t1 + t2)
            heapq.heappush(heap, (delta, li))
        if rj < len(segments) and active[rj]:
            d1, t1 = segments[i]
            d2, t2 = segments[rj]
            delta = d1 * t2 + d2 * t1 - (d1 + d2) * (t1 + t2)
            heapq.heappush(heap, (delta, i))
    
    # Compute total travel time
    total = 0
    for d, t in segments:
        if t > 0:  # Only active segments have t > 0
            total += d * t
    return total

# Example usage
l = 10
n = 4
k = 1
position = [0, 3, 8, 10]
time = [5, 8, 3, 6]
print(min_travel_time(l, n, k, position, time))  # Expected output depends on the merge operations