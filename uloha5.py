import math

def calculate_subarray_sums(input_array):
    distances = []
    pairs = []
    for i in range(len(input_array)):
        for j in range(i + 1, len(input_array)):
            pairs.append([input_array[i][2], input_array[j][2]])
            distances += (abs(input_array[i][0] - input_array[j][0]) ** 2 + abs(input_array[i][1] - input_array[j][1]) ** 2) ** 0.5,
    

    min_distance = min(distances)
    indices = [i for i, dist in enumerate(distances) if dist == min_distance]


    print(f"Minimum distance: {min_distance}")
    print("Pairs of planes with minimum distance:")
    for i in indices:
        print(pairs[i])


inp = [
    [0, 5, "Qantas"],
    [5, 0, "KLM"],
    [0, 0, "AirFrance"],
    [5, 5, "Lufthansa"],
    [2.5, 2.5, "KLM"]
]
calculate_subarray_sums(inp)