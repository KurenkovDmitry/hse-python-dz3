#!/bin/sh
set -e

URL="http://127.0.0.1:8000/calculate/"

test_api() {
    name="$1"
    data="$2"
    expected="$3"

    response=$(curl -s -w '\n%{http_code}' \
        -X POST "$URL" \
        -H "Content-Type: application/json" \
        -d "$data")

    status=$(printf '%s\n' "$response" | tail -n 1)

    if [ "$status" = "$expected" ]; then
        echo "PASS: $name (HTTP $status)"
    else
        echo "FAIL: $name (expected $expected, got: $status)"
        exit 1
    fi
}

test_api "Valid request" \
    '{"numbers":[5,3,10],"delays":[1,2,0.5]}' 200

test_api "Different array length - 1" \
    '{"numbers":[5],"delays":[1,2]}' 422

test_api "Different array length - 2" \
    '{"numbers":[5,3],"delays":[1]}' 422

test_api "Negative delay" \
    '{"numbers":[5],"delays":[-1]}' 422

test_api "Empty arrays" \
    '{"numbers":[],"delays":[]}' 422

test_api "Missing numbers" \
    '{"delays":[1]}' 422

response=$(curl -fsS -X POST "$URL" \
    -H "Content-Type: application/json" \
    -d '{"numbers":[5,3,10],"delays":[1,2,0.5]}')

printf '%s' "$response" | python3 -c '
import json
import sys

data = json.load(sys.stdin)

expected = [
    (5, 25, 1),
    (3, 9, 2),
    (10, 100, 0.5)
]

result = data["results"]

assert len(result) == 3, "Wrong results count)"

for result, (number, square, delay) in zip(result, expected):
    assert result["number"] == number
    assert result["square"] == square
    assert result["delay"] == delay
    assert delay <= result["time"] <= delay + 0.5, "Wrong task time"

assert 2 <= data["total_time"] <= 2.5, "Wrong total time"
assert data["parallel_faster_than_sequential"] is True

print("PASS: Response data and parallel execution")
' || exit 1

echo "All HTTP status tests passed"
