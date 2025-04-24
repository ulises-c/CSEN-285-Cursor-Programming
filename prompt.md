# Cursor Prompt

```md
You are an AI coding assistant. Your task is to write a program that processes a list of web‐app log entries and identifies the first user who experienced two or more consecutive HTTP 500 errors, returning that user’s ID along with the timestamps of those errors.

## Requirements

1. **Input**: an array (or list) of strings, each in the format:
```

"YYYY-MM-DDThh:mm:ssZ userId statusCode"

````text
- `timestamp` is an ISO-8601 UTC timestamp.
- `userId` is an alphanumeric string.
- `statusCode` is an integer (e.g. 200, 404, 500).

2. **Processing**:
- Parse each log line into its three parts: timestamp, userId, statusCode.
- Scan through the logs **in chronological order**.
- Track per-user sequences of consecutive 500 errors.
- Stop as soon as you find the **first** user who has **two or more** 500s in a row.

3. **Output**:
- If found, return an object (or struct) with:
  - `userId`: the ID of that user.
  - `errorTimestamps`: an array of the consecutive 500-error timestamps for that user.
- If **no** user has ≥2 consecutive 500s, return `null` or an empty structure.

4. **Edge cases**:
- Logs may contain other status codes interleaved.
- A user may have multiple 500s non-consecutively—only count runs without interruption.
- Multiple users may have runs; only the **earliest** run (by log order) counts.

5. **Example**
```text
Input:
[
  "2025-04-11T13:45:00Z user123 200",
  "2025-04-11T13:45:05Z user456 500",
  "2025-04-11T13:45:10Z user123 500",
  "2025-04-11T13:45:12Z user123 500",
  "2025-04-11T13:45:15Z user456 500"
]

Processing:
- user456: first 500 at 13:45:05Z, but next log for user456 is 13:45:15Z (still 500) → 2 in a row.
- user123: 500s at 13:45:10Z and 13:45:12Z → also 2 in a row, but those happen *later* in the log.

Earliest run is user456 at [13:45:05Z, 13:45:15Z].

Output:
{
  "userId": "user456",
  "errorTimestamps": ["2025-04-11T13:45:05Z", "2025-04-11T13:45:15Z"]
}
````

6. **Deliverables**
   - Well-structured, commented source code in your language of choice (e.g. Python, JavaScript, Java).
   - A brief explanation of your approach.
   - At least one unit test covering:
     - A positive case (consecutive 500s found).
     - A negative case (no user has ≥2 consecutive 500s).

---

Please provide the complete implementation, explanation, and tests.

```

```
