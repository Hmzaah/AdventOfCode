from google.colab import files


uploaded = files.upload()

file_path = next(iter(uploaded))  

reports = []
with open(file_path, 'r') as file:
    for line in file:
        # Convert each report into a list of integers
        reports.append(list(map(int, line.split())))

def is_safe_report(report):
    is_increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
    is_decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))

    if not is_increasing and not is_decreasing:
        return False

    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff < 1 or diff > 3:
            return False

    return True

def is_safe_by_removal(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove the element at index i
        if is_safe_report(modified_report):
            return True
    return False

safe_reports_count = 0
for report in reports:
    if is_safe_report(report) or is_safe_by_removal(report):
        safe_reports_count += 1

print(f"Number of safe reports: {safe_reports_count}")

#PART TWO

import re
from google.colab import files

uploaded = files.upload()

file_path = next(iter(uploaded))

with open(file_path, 'r') as file:
    corrupted_memory = file.read()

mul_pattern = r"mul\((?P<X>\d{1,3}),(?P<Y>\d{1,3})\)"  # Valid mul instructions
do_pattern = r"do\(\)"  # do() instruction
dont_pattern = r"don't\(\)"  # don't() instruction

# Combine all patterns into one with distinct names
combined_pattern = f"(?P<mul>{mul_pattern})|(?P<do>{do_pattern})|(?P<dont>{dont_pattern})"

matches = re.finditer(combined_pattern, corrupted_memory)

enabled = True  # Multiplications are enabled at the start
total_sum = 0

for match in matches:
    if match.group('do'):  # Check for do() instruction
        enabled = True
    elif match.group('dont'):  # Check for don't() instruction
        enabled = False
    elif match.group('mul') and enabled:  # Process mul(X, Y) if enabled
        x, y = int(match.group('X')), int(match.group('Y'))  # Extract numbers
        total_sum += x * y

print("Total Sum of Enabled Multiplications:", total_sum)