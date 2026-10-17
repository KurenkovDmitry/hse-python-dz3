#!/bin/sh

set -e

cd "$(dirname "$0")"

sh start.sh &
SERVER_PID=$!

trap 'kill "$SERVER_PID" 2>/dev/null || true' EXIT

i=0
until curl -fsS http://127.0.0.1:8000/openapi.json >/dev/null 2>&1; do
    i=$((i + 1))
    if [ "$i" -ge 30 ]; then
        echo "FAIL: Server did not start"
        exit 1
    fi
    sleep 1
done

sh test.sh
