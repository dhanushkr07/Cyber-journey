# My Linux Command Notes — Bandit 0-20

## Navigation & files
- `ls` / `ls -a` / `ls -l` — list files (-a shows hidden, -l shows details)
- `cd` — change directory
- `cat` — read a file
- `file` — identify what type of file something is
- `mv` — rename/move
- `cp` — copy
- `mkdir` — make a folder

## Searching
- `find . -type f -size 1033c` — find files by size
- `find / -user X -group Y -size 33c 2>/dev/null` — search whole system, hide errors
- `grep millionth data.txt` — find a line inside a file
- `sort data.txt | uniq -u` — show only unique lines
- `diff old new` — compare two files

## Decoding / decompressing
- `strings data.txt` — pull readable text from binary
- `base64 -d data.txt` — decode base64
- `tr 'A-Za-z' 'N-ZA-Mn-za-m'` — ROT13
- `xxd -r file > out` — reverse a hexdump
- `tar -xf`, `gzip -d`, `bzip2 -d` — unpack archives

## Networking & access
- `ssh user@host -p 2220` — log in
- `ssh -i keyfile user@host` — log in with a private key
- `nc localhost 30000` — connect to a port
- `nc -l 1234` — listen on a port
- `nmap -p 31000-32000 localhost` — scan ports
- `openssl s_client -connect host:port` — SSL connection

## Tricks I learned
- `./-file` — read a file that starts with a dash
- `cat "file with spaces"` — quotes handle spaces
- setuid (`-rws...`) — program runs as its owner, not you
