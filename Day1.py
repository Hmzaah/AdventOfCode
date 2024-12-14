from google.colab import files

uploaded = files.upload()

file_path = next(iter(uploaded))  # Get the name of the uploaded file


left_list = []
right_list = []

with open(file_path, 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)


left_list.sort()
right_list.sort()

total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

print("Total Distance:", total_distance)
