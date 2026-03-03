
def total_salary(path_to_salary_file):
    total = 0
    count = 0
    try:
        with open(path_to_salary_file, 'r') as file:
            lines_with_info = file.readlines()
    except:
        print("Error: File not found or invalid format.")
        return 0, 0
    for line in lines_with_info:
        result = line.split(",")
        removesufix = int(result[1].rstrip(","))
        total += removesufix
        count += 1
        return total, count
total, count = total_salary("salary.txt")
average = total / count if count > 0 else 0
result = (total, average)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


