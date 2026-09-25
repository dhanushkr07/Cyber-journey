# 🔐 Cyber-journey

Security + GenAI. Building in public — shipping a tool every week.

**Status: Week 1 COMPLETE ✅**

---

## ✅ Week 1 — Completed

- [x] Linux fundamentals + terminal fluency
- [x] OverTheWire **Bandit levels 0–26** (Linux, privilege escalation, brute force, restricted-shell escapes)
- [x] Set up **git + GitHub** workflow (add / commit / push)
- [x] Shipped **2 working security tools** (below)
- [x] Networking basics (IPs, ports, TCP) by building a port scanner

---

## 🛠️ Tools

### [`log-sniffer.sh`](log-sniffer.sh)
Bash SOC-triage tool. Scans a log file and reports failed logins, top attacking IPs, and error/denial counts.
```bash
./log-sniffer.sh fake-auth.log
```

### [`portscan.py`](portscan.py)
TCP port scanner in Python (a mini-nmap). Checks a target for common open ports — my first Python program.
```bash
python3 portscan.py scanme.nmap.org
```

### [`commands.md`](commands.md)
My running Linux/CLI cheat-sheet, built from Bandit + real work.

> ⚠️ **Ethics:** Only scan/test systems you own or have explicit written permission for.

---

## 📈 Weekly progress

| Week | Focus | Status |
|---|---|---|
| 1 | Linux, Bandit 0–26, Bash+Python tools, git | ✅ Done |
| 2 | Web app security (OWASP), Security+ prep, GenAI workflow | ⏳ In progress |
| 3+ | _updating weekly…_ | |

---

## 🎯 Direction
SOC / Blue Team → **AI Security (LLM / GenAI)**. Using AI agents to do security work faster.

_Follow the journey — new tool every week._
