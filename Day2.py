from google.colab import files

uploaded = files.upload()

file_path = next(iter(uploaded))  

reports = []
with open(file_path, 'r') as file:
    for line in file:
        
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

safe_reports_count = sum(1 for report in reports if is_safe_report(report))

print(f"Number of safe reports: {safe_reports_count}")


#PART TWO 

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
        modified_report = report[:i] + report[i+1:]  
        if is_safe_report(modified_report):
            return True
    return False


safe_reports_count = 0
for report in reports:
    if is_safe_report(report) or is_safe_by_removal(report):
        safe_reports_count += 1

print(f"Number of safe reports: {safe_reports_count}")
