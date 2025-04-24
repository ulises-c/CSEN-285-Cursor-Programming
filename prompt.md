# Web App Log Analyzer - Implementation Prompt

## Problem Description

You are given a list of log entries from a web application. Each entry is a string in the format:

```
[timestamp][user_id][status_code]
```

Example:

```
"2025-04-11T13:45:00Z user123 200"
"2025-04-11T13:45:05Z user456 500"
"2025-04-11T13:45:10Z user123 500"
```

## Requirements

Write a program that:

1. Parses the logs.
2. Finds the first user who received 2 or more consecutive 500 errors.
3. Returns the user ID and the list of timestamps for those 500 errors.

## Implementation Guidelines

### Data Structures

You should define appropriate data structures to represent:

- A log entry (with timestamp, user ID, and status code)
- The result of finding consecutive errors (with user ID and error timestamps)

### Core Functions

Your implementation should include:

1. A function to parse a log line into a structured format
2. A function to find the first user with consecutive 500 errors

### Algorithm Approach

1. Parse all log entries into structured objects
2. Sort entries chronologically by timestamp
3. Track consecutive 500 errors for each user
4. Return the earliest occurrence of consecutive 500 errors

### Error Handling

Your implementation should handle:

- Invalid log line formats
- Invalid timestamp formats
- Non-integer status codes
- Empty log lists

## Example

For the following log entries:

```
"2025-04-11T13:45:00Z user123 200"
"2025-04-11T13:45:05Z user456 500"
"2025-04-11T13:45:10Z user123 500"
"2025-04-11T13:45:12Z user123 500"
"2025-04-11T13:45:15Z user456 500"
```

The program should identify that user123 has consecutive 500 errors at timestamps "2025-04-11T13:45:10Z" and "2025-04-11T13:45:12Z".

## Testing

Include test cases for:

1. A positive case with consecutive 500 errors
2. A negative case with no consecutive 500 errors
3. A case with multiple users having consecutive 500 errors (should return the earliest one)

## Language Options

You can implement this in any programming language of your choice. Some suggestions:

- Python
- JavaScript/TypeScript
- Go
- C/C++
- Java
- Ruby

## Evaluation Criteria

Your solution will be evaluated on:

1. Correctness (handles all test cases correctly)
2. Code organization and readability
3. Error handling
4. Performance (efficient algorithm)
5. Documentation

## Bonus Challenges

1. Handle log entries with the same timestamp
2. Support different log formats
3. Implement a command-line interface to process log files
4. Add visualization of the error patterns

```

```
