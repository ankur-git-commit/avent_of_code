# --- Day 2: Red-Nosed Reports ---

# --- (Part 1) ---
def safe_reports(report):
    monitor = []
    safe_count = 0
    for number_list in report:
        x, y = 0, 1
        prev_sign = None
        
        while y < len(number_list):
            diff = number_list[y] - number_list[x]
            current_sign = 1 if diff > 0 else -1

            if abs(diff) > 3 or diff == 0 or (prev_sign is not None and prev_sign != current_sign):
                monitor.append("unsafe")
                break

            prev_sign = current_sign
            x += 1
            y += 1

        if y == len(number_list):
            monitor.append("safe")
            safe_count += 1
    return monitor, safe_count

# --- Helper Function (Part 2) ---
def is_report_safe(report):
    """
    Checks if a given report is safe according to the rules from Part 1.
    - It must be consistently increasing or decreasing.
    - The difference between any two adjacent levels must be between 1 and 3.
    """
    if len(report) < 2:
        return True

    x, y = 0, 1
    prev_sign = None
    while y < len(report):
        diff = report[y] - report[x]

        current_sign = 1 if diff > 0 else -1

        if (
            abs(diff) > 3
            or diff == 0
            or (prev_sign is not None and prev_sign != current_sign)
        ):
            return False

        prev_sign = current_sign
        x += 1
        y += 1

    return True


# --- Main Solver Function (Part 2) ---
def count_safe_reports_with_dampener(data):
    """
    Calculates the total number of safe reports, considering the "Problem Dampener"
    rule from Part 2.
    """
    safe_count = 0
    for number_list in data:
        is_safe_overall = False

        # 1. Check if the report is already safe.
        if is_report_safe(number_list):
            is_safe_overall = True
        else:
            # 2. If not, try removing one level at a time.
            for i in range(len(number_list)):
                temp_list = number_list[:i] + number_list[i + 1 :]

                # 3. Check if the modified list is safe.
                if is_report_safe(temp_list):
                    is_safe_overall = True
                    break  # Found a safe version, no need to check further.

        if is_safe_overall:
            safe_count += 1

    return safe_count


# --- Data Loading Function ---
def extract_data_from_file(file_path):
    """
    Reads data from a text file, where each line contains space-separated numbers.
    """
    data = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                # Split the line by spaces and convert each part to an integer.
                if line.strip():  # Ensure the line is not empty
                    numbers = [int(x) for x in line.strip().split()]
                    data.append(numbers)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    return data


# --- Main Execution Block ---
if __name__ == "__main__":
    input_file_path = "paste.txt"

    # Load the data from the file.
    puzzle_data = extract_data_from_file(input_file_path)

    if puzzle_data is not None:
        # Calculate the answer for Part 1.
        safe_without_damper, safe_count = safe_reports(puzzle_data)
        # Calculate the answer for Part 2.
        final_safe_count = count_safe_reports_with_dampener(puzzle_data)

        # Print the final result.
        print(f"Total safe reports without the Dampener: {safe_count}")
        print(f"Total safe reports with the Problem Dampener: {final_safe_count}")
