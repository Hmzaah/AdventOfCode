# Function to simulate the evolution of stones
'''def simulate_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)

# Input and number of blinks
input_stones = [8435, 234, 928434, 14, 0, 7, 92446, 8992692]
blinks = 25

# Calculate and print the result
result = simulate_stones(input_stones, blinks)
print("Number of stones after", blinks, "blinks:", result)'''''


#part two

# Function to simulate the evolution of stones
def simulate_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)

# Input and number of blinks
input_stones = [8435, 234, 928434, 14, 0, 7, 92446, 8992692]
blinks = 75

# Calculate and print the result
result = simulate_stones(input_stones, blinks)
print("Number of stones after", blinks, "blinks:", result)