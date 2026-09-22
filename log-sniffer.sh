#!/bin/bash
# lo-sniffer.sh -quick SOC triage of a log file
# usage: ./log-sniffer.sh <logfile>
 LOGFILE="$1"

 if [ ! -f "$LOGFILE" ]; then
    echo "error: file '$LOGFILE' not found."
    exit 1
 fi

 echo "=== scanning $LOGFILE ==="

 echo""
 echo "[!] failed login attempts:"
 grep -ci "failed password" "$LOGFILE"

 echo ""
 echo "[!] Top attacking IPs (failed logins):"
 grep -i "failed password" "$LOGFILE" | grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" | sort | uniq -c | sort -rn | head -5


 echo ""
 echo "[!] Error / denied / invalid lines:"
 grep -icE "error|denied|invalid" "$LOGFILE"
