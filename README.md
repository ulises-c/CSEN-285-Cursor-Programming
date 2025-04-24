# Web App Log Analyzer

This project implements a log analyzer for web application logs that identifies users who have experienced consecutive HTTP 500 errors.

## Problem Requirements

The log analyzer:

1. Parses web application log entries
2. Finds the first user who received 2 or more consecutive 500 errors
3. Returns the user ID and the list of timestamps for those 500 errors

## Implementation Details

The code is implemented in Python and consists of the following components:

- `LogEntry` class: Represents a single log entry with timestamp, user ID, and status code
- `ErrorResult` class: Represents the result of finding consecutive 500 errors
- `parse_log_line()` function: Parses a log line into a LogEntry object
- `find_consecutive_errors()` function: Finds the first user who experienced consecutive 500 errors

### How It Works

The `find_consecutive_errors()` function:

1. Parses all log entries and sorts them by timestamp
2. Tracks consecutive 500 errors for each user independently using dictionaries
3. When a user has 2 or more consecutive 500 errors, it records the user ID and timestamps
4. Returns the earliest occurrence of consecutive 500 errors across all users

### Algorithm Approach

The implementation follows these key steps:

1. Parse all log entries into structured objects
2. Sort entries chronologically by timestamp
3. Track consecutive 500 errors for each user using separate counters and timestamp lists
4. Reset tracking when encountering non-500 status codes
5. Return the earliest occurrence of consecutive 500 errors

## Usage

```python
from log_analyzer import find_consecutive_errors

# Example log entries
log_lines = [
    "2025-04-11T13:45:00Z user123 200",
    "2025-04-11T13:45:05Z user456 500",
    "2025-04-11T13:45:10Z user123 500",
    "2025-04-11T13:45:12Z user123 500",
    "2025-04-11T13:45:15Z user456 500"
]

# Find consecutive 500 errors
result = find_consecutive_errors(log_lines)

if result:
    print(f"User {result.user_id} experienced consecutive 500 errors at:")
    for timestamp in result.error_timestamps:
        print(f"  - {timestamp}")
else:
    print("No consecutive 500 errors found.")
```

## Test Files

The project includes two test files:

- `test_log.txt`: Contains log entries without any consecutive 500 errors
- `test_log_modified.txt`: Contains log entries with consecutive 500 errors for user127

## Running the Tests

To run the tests, simply execute the Python script:

```bash
python log_analyzer.py
```

This will run the test cases and process both test log files.

## Input Format

Each log entry should be a string in the format:

```text
YYYY-MM-DDThh:mm:ssZ userId statusCode
```

Where:

- `timestamp`: ISO-8601 UTC timestamp (e.g., "2025-04-11T13:45:00Z")
- `userId`: Alphanumeric string identifier
- `statusCode`: Integer HTTP status code

## Error Handling

The implementation includes robust error handling for:

- Invalid log line format (wrong number of components)
- Invalid timestamp format
- Non-integer status codes
- Empty log lists

## Performance Considerations

The algorithm has the following complexity:

- Time: O(n log n) due to sorting
- Space: O(n) for storing parsed entries and user tracking data
- Where n is the number of log entries

## Dependencies

- Python 3.7+
- Standard library only (no external packages required)
- Uses type hints for better code clarity and IDE support

## Alternative Implementations

This problem can be implemented in various programming languages. The prompt.md file provides guidelines for implementing this log analyzer in other languages such as:

- JavaScript/TypeScript
- Go
- C/C++
- Java
- Ruby

Each implementation would follow the same general algorithm approach while adapting to the specific language's features and idioms.
