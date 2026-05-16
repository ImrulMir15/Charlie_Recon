<p align="center">
  <img src="screenshots/banner.png" alt="Charlie_Recon Banner" width="100%"/>
</p>

<h1 align="center">⚡ Charlie_Recon</h1>

<p align="center">
  <strong>A modern reconnaissance & intelligence-gathering toolkit for ethical hackers, bug bounty hunters, red teamers, and cybersecurity researchers.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10%2B-00ff88?style=for-the-badge&logo=python&logoColor=white&labelColor=0d1117" alt="Python">
  <img src="https://img.shields.io/badge/platform-Kali%20Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white&labelColor=0d1117" alt="Kali Linux">
  <img src="https://img.shields.io/badge/license-Educational-00e5ff?style=for-the-badge&labelColor=0d1117" alt="License">
  <img src="https://img.shields.io/badge/version-1.0.0-ff2d55?style=for-the-badge&labelColor=0d1117" alt="Version">
  <img src="https://img.shields.io/badge/SecLists-Integrated-bd5fff?style=for-the-badge&labelColor=0d1117" alt="SecLists">
  <img src="https://img.shields.io/badge/author-ImrulMir-00ff88?style=for-the-badge&labelColor=0d1117" alt="Author">
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-usage-examples">Usage</a> •
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-output--reports">Reports</a> •
  <a href="#-legal-disclaimer">Disclaimer</a>
</p>

---

## 📸 Preview

### CLI — Cyberpunk Terminal Interface
<p align="center">
  <img src="screenshots/cli_banner.png" alt="Charlie_Recon CLI Banner" width="80%"/>
</p>

### Vulnerability Scanning in Action
<p align="center">
  <img src="screenshots/cli_scan.png" alt="Charlie_Recon Vulnerability Scanning" width="80%"/>
</p>

### HTML Report — Interactive Cybersecurity Dashboard
<p align="center">
  <img src="screenshots/html_report.png" alt="Charlie_Recon HTML Report Dashboard" width="100%"/>
</p>

---

## ⚡ Quick Start

> **Designed for Kali Linux** — works out of the box with virtual environments.

### Step 1: Clone & Setup

```bash
git clone https://github.com/ImrulMir/Charlie_Recon.git
cd Charlie_Recon
chmod +x setup.sh && ./setup.sh
```

### Step 2: Activate & Run

```bash
source venv/bin/activate
python3 charlie_recon.py -t scanme.nmap.org
```

### Step 3: View Report

```bash
firefox charlie_recon_output/*/report.html
```

> 💡 **PDF Download:** Click the **"Download PDF"** button inside the HTML report.

<details>
<summary>📋 Manual Setup (if setup.sh doesn't work)</summary>

```bash
git clone https://github.com/ImrulMir/Charlie_Recon.git
cd Charlie_Recon

# Create virtual environment (required on Kali Linux)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install SecLists (if not already on your system)
sudo apt install seclists
# OR
git clone --depth 1 https://github.com/danielmiessler/SecLists.git ~/SecLists

# Run
python3 charlie_recon.py -t example.com
```

</details>

---

## 🚀 Usage Examples

```bash
# Basic scan
python3 charlie_recon.py -t example.com

# Scan an IP address
python3 charlie_recon.py -t 192.168.1.1

# Scan a full URL
python3 charlie_recon.py -t https://target.com

# Full scan with external tools
python3 charlie_recon.py -t example.com --nikto --nuclei

# Stealth mode (slower, evasive scanning)
python3 charlie_recon.py -t example.com --stealth

# Custom threads and depth
python3 charlie_recon.py -t example.com --threads 20 --depth 5

# Skip specific phases
python3 charlie_recon.py -t example.com --skip-crawl --skip-vuln

# Show help
python3 charlie_recon.py -h
```

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔍 Reconnaissance
- **WHOIS** — Registration, registrar, dates
- **DNS** — A, AAAA, CNAME, MX, NS, TXT, SOA, PTR
- **Subdomains** — 6 passive sources + SecLists brute-force
- **Ports** — Nmap top 1000 with banner grabbing
- **Tech Detection** — 30+ technologies (WAF bypass)
- **Header Audit** — 8 security headers + cookies

</td>
<td width="50%">

### 🕷️ Crawling & Discovery
- **Web Crawler** — Recursive BFS with depth control
- **Dir Bruteforce** — SecLists (3000 paths)
- **JS Analysis** — API keys, secrets, endpoints
- **Param Extraction** — URL + form field mining

</td>
</tr>
<tr>
<td>

### ⚡ Vulnerability Scanning
- **9 Built-in Checks:**
  - CORS misconfiguration
  - Clickjacking (X-Frame-Options)
  - XSS reflection
  - SQL error detection
  - Open redirect
  - Sensitive file exposure
  - HTTP methods (PUT/DELETE)
  - Information disclosure
  - Missing security headers
- **Nikto** integration (optional)
- **Nuclei** integration (optional)

</td>
<td>

### 📊 Reporting
- **HTML Report** — Dark cyberpunk dashboard
  - Severity donut chart
  - Expandable sections
  - 🔴 Red rows = internal IPs
  - 🟡 Amber rows = dev/admin/staging
  - Smart hacker-priority sorting
  - One-click PDF download
- **JSON Export** — Machine-readable

</td>
</tr>
</table>

---

## 🔗 Subdomain Sources (6 Passive + Active)

| # | Source | Type |
|---|--------|------|
| 1 | **crt.sh** | Certificate Transparency logs |
| 2 | **HackerTarget** | DNS search API |
| 3 | **RapidDNS** | DNS database |
| 4 | **AlienVault OTX** | Threat intelligence |
| 5 | **URLScan.io** | Web scanning archive |
| 6 | **Anubis-DB** | Subdomain database |
| 7 | **SecLists DNS** | Active brute-force (5000 words) |

---

## 📖 CLI Options

```
usage: charlie_recon.py [-h] -t TARGET [-o OUTPUT] [--threads N] [--timeout N]
                        [--depth N] [--rate-limit N]
                        [--skip-recon] [--skip-crawl] [--skip-vuln]
                        [--nikto] [--nuclei] [--stealth] [-v] [--no-banner]
```

| Flag | Description | Default |
|------|-------------|---------|
| `-t, --target` | Target domain, URL, or IP | **Required** |
| `-o, --output` | Output base directory | `charlie_recon_output` |
| `--threads` | Number of threads | `10` |
| `--timeout` | Request timeout (seconds) | `15` |
| `--depth` | Crawler depth | `3` |
| `--rate-limit` | Max requests/second | `15` |
| `--skip-recon` | Skip reconnaissance phase | — |
| `--skip-crawl` | Skip crawling phase | — |
| `--skip-vuln` | Skip vulnerability scanning | — |
| `--nikto` | Enable Nikto scanner | — |
| `--nuclei` | Enable Nuclei scanner | — |
| `--stealth` | Stealth mode (random delays) | — |
| `-v, --verbose` | Verbose output | — |
| `--no-banner` | Suppress ASCII banner | — |
| `-h, --help` | Show help message | — |

---

## 📊 Output & Reports

Each scan creates a **unique timestamped folder** — reports never overwrite:

```
charlie_recon_output/
├── example_com_20260517_030000/
│   ├── report.html          ← Interactive HTML dashboard
│   └── results.json         ← Machine-readable JSON
├── scanme_nmap_org_20260517_031500/
│   ├── report.html
│   └── results.json
```

### HTML Report Highlights
- 🎨 **Dark Cyberpunk theme** with animated scanline & gradient glow
- 📊 **Dashboard** with live statistics and severity donut chart
- 🔴 **Red-highlighted rows** — subdomains with internal IPs (10.x, 192.168.x, 172.x)
- 🟡 **Amber-highlighted rows** — interesting targets (admin, dev, staging, vpn, api)
- 📂 **Smart sorting** — most vulnerable/interesting findings always on top
- 📥 **One-click PDF download**
- 🔍 **Expand All** button for deep inspection

---

## 🏗️ Architecture

```
Charlie_Recon/
├── charlie_recon.py           # CLI entry point
├── setup.sh                   # One-command Kali setup
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container support
├── docker-compose.yml         # Docker Compose config
├── core/
│   ├── engine.py              # Scan orchestrator
│   ├── config.py              # Config + top 1000 ports
│   ├── logger.py              # Rich console output
│   ├── validator.py           # Input validation
│   └── seclists.py            # SecLists manager
└── modules/
    ├── recon/                 # 6 recon modules
    │   ├── whois_lookup.py
    │   ├── dns_recon.py
    │   ├── subdomain_enum.py
    │   ├── port_scanner.py
    │   ├── tech_detect.py
    │   └── header_analyzer.py
    ├── crawler/               # 4 discovery modules
    │   ├── crawler.py
    │   ├── dir_bruteforce.py
    │   ├── js_analyzer.py
    │   └── param_extractor.py
    ├── scanners/              # 3 vuln scanner modules
    │   ├── custom_checks.py
    │   ├── nikto_scanner.py
    │   └── nuclei_scanner.py
    └── report/                # HTML + JSON generators
        ├── html_report.py
        └── json_export.py
```

### Scan Pipeline

```
┌──────────────────────────────────────────────────────────────┐
│                     TARGET INPUT                              │
│            (domain / URL / IP address)                        │
└─────────────┬────────────────────────────────────────────────┘
              ▼
┌──────────────────────────────────────────────────────────────┐
│  VALIDATION → HTTP/HTTPS Probe → SecLists Init               │
└─────────────┬────────────────────────────────────────────────┘
              ▼
┌──────────────────────────────────────────────────────────────┐
│  Phase 1: RECONNAISSANCE                                      │
│  WHOIS → DNS → Subdomains (2000+) → Ports (1000) → Tech      │
│  → Headers                                                    │
└─────────────┬────────────────────────────────────────────────┘
              ▼
┌──────────────────────────────────────────────────────────────┐
│  Phase 2: CRAWLING & DISCOVERY                                │
│  Crawler → Dir Bruteforce (3000) → JS Analysis → Params      │
└─────────────┬────────────────────────────────────────────────┘
              ▼
┌──────────────────────────────────────────────────────────────┐
│  Phase 3: VULNERABILITY SCANNING                              │
│  9 Custom Checks → Nikto (opt) → Nuclei (opt)                │
└─────────────┬────────────────────────────────────────────────┘
              ▼
┌──────────────────────────────────────────────────────────────┐
│  Phase 4: REPORTING                                           │
│  Statistics → JSON Export → HTML Report (with PDF download)   │
└──────────────────────────────────────────────────────────────┘
```

---

## 🔧 Requirements

```
requests>=2.31.0
dnspython>=2.4.0
python-whois>=0.8.0
beautifulsoup4>=4.12.0
rich>=13.7.0
urllib3>=2.0.0
lxml>=4.9.0
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🔧 Optional: External Scanners

```bash
# Nikto (usually pre-installed on Kali)
sudo apt install nikto

# Nuclei
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
```

---

## 🐳 Docker

```bash
# Build image
docker build -t charlie_recon .

# Run a scan
docker run --rm -v $(pwd)/output:/app/charlie_recon_output charlie_recon -t example.com

# Using Docker Compose
docker compose run charlie_recon -t example.com
```

---

## ❓ Troubleshooting

<details>
<summary><b>"externally-managed-environment" error on Kali</b></summary>

Always use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
</details>

<details>
<summary><b>Technology Detection / Header Analysis times out</b></summary>

Some sites use aggressive WAFs (Akamai, Cloudflare) that block even browser-like requests. This is expected — the tool still collects subdomains, ports, DNS, and WHOIS data. Try a different target or use `--stealth`.
</details>

<details>
<summary><b>"SecLists not found" warning</b></summary>

```bash
sudo apt install seclists          # Kali/Debian
# OR
git clone --depth 1 https://github.com/danielmiessler/SecLists.git ~/SecLists
```
</details>

<details>
<summary><b>Scan is slow</b></summary>

- Port scanning 1000 ports takes ~60s depending on the target
- Skip phases: `--skip-recon` or `--skip-crawl`
- Increase threads: `--threads 30`
</details>

---

## 🛡️ Ethical Safeguards

- ⚠️ Authorization disclaimer on every scan
- 🔒 Rate-limiting (15 req/s default)
- 🚫 Read-only checks — no destructive payloads
- 🎭 User-Agent rotation
- 📝 All activities timestamped

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-module`
3. Commit your changes: `git commit -m 'Add new recon module'`
4. Push to the branch: `git push origin feature/new-module`
5. Open a Pull Request

---

## ⚠️ Legal Disclaimer

> **This tool is intended for authorized security testing only.**
> Only scan targets you have **explicit written permission** to test.
> Unauthorized scanning is illegal and unethical.
> The author assumes **no liability** for misuse of this tool.
> Use responsibly and within the bounds of applicable law.

---

## 📄 License

This project is licensed for **educational and authorized security research** purposes only.

---

<p align="center">
  <b>Built with ❤️ by <a href="https://github.com/ImrulMir">ImrulMir</a></b><br>
  <sub>⚡ Charlie_Recon — See everything. Miss nothing.</sub>
</p>
