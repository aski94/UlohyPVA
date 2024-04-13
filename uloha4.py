import math

def calculate_sum_subarrays(input_array):
    subarray_sums = []
    for i in range(len(input_array)):
        for j in range(i + 2, len(input_array) + 1):
            subarray_sums.append(sum(input_array[i:j]))
    
    unique_sums = tuple(set(subarray_sums))
    repeating_sums = [[num] * subarray_sums.count(num) for num in unique_sums if subarray_sums.count(num) > 1]
    
    result_count = 0
    for repeats in repeating_sums:
        result_count += len(repeats) * (len(repeats) - 1) // 2
    
    return result_count

inp = [1, 5, 2, 4, 2, 2, 2]
result = calculate_sum_subarrays(inp)
print(f"Výsledek: {result}")