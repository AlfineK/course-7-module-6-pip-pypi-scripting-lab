from datetime import datetime
import os
import sys
from typing import Any, Dict, List, Optional
import requests


def fetch_data(url: str = "https://jsonplaceholder.typicode.com/posts/1") -> Dict[str, Any]:
    """
    Fetches data from a public API endpoint using the requests package.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"[WARNING] Request failed: {err}")
        return {}


def generate_log(data: List[str]) -> str:
    """
    Validates log data, creates a timestamped file, and writes log entries.
    """
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    # STEP 2: Generate a filename with today's date (e.g., "log_20261020.txt")
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    print("--- Running Log Generation & API Automation ---")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Build initial activity log data
    log_data: List[str] = [
        f"[{timestamp}] User logged in",
        f"[{timestamp}] User updated profile"
    ]

    # Fetch remote API payload
    print("Fetching remote post data...")
    post = fetch_data()
    
    if post:
        title = post.get("title", "No title found")
        post_id = post.get("id", "N/A")
        print(f"Fetched Post Title: {title}")
        log_data.append(f"[{timestamp}] API Fetch Success - ID {post_id}: {title}")
    else:
        log_data.append(f"[{timestamp}] API Fetch Failed")

    log_data.append(f"[{timestamp}] Report exported")

    # Generate log file
    generate_log(log_data)
