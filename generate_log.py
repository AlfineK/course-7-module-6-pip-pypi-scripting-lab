from datetime import datetime
import os

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    # STEP 2: Generate a filename with today's date (e.g., "log_YYYYMMDD.txt")
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)