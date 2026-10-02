# SQL Injection — WHERE clause reveals hidden data

**Type:** SQL Injection (OWASP A03: Injection)
**Target:** PortSwigger Web Security Academy lab (training environment)
**Date:** 2026-10-02
**Status:** Exploited ✅

## Summary
The product category filter passes user input directly into a SQL query without
sanitization, letting an attacker alter the query logic and retrieve hidden
(unreleased) products.

## Steps to reproduce
1. Open the shop, pick a category: `.../filter?category=Gifts`
2. Only that category's released products are shown.
3. Replace the category value with the payload: `' OR 1=1--`
4. The app now returns ALL products, including hidden ones.

## Payload
' OR 1=1--

## Why it works
The vulnerable query is effectively:
SELECT * FROM products WHERE category = '$input' AND released = 1

Injecting the payload makes it:
SELECT * FROM products WHERE category = '' OR 1=1-- ' AND released = 1

- `'` closes the opening string
- `OR 1=1` makes the condition always true
- `--` comments out the rest (removes the `AND released = 1` filter)

Result: every row returned, hidden data included.

## Impact
Bypasses the app's data filter to read records it intends to hide. In a real
system this pattern escalates to dumping whole tables (users, passwords, PII).

## Remediation
- Use parameterized queries / prepared statements (never concatenate input into SQL)
- Validate / whitelist input
- Run the DB with least privilege
