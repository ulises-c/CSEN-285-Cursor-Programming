# AI Coding - In Class Assignment

Use AI-Coding assitance to solve
You are given a list of log entries from a web application. Each entry is a string in the format:
`"[timestamp][user_id][status_code]"`

example

```text
"2025-04-11T13:45:00Z user123 200"
"2025-04-11T13:45:05Z user456 500"
"2025-04-11T13:45:10Z user123 500"
```

Write a program that:

1. Parses the logs.
2. Finds the first use who received 2 or more consecutive 500 errors.
3. Retruns the user ID and the list of timestamps for those 500 errors.
