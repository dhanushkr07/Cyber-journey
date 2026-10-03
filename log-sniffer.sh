#!/bin/bash
# log-sniffer.sh v2 - SOC triage: auth anomalies + web attack signatures
# Usage: ./log-sniffer.sh <logfile>
# v2: also detects web attack signatures (XSS, SQLi, path traversal) — red-team knowledge as a blue-team tool.

LOGFILE="$1"

if [ ! -f "$LOGFILE" ]; then
    echo "Error: file '$LOGFILE' not found."
    exit 1
fi

XSS="<script|%3Cscript|onerror=|onload=|alert\(|javascript:"
SQLI="union select|' or '|or 1=1|drop table|sleep\(|benchmark\("
TRAV="\.\./|\.\.%2f"
ATTACKS="$XSS|$SQLI|$TRAV"

echo "=== Scanning $LOGFILE ==="

echo ""
echo "[!] Failed login attempts:"
grep -ci "failed password" "$LOGFILE"

echo ""
echo "[!] Top IPs (failed logins):"
grep -i "failed password" "$LOGFILE" | grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" | sort | uniq -c | sort -rn | head -5

echo ""
echo "[!] Error / denied / invalid lines:"
grep -icE "error|denied|invalid" "$LOGFILE"

echo ""
echo "===== WEB ATTACK SIGNATURES ====="
echo ""
echo "[XSS] attempts:            $(grep -icE "$XSS" "$LOGFILE")"
echo "[SQLi] attempts:           $(grep -icE "$SQLI" "$LOGFILE")"
echo "[Path traversal] attempts: $(grep -icE "$TRAV" "$LOGFILE")"

echo ""
echo "[!] Top web-attacker IPs:"
grep -iE "$ATTACKS" "$LOGFILE" | grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" | sort | uniq -c | sort -rn | head -5

echo ""
echo "[!] Sample attack lines:"
grep -inE "$ATTACKS" "$LOGFILE" | head -5
