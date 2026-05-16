"""
Charlie_Recon - HTML Report Generator
Author: ImrulMir
Generates a hacker-themed, self-contained HTML report with charts and animations.
"""

import html
import json
from datetime import datetime


class HTMLReportGenerator:
    """Generates a stunning cyberpunk-themed HTML security report for Charlie_Recon."""

    def __init__(self, results, output_path):
        self.results = results
        self.output_path = output_path

    def generate(self):
        """Generate the full HTML report."""
        meta = self.results.get("meta", {})
        target = self.results.get("target", {})
        recon = self.results.get("recon", {})
        crawler = self.results.get("crawler", {})
        vulns = self.results.get("vulnerabilities", [])
        stats = self.results.get("statistics", {})

        # Severity counts
        sev_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}
        for v in vulns:
            s = v.get("severity", "INFO").upper()
            if s in sev_counts:
                sev_counts[s] += 1

        report_html = self._build_html(meta, target, recon, crawler, vulns, stats, sev_counts)
        with open(self.output_path, "w", encoding="utf-8") as f:
            f.write(report_html)

    def _build_html(self, meta, target, recon, crawler, vulns, stats, sev_counts):
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Charlie_Recon Report - {self._esc(target.get('domain',''))}</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
<style>{self._css()}</style>
</head>
<body>
<div class="scanline"></div>
<div class="container">
  {self._header_section(meta, target)}
  {self._nav_section()}
  {self._stats_section(stats, sev_counts)}
  {self._vuln_chart_section(sev_counts)}
  {self._target_section(target)}
  {self._recon_section(recon)}
  {self._crawler_section(crawler)}
  {self._vuln_section(vulns)}
  {self._footer_section(meta)}
</div>
<script>{self._js(sev_counts)}</script>
</body>
</html>"""

    def _css(self):
        return """
:root{--bg:#0d1117;--surface:#0f1923;--surface2:#131d2b;--border:#1e2d40;--green:#00ff88;--red:#ff2d55;--blue:#00c8ff;--amber:#ffc107;--purple:#bd5fff;--cyan:#00e5ff;--text:#d0dbe8;--dim:#4a6080;--glow-green:rgba(0,255,136,0.18);--glow-blue:rgba(0,200,255,0.18);--glow-red:rgba(255,45,85,0.18)}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:'JetBrains Mono',monospace;font-size:14px;line-height:1.6;overflow-x:hidden;background-image:radial-gradient(ellipse at 20% 50%,rgba(0,200,255,0.04) 0%,transparent 60%),radial-gradient(ellipse at 80% 20%,rgba(189,95,255,0.04) 0%,transparent 60%)}
.scanline{position:fixed;top:0;left:0;width:100%;height:3px;background:linear-gradient(90deg,transparent,var(--green),transparent);opacity:0.5;z-index:9999;animation:scanline 5s ease-in-out infinite}
@keyframes scanline{0%{top:-5px;opacity:0}30%{opacity:0.6}70%{opacity:0.6}100%{top:100vh;opacity:0}}
.container{max-width:1280px;margin:0 auto;padding:24px 20px}
h1,h2,h3{font-family:'Orbitron',sans-serif}
.header{text-align:center;padding:48px 0 28px;border-bottom:1px solid var(--border);position:relative;overflow:hidden}
.header::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:radial-gradient(ellipse at center top,rgba(0,200,255,0.06),transparent 70%);pointer-events:none}
.header h1{font-size:2.6em;background:linear-gradient(135deg,var(--green),var(--cyan));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;text-shadow:none;margin-bottom:10px;letter-spacing:3px;animation:glow-text 3s ease-in-out infinite alternate}
@keyframes glow-text{from{filter:drop-shadow(0 0 8px rgba(0,255,136,0.4))}to{filter:drop-shadow(0 0 20px rgba(0,200,255,0.5))}}
.header .subtitle{color:var(--dim);font-size:0.9em;letter-spacing:1px}
.header .target-badge{display:inline-block;background:rgba(0,200,255,0.08);border:1px solid var(--cyan);padding:8px 24px;border-radius:6px;margin-top:14px;color:var(--cyan);font-size:1em;letter-spacing:2px;box-shadow:0 0 16px rgba(0,200,255,0.12)}
nav{display:flex;flex-wrap:wrap;gap:8px;padding:18px 0;border-bottom:1px solid var(--border);margin-bottom:28px;align-items:center}
nav a{color:var(--dim);text-decoration:none;padding:7px 16px;border:1px solid var(--border);border-radius:5px;font-size:0.8em;transition:all .25s;letter-spacing:.5px}
nav a:hover{color:var(--green);border-color:var(--green);background:var(--glow-green);box-shadow:0 0 10px var(--glow-green)}
.stats-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px;margin-bottom:32px}
.stat-card{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:18px 14px;text-align:center;transition:all .3s;position:relative;overflow:hidden}
.stat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--green),var(--cyan));opacity:0;transition:opacity .3s}
.stat-card:hover{border-color:var(--green);box-shadow:0 0 20px var(--glow-green);transform:translateY(-2px)}
.stat-card:hover::before{opacity:1}
.stat-card .value{font-family:'Orbitron',sans-serif;font-size:2em;color:var(--green);line-height:1}
.stat-card .label{font-size:0.72em;color:var(--dim);margin-top:6px;text-transform:uppercase;letter-spacing:1px}
.section{margin-bottom:32px}
.section-title{font-size:1.05em;color:var(--cyan);padding:12px 0;border-bottom:1px solid var(--border);margin-bottom:16px;display:flex;align-items:center;gap:10px;letter-spacing:1px}
table{width:100%;border-collapse:collapse;margin-bottom:16px;font-size:0.85em}
th{background:var(--surface2);color:var(--green);padding:10px 14px;text-align:left;border:1px solid var(--border);font-weight:600;text-transform:uppercase;font-size:0.72em;letter-spacing:1.5px}
td{padding:9px 14px;border:1px solid var(--border);vertical-align:top;word-break:break-word;transition:background .2s}
tr:nth-child(even) td{background:rgba(255,255,255,0.01)}
tr:hover td{background:rgba(0,255,136,0.03)}
tr.vuln-row td{background:rgba(255,45,85,0.07);border-left:3px solid var(--red)}
tr.warn-row td{background:rgba(255,193,7,0.06);border-left:3px solid var(--amber)}
.badge{display:inline-block;padding:2px 10px;border-radius:4px;font-size:0.72em;font-weight:700;text-transform:uppercase;letter-spacing:1px}
.badge-critical{background:rgba(255,45,85,0.15);color:#ff2d55;border:1px solid rgba(255,45,85,0.35)}
.badge-high{background:rgba(255,90,90,0.15);color:#ff5a5a;border:1px solid rgba(255,90,90,0.35)}
.badge-medium{background:rgba(255,193,7,0.15);color:#ffc107;border:1px solid rgba(255,193,7,0.35)}
.badge-low{background:rgba(0,200,255,0.15);color:#00c8ff;border:1px solid rgba(0,200,255,0.35)}
.badge-info{background:rgba(100,130,160,0.15);color:#7a9ab8;border:1px solid rgba(100,130,160,0.3)}
.vuln-card{background:var(--surface);border:1px solid var(--border);border-radius:8px;margin-bottom:10px;overflow:hidden;transition:border-color .2s}
.vuln-card:hover{border-color:var(--border)}
.vuln-header{display:flex;justify-content:space-between;align-items:center;padding:13px 18px;cursor:pointer;transition:background .2s;gap:12px}
.vuln-header:hover{background:var(--surface2)}
.vuln-header .title{font-weight:500;flex:1}
.vuln-body{padding:14px 18px;border-top:1px solid var(--border);display:none;font-size:0.85em;background:var(--surface2)}
.vuln-body.open{display:block;animation:fadeIn .2s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:translateY(0)}}
.vuln-body p{margin-bottom:8px}
.vuln-body .label{color:var(--dim);font-size:0.8em;text-transform:uppercase;letter-spacing:.5px}
.chart-container{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:24px;margin-bottom:32px;display:flex;justify-content:center;align-items:center;gap:40px;flex-wrap:wrap}
.donut-chart{position:relative;width:200px;height:200px}
.donut-chart canvas{width:200px;height:200px}
.chart-legend{display:flex;flex-direction:column;gap:10px}
.legend-item{display:flex;align-items:center;gap:10px;font-size:0.82em}
.legend-dot{width:12px;height:12px;border-radius:3px;flex-shrink:0}
.info-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}
.info-card{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:16px}
.info-card h4{color:var(--green);font-size:0.78em;margin-bottom:10px;text-transform:uppercase;letter-spacing:1px}
.info-card p,.info-card li{font-size:0.85em;color:var(--text);margin-bottom:5px}
.info-card ul{list-style:none;padding:0}
.info-card ul li::before{content:"▸ ";color:var(--green)}
.tag{display:inline-block;background:var(--surface2);border:1px solid var(--border);padding:2px 9px;border-radius:4px;font-size:0.75em;margin:2px;color:var(--text)}
.footer{text-align:center;padding:36px 0;border-top:1px solid var(--border);color:var(--dim);font-size:0.8em;letter-spacing:.5px}
.footer p{margin-bottom:6px}
.collapsible{cursor:pointer;user-select:none;padding:10px 0;margin-bottom:4px}
.collapsible::after{content:" ▸";color:var(--green)}
.collapsible.active::after{content:" ▾"}
.btn{display:inline-block;padding:8px 20px;border:1px solid var(--green);border-radius:5px;color:var(--green);background:rgba(0,255,136,0.05);cursor:pointer;font-family:'JetBrains Mono',monospace;font-size:0.8em;transition:all .25s;text-decoration:none;letter-spacing:.5px}
.btn:hover{background:rgba(0,255,136,0.14);box-shadow:0 0 14px var(--glow-green)}
.btn-red{border-color:var(--red);color:var(--red);background:rgba(255,45,85,0.05)}
.btn-red:hover{background:rgba(255,45,85,0.14);box-shadow:0 0 14px var(--glow-red)}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:var(--dim)}
@media(max-width:768px){.stats-grid{grid-template-columns:repeat(2,1fr)}.info-grid{grid-template-columns:1fr}.chart-container{flex-direction:column}nav{gap:6px}}
@media print{.scanline,.no-print{display:none!important}body{background:#fff;color:#000;font-size:11px}th{background:#eee;color:#000;-webkit-print-color-adjust:exact;print-color-adjust:exact}.container{max-width:100%}.badge{border:1px solid #333;color:#000;background:#eee;-webkit-print-color-adjust:exact;print-color-adjust:exact}.vuln-body{display:block!important}.collapsible-content{display:block!important}.stat-card{border:1px solid #ccc}.stat-card .value{color:#000}.header h1{color:#000;-webkit-text-fill-color:#000}.section-title{color:#000}nav{display:none}}
"""

    def _header_section(self, meta, target):
        return f"""
<div class="header">
  <h1>⚡ CHARLIE_RECON</h1>
  <p class="subtitle">Automated Reconnaissance & Vulnerability Assessment Report</p>
  <div class="target-badge">⎯ {self._esc(target.get('domain','N/A'))} ⎯</div>
  <p class="subtitle" style="margin-top:10px">
    {self._esc(meta.get('scan_date',''))} | v{self._esc(meta.get('version','1.0.0'))} | Author: {self._esc(meta.get('author','ImrulMir'))}
  </p>
</div>"""

    def _nav_section(self):
        return """
<nav>
  <a href="#stats">Dashboard</a>
  <a href="#target">Target</a>
  <a href="#recon">Reconnaissance</a>
  <a href="#crawler">Crawler</a>
  <a href="#vulns">Vulnerabilities</a>
  <a href="#" class="btn no-print" onclick="expandAll();return false">Expand All</a>
  <a href="#" class="btn btn-red no-print" onclick="downloadPDF();return false">Download PDF</a>
</nav>"""

    def _stats_section(self, stats, sev_counts):
        total_vulns = stats.get('total_vulnerabilities', 0)
        cards = f"""
<div id="stats" class="section">
  <h2 class="section-title">📊 Dashboard</h2>
  <div class="stats-grid">
    <div class="stat-card"><div class="value">{stats.get('total_subdomains',0)}</div><div class="label">Subdomains</div></div>
    <div class="stat-card"><div class="value">{stats.get('total_open_ports',0)}</div><div class="label">Open Ports</div></div>
    <div class="stat-card"><div class="value">{stats.get('total_technologies',0)}</div><div class="label">Technologies</div></div>
    <div class="stat-card"><div class="value">{stats.get('total_urls_crawled',0)}</div><div class="label">URLs Crawled</div></div>
    <div class="stat-card"><div class="value">{stats.get('total_directories',0)}</div><div class="label">Directories</div></div>
    <div class="stat-card"><div class="value" style="color:{'var(--red)' if total_vulns > 0 else 'var(--green)'}">{total_vulns}</div><div class="label">Vulnerabilities</div></div>
    <div class="stat-card"><div class="value">{stats.get('total_parameters',0)}</div><div class="label">Parameters</div></div>
    <div class="stat-card"><div class="value">{stats.get('scan_duration','N/A')}</div><div class="label">Duration</div></div>
  </div>
</div>"""
        return cards

    def _vuln_chart_section(self, sev_counts):
        total = sum(sev_counts.values())
        if total == 0:
            return ""
        colors = {"CRITICAL":"#ff0040","HIGH":"#ff4444","MEDIUM":"#ffaa00","LOW":"#00d4ff","INFO":"#888"}
        legend = ""
        for sev in ["CRITICAL","HIGH","MEDIUM","LOW","INFO"]:
            if sev_counts[sev] > 0:
                legend += f'<div class="legend-item"><div class="legend-dot" style="background:{colors[sev]}"></div>{sev}: {sev_counts[sev]}</div>'
        return f"""
<div class="chart-container">
  <div class="donut-chart"><canvas id="vulnChart" width="200" height="200"></canvas></div>
  <div class="chart-legend">{legend}</div>
</div>"""

    def _target_section(self, target):
        rows = ""
        for k in ["domain","ip","url","target_type","scheme"]:
            v = target.get(k,"")
            if v:
                rows += f"<tr><td><strong>{self._esc(k.replace('_',' ').title())}</strong></td><td>{self._esc(str(v))}</td></tr>"
        return f"""
<div id="target" class="section">
  <h2 class="section-title">🎯 Target Information</h2>
  <table><thead><tr><th>Property</th><th>Value</th></tr></thead><tbody>{rows}</tbody></table>
</div>"""

    def _recon_section(self, recon):
        parts = []
        # Subdomains — sorted by hacker priority
        subs = recon.get("subdomains",[])
        if subs:
            subs_sorted = self._sort_subdomains(subs)
            rows = ""
            for s in subs_sorted:
                if isinstance(s, dict):
                    ip = s.get('ip','N/A') or 'N/A'
                    cls = self._subdomain_row_class(s)
                    rows += f"<tr class='{cls}'><td>{self._esc(s.get('subdomain',''))}</td><td>{self._esc(ip)}</td><td>{self._esc(s.get('status',''))}</td></tr>"
                else:
                    rows += f"<tr><td>{self._esc(str(s))}</td><td>-</td><td>-</td></tr>"
            parts.append(f"""<h3 class="collapsible" onclick="toggle(this)">Subdomains ({len(subs)})</h3>
<div class="collapsible-content"><table><thead><tr><th>Subdomain</th><th>IP</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table></div>""")

        # Ports
        ports = recon.get("ports",[])
        open_ports = [p for p in ports if isinstance(p, dict) and p.get("state")=="open"]
        if open_ports:
            rows = ""
            for p in open_ports:
                rows += f"<tr><td>{p.get('port','')}</td><td><span class='badge badge-high'>OPEN</span></td><td>{self._esc(p.get('service',''))}</td><td>{self._esc(p.get('banner','')[:60])}</td></tr>"
            parts.append(f"""<h3 class="collapsible" onclick="toggle(this)">Open Ports ({len(open_ports)})</h3>
<div class="collapsible-content"><table><thead><tr><th>Port</th><th>State</th><th>Service</th><th>Banner</th></tr></thead><tbody>{rows}</tbody></table></div>""")

        # Technologies
        techs = recon.get("technologies",[])
        if techs:
            rows = ""
            for t in techs:
                if isinstance(t, dict):
                    rows += f"<tr><td>{self._esc(t.get('name',''))}</td><td>{t.get('confidence','')}%</td><td>{self._esc(', '.join(t.get('evidence',[])))}</td></tr>"
            parts.append(f"""<h3 class="collapsible" onclick="toggle(this)">Technologies ({len(techs)})</h3>
<div class="collapsible-content"><table><thead><tr><th>Technology</th><th>Confidence</th><th>Evidence</th></tr></thead><tbody>{rows}</tbody></table></div>""")

        # DNS
        dns = recon.get("dns",{})
        if dns:
            rows = ""
            for rtype, records in dns.items():
                if isinstance(records, list):
                    for r in records:
                        val = str(r) if not isinstance(r, dict) else json.dumps(r)
                        rows += f"<tr><td>{self._esc(rtype)}</td><td>{self._esc(val[:100])}</td></tr>"
            if rows:
                parts.append(f"""<h3 class="collapsible" onclick="toggle(this)">DNS Records</h3>
<div class="collapsible-content"><table><thead><tr><th>Type</th><th>Value</th></tr></thead><tbody>{rows}</tbody></table></div>""")

        # WHOIS
        whois = recon.get("whois",{})
        if whois:
            rows = ""
            for k,v in whois.items():
                if v and str(v) != "None":
                    rows += f"<tr><td>{self._esc(k.replace('_',' ').title())}</td><td>{self._esc(str(v)[:100])}</td></tr>"
            if rows:
                parts.append(f"""<h3 class="collapsible" onclick="toggle(this)">WHOIS Information</h3>
<div class="collapsible-content"><table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody>{rows}</tbody></table></div>""")

        # Headers
        hdrs = recon.get("headers",{})
        missing = hdrs.get("missing",[])
        present = hdrs.get("present",[])
        if missing or present:
            rows = ""
            for h in present:
                if isinstance(h, dict):
                    rows += f"<tr><td>{self._esc(h.get('header',''))}</td><td><span class='badge badge-info'>PRESENT</span></td><td>{self._esc(str(h.get('value',''))[:60])}</td></tr>"
            for h in missing:
                if isinstance(h, dict):
                    rows += f"<tr><td>{self._esc(h.get('header',''))}</td><td><span class='badge badge-{h.get('severity','LOW').lower()}'>MISSING</span></td><td>{self._esc(h.get('recommendation',''))}</td></tr>"
            parts.append(f"""<h3 class="collapsible" onclick="toggle(this)">Security Headers</h3>
<div class="collapsible-content"><table><thead><tr><th>Header</th><th>Status</th><th>Detail</th></tr></thead><tbody>{rows}</tbody></table></div>""")

        content = "\n".join(parts) if parts else "<p style='color:var(--dim)'>No reconnaissance data collected.</p>"
        return f'<div id="recon" class="section"><h2 class="section-title">🔍 Reconnaissance</h2>{content}</div>'

    def _crawler_section(self, crawler):
        parts = []
        urls = crawler.get("urls",[])
        if urls:
            rows = "".join(f"<tr><td>{self._esc(u)}</td></tr>" for u in urls)
            parts.append(f"""<h3 class="collapsible" onclick="toggle(this)">Crawled URLs ({len(urls)})</h3>
<div class="collapsible-content"><table><thead><tr><th>URL</th></tr></thead><tbody>{rows}</tbody></table></div>""")

        dirs = crawler.get("directories",[])
        if dirs:
            dirs_sorted = self._sort_directories(dirs)
            rows = ""
            for d in dirs_sorted:
                if isinstance(d, dict):
                    sc = d.get('status_code',0)
                    cls = 'vuln-row' if sc == 200 else ('warn-row' if sc == 403 else '')
                    rows += f"<tr class='{cls}'><td>{self._esc(d.get('path',''))}</td><td>{sc}</td><td>{self._esc(d.get('content_type','')[:40])}</td></tr>"
            parts.append(f"""<h3 class="collapsible" onclick="toggle(this)">Directories ({len(dirs)})</h3>
<div class="collapsible-content"><table><thead><tr><th>Path</th><th>Status</th><th>Type</th></tr></thead><tbody>{rows}</tbody></table></div>""")

        js_files = crawler.get("js_files",[])
        if js_files:
            rows = "".join(f"<tr><td>{self._esc(j)}</td></tr>" for j in js_files)
            parts.append(f"""<h3 class="collapsible" onclick="toggle(this)">JavaScript Files ({len(js_files)})</h3>
<div class="collapsible-content"><table><thead><tr><th>URL</th></tr></thead><tbody>{rows}</tbody></table></div>""")

        secrets = crawler.get("js_secrets",[])
        if secrets:
            rows = ""
            for s in secrets:
                if isinstance(s, dict):
                    rows += f"<tr><td><span class='badge badge-high'>{self._esc(s.get('type',''))}</span></td><td>{self._esc(s.get('value',''))}</td><td>{self._esc(s.get('file','').split('/')[-1])}</td></tr>"
            parts.append(f"""<h3 class="collapsible" onclick="toggle(this)">JS Secrets ({len(secrets)})</h3>
<div class="collapsible-content"><table><thead><tr><th>Type</th><th>Value</th><th>File</th></tr></thead><tbody>{rows}</tbody></table></div>""")

        params = crawler.get("parameters",[])
        if params:
            rows = ""
            for p in params:
                if isinstance(p, dict):
                    rows += f"<tr><td>{self._esc(p.get('name',''))}</td><td>{self._esc(', '.join(p.get('sources',[])))}</td><td>{self._esc(', '.join(p.get('methods',[])))}</td></tr>"
            parts.append(f"""<h3 class="collapsible" onclick="toggle(this)">Parameters ({len(params)})</h3>
<div class="collapsible-content"><table><thead><tr><th>Name</th><th>Source</th><th>Methods</th></tr></thead><tbody>{rows}</tbody></table></div>""")

        content = "\n".join(parts) if parts else "<p style='color:var(--dim)'>No crawl data collected.</p>"
        return f'<div id="crawler" class="section"><h2 class="section-title">🕷️ Crawling & Discovery</h2>{content}</div>'

    def _vuln_section(self, vulns):
        if not vulns:
            return '<div id="vulns" class="section"><h2 class="section-title">⚡ Vulnerabilities</h2><p style="color:var(--dim)">No vulnerabilities found.</p></div>'
        # Sort by severity
        order = {"CRITICAL":0,"HIGH":1,"MEDIUM":2,"LOW":3,"INFO":4}
        vulns_sorted = sorted(vulns, key=lambda v: order.get(v.get("severity","INFO").upper(), 5))
        cards = ""
        for i, v in enumerate(vulns_sorted):
            sev = v.get("severity","INFO").upper()
            badge_cls = f"badge-{sev.lower()}"
            detail = ""
            if v.get("detail"):
                detail += f"<p><span class='label'>Detail:</span> {self._esc(str(v['detail']))}</p>"
            if v.get("url"):
                detail += f"<p><span class='label'>URL:</span> {self._esc(str(v['url']))}</p>"
            if v.get("recommendation"):
                detail += f"<p><span class='label'>Fix:</span> {self._esc(str(v['recommendation']))}</p>"
            if v.get("source"):
                detail += f"<p><span class='label'>Source:</span> {self._esc(str(v['source']))}</p>"
            cards += f"""
<div class="vuln-card">
  <div class="vuln-header" onclick="this.nextElementSibling.classList.toggle('open')">
    <span class="title">{self._esc(v.get('title','Unknown'))}</span>
    <span class="badge {badge_cls}">{sev}</span>
  </div>
  <div class="vuln-body">{detail}</div>
</div>"""
        return f'<div id="vulns" class="section"><h2 class="section-title">⚡ Vulnerabilities ({len(vulns)})</h2>{cards}</div>'

    def _footer_section(self, meta):
        return f"""
<div class="footer">
  <p>⚡ Generated by Charlie_Recon v{self._esc(meta.get('version','1.0.0'))} | Author: {self._esc(meta.get('author','ImrulMir'))}</p>
  <p>Report generated: {self._esc(meta.get('scan_date',''))}</p>
  <p style="margin-top:8px;color:var(--dim)">⚠ This report is for authorized security testing only.</p>
</div>"""

    def _js(self, sev_counts):
        return f"""
function toggle(el){{el.classList.toggle('active');var c=el.nextElementSibling;c.style.display=c.style.display==='none'?'block':'none'}}
function expandAll(){{document.querySelectorAll('.collapsible-content').forEach(function(e){{e.style.display='block'}});document.querySelectorAll('.collapsible').forEach(function(e){{e.classList.add('active')}});document.querySelectorAll('.vuln-body').forEach(function(e){{e.classList.add('open')}})}}
function downloadPDF(){{expandAll();setTimeout(function(){{window.print()}},400)}}
document.querySelectorAll('.collapsible-content').forEach(function(e){{e.style.display='none'}});
(function(){{
  var canvas=document.getElementById('vulnChart');
  if(!canvas)return;
  var ctx=canvas.getContext('2d');
  var data=[{sev_counts.get('CRITICAL',0)},{sev_counts.get('HIGH',0)},{sev_counts.get('MEDIUM',0)},{sev_counts.get('LOW',0)},{sev_counts.get('INFO',0)}];
  var colors=['#ff0040','#ff4444','#ffaa00','#00d4ff','#888888'];
  var total=data.reduce(function(a,b){{return a+b}},0);
  if(total===0)return;
  var cx=100,cy=100,r=80,ir=50,start=-Math.PI/2;
  for(var i=0;i<data.length;i++){{
    if(data[i]===0)continue;
    var slice=2*Math.PI*data[i]/total;
    ctx.beginPath();ctx.moveTo(cx,cy);ctx.arc(cx,cy,r,start,start+slice);ctx.closePath();
    ctx.fillStyle=colors[i];ctx.fill();start+=slice;
  }}
  ctx.beginPath();ctx.arc(cx,cy,ir,0,2*Math.PI);ctx.fillStyle='#0a0a0f';ctx.fill();
  ctx.fillStyle='#00ff41';ctx.font='bold 20px Orbitron';ctx.textAlign='center';ctx.textBaseline='middle';
  ctx.fillText(total,cx,cy);
}})();"""

    @staticmethod
    def _esc(text):
        return html.escape(str(text)) if text else ""

    @staticmethod
    def _sort_subdomains(subs):
        """Sort subdomains by hacker priority: internal IPs, dev/staging/admin first."""
        INTERESTING_KEYWORDS = [
            'admin', 'dev', 'staging', 'test', 'beta', 'internal', 'intranet',
            'vpn', 'remote', 'jenkins', 'git', 'ci', 'deploy', 'debug',
            'api', 'dashboard', 'portal', 'login', 'auth', 'sso', 'db',
            'database', 'mysql', 'mongo', 'redis', 'elastic', 'grafana',
            'backup', 'old', 'legacy', 'phpmyadmin', 'cpanel', 'ftp',
            'mail', 'smtp', 'webmail', 'ssh', 'shell', 'console', 'monitor',
        ]

        def score(s):
            if not isinstance(s, dict):
                return 99
            ip = s.get('ip', '') or ''
            name = s.get('subdomain', '').lower()
            status = s.get('status', '')

            # Unresolved = lowest priority
            if status != 'active':
                return 90

            priority = 50  # default active

            # Internal IPs are gold — highest priority
            if ip.startswith('10.') or ip.startswith('192.168.') or ip.startswith('172.'):
                priority = 0
            # Interesting names
            for kw in INTERESTING_KEYWORDS:
                if kw in name:
                    priority = min(priority, 10)
                    break
            return priority

        return sorted(subs, key=score)

    @staticmethod
    def _subdomain_row_class(s):
        """Return CSS class for highlighting interesting subdomains."""
        if not isinstance(s, dict):
            return ''
        ip = s.get('ip', '') or ''
        name = s.get('subdomain', '').lower()
        if ip.startswith('10.') or ip.startswith('192.168.') or ip.startswith('172.'):
            return 'vuln-row'
        interesting = ['admin', 'dev', 'staging', 'test', 'beta', 'internal',
                       'vpn', 'jenkins', 'git', 'api', 'dashboard', 'login',
                       'db', 'backup', 'ftp', 'ssh', 'console', 'debug']
        for kw in interesting:
            if kw in name:
                return 'warn-row'
        return ''

    @staticmethod
    def _sort_directories(dirs):
        """Sort directories: 200 first (accessible), then 403 (forbidden but exists), then 301."""
        STATUS_PRIORITY = {200: 0, 403: 1, 405: 2, 301: 3, 302: 4}
        INTERESTING_PATHS = [
            'admin', 'config', 'backup', '.env', '.git', 'database', 'debug',
            'phpmyadmin', 'console', 'shell', 'upload', 'api', 'private',
            'secret', 'log', 'password', 'token', 'key', 'credential',
        ]

        def score(d):
            if not isinstance(d, dict):
                return 99
            sc = d.get('status_code', 999)
            path = d.get('path', '').lower()

            base = STATUS_PRIORITY.get(sc, 5)
            # Bump interesting paths higher within their status group
            for kw in INTERESTING_PATHS:
                if kw in path:
                    return base * 10  # Keep status priority but sort interesting first
            return base * 10 + 1

        return sorted(dirs, key=score)
