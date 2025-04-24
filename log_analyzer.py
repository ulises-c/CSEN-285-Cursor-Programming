"""
Web App Log Analyzer

Problem Requirements:
1. Parses the logs.
2. Finds the first user who received 2 or more consecutive 500 errors.
3. Returns the user ID and the list of timestamps for those 500 errors.
"""

from dataclasses import dataclass
from typing import List, Optional, Dict
from datetime import datetime


@dataclass
class LogEntry:
    """Represents a single log entry with timestamp, user ID, and status code."""
    timestamp: datetime
    user_id: str
    status_code: int


@dataclass
class ErrorResult:
    """Represents the result of finding consecutive 500 errors."""
    user_id: str
    error_timestamps: List[str]


def parse_log_line(line: str) -> LogEntry:
    """
    Parse a log line into a LogEntry object.

    Args:
        line: String in format "YYYY-MM-DDThh:mm:ssZ userId statusCode"

    Returns:
        LogEntry object with parsed data
    """
    parts = line.split()
    if len(parts) != 3:
        raise ValueError(f"Invalid log line format: {line}")

    timestamp_str, user_id, status_code_str = parts
    try:
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
        status_code = int(status_code_str)
    except ValueError as e:
        raise ValueError(
            f"Invalid timestamp or status code format: {line}") from e

    return LogEntry(timestamp, user_id, status_code)


def find_consecutive_errors(log_lines: List[str]) -> Optional[ErrorResult]:
    """
    Find the first user who experienced two or more consecutive HTTP 500 errors.

    Args:
        log_lines: List of log entries in format "YYYY-MM-DDThh:mm:ssZ userId statusCode"

    Returns:
        ErrorResult object if found, None otherwise
    """
    # Parse all log entries
    entries = [parse_log_line(line) for line in log_lines]

    # Sort entries by timestamp to ensure chronological order
    entries.sort(key=lambda x: x.timestamp)

    # Track the earliest user with consecutive 500s
    earliest_user: Optional[str] = None
    earliest_timestamp: Optional[datetime] = None
    earliest_errors: List[str] = []

    # Track per-user consecutive 500 errors independently
    per_user_count: Dict[str, int] = {}
    per_user_timestamps: Dict[str, List[datetime]] = {}

    # Check for consecutive 500 errors in chronological order per user
    for entry in entries:
        user = entry.user_id
        if entry.status_code == 500:
            # Increment count and record timestamp
            per_user_count[user] = per_user_count.get(user, 0) + 1
            per_user_timestamps.setdefault(user, []).append(entry.timestamp)
            # Check if this user has 2+ consecutive 500s
            if per_user_count[user] >= 2:
                first_ts = per_user_timestamps[user][0]
                if earliest_user is None or first_ts < earliest_timestamp:  # type: ignore
                    earliest_user = user
                    earliest_timestamp = first_ts
                    earliest_errors = [ts.strftime(
                        "%Y-%m-%dT%H:%M:%SZ") for ts in per_user_timestamps[user][:2]]
        else:
            # Reset this user's consecutive 500 count
            per_user_count[user] = 0
            per_user_timestamps[user] = []

    if earliest_user:
        output = ErrorResult(
            user_id=earliest_user,
            error_timestamps=earliest_errors
        )
        print(f"Found consecutive errors for user: {output.user_id}")
        print(f"Error timestamps: {output.error_timestamps}")
        return output
    else:
        print("No consecutive 500 errors found.")
        return None


def test_find_consecutive_errors():
    """Test cases for the find_consecutive_errors function."""
    # Test case 1: Positive case with consecutive 500s
    logs1 = [
        "2025-04-11T13:45:00Z user123 200",
        "2025-04-11T13:45:05Z user456 500",
        "2025-04-11T13:45:10Z user123 500",
        "2025-04-11T13:45:12Z user123 500",
        "2025-04-11T13:45:15Z user456 500"
    ]
    result1 = find_consecutive_errors(logs1)
    assert result1 is not None
    # user456 has consecutive 500s at 13:45:05Z and 13:45:15Z
    assert result1.user_id == "user456"
    assert result1.error_timestamps == [
        "2025-04-11T13:45:05Z", "2025-04-11T13:45:15Z"]

    # Test case 2: Negative case with no consecutive 500s
    logs2 = [
        "2025-04-11T13:45:00Z user123 200",
        "2025-04-11T13:45:05Z user456 500",
        "2025-04-11T13:45:10Z user123 200",
        "2025-04-11T13:45:12Z user123 500",
        "2025-04-11T13:45:15Z user456 200"
    ]
    result2 = find_consecutive_errors(logs2)
    assert result2 is None

    # Test case 3: Multiple users with consecutive 500s, should return earliest
    logs3 = [
        "2025-04-11T13:45:00Z user123 500",
        "2025-04-11T13:45:05Z user123 500",
        "2025-04-11T13:45:10Z user456 500",
        "2025-04-11T13:45:12Z user456 500"
    ]
    result3 = find_consecutive_errors(logs3)
    assert result3 is not None
    assert result3.user_id == "user123"
    assert result3.error_timestamps == [
        "2025-04-11T13:45:00Z", "2025-04-11T13:45:05Z"]

    print("All tests passed!")


if __name__ == "__main__":
    # Run the test cases
    print("Running test cases...")
    test_find_consecutive_errors()
    print("Test cases executed successfully.\n")

    print("Testing with `test_log.txt`")
    # Use the file test_log.txt - this contains the log entries
    # It should pass without any duplicate 500 errors
    with open("test_log.txt", "r") as file:
        log_lines = file.readlines()
    y = find_consecutive_errors(log_lines)

    print("\nTesting with `test_log_modified.txt`")

    # Use the file test_log_modified.txt - this contains the log entries (modified)
    # It should pass with duplicate 500 errors for user127
    # BUG: Not able to find the consecutive 500 errors
    with open("test_log_modified.txt", "r") as file:
        log_lines = file.readlines()
    z = find_consecutive_errors(log_lines)
