# Web App Log Analyzer

This program processes web application log entries to identify the first user who experienced two or more consecutive HTTP 500 errors.

## Problem Requirements

1. Parses the logs.
1. Finds the first user who received 2 or more consecutive 500 errors.
1. Returns the user ID and the list of timestamps for those 500 errors.

## Implementation Details

The solution consists of the following components:

1. **Data Structures**:

   - `LogEntry`: A dataclass representing a single log entry with:
     - `timestamp`: datetime object
     - `user_id`: string
     - `status_code`: integer
   - `ErrorResult`: A dataclass containing the result with:
     - `user_id`: string
     - `error_timestamps`: List[str]

1. **Main Functions**:

   - `parse_log_line()`: Parses a log line string into a `LogEntry` object
   - `find_consecutive_errors()`: Processes log entries to find the first user with consecutive 500 errors

1. **Algorithm**:
   1. Parse all log entries into `LogEntry` objects
   1. Sort entries chronologically by timestamp
   1. Group entries by user_id for efficient processing
   1. For each user:
      - Track consecutive 500 errors
      - Return immediately when finding 2+ consecutive errors
      - Reset tracking on non-500 status codes
   1. Return None if no user has consecutive 500s

## Usage

```python
from log_analyzer import find_consecutive_errors

# Example log entries
logs = [
    "2025-04-11T13:45:00Z user123 200",
    "2025-04-11T13:45:05Z user456 500",
    "2025-04-11T13:45:10Z user123 500",
    "2025-04-11T13:45:12Z user123 500",
    "2025-04-11T13:45:15Z user456 500"
]

# Find consecutive errors
result = find_consecutive_errors(logs)

if result:
    print(f"User {result.user_id} experienced consecutive 500 errors at:")
    for timestamp in result.error_timestamps:
        print(f"  - {timestamp}")
else:
    print("No user experienced consecutive 500 errors")
```

## Testing

The implementation includes three comprehensive test cases:

1. **Positive Case**:

   - Tests detection of consecutive 500s
   - Verifies correct user identification
   - Validates timestamp collection

1. **Negative Case**:

   - Verifies handling of non-consecutive 500s
   - Confirms None return when no consecutive errors exist

1. **Multiple Users Case**:
   - Tests handling of multiple users with consecutive errors
   - Verifies earliest occurrence is returned
   - Validates chronological ordering

Run the tests by executing:

```bash
python log_analyzer.py
```

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
- Space: O(n) for storing parsed entries and user groups
- Where n is the number of log entries

## Dependencies

- Python 3.7+
- Standard library only (no external packages required)
- Uses type hints for better code clarity and IDE support
