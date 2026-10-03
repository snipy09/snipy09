import os
import urllib.parse

width = 78

def make_box(title, rows, w=width):
    header = f"┌─ {title} " + "─" * (w - 4 - len(title)) + "┐"
    footer = "└" + "─" * (w - 2) + "┘"
    res = [header]
    for r in rows:
        pad = w - 4 - len(r)
        if pad < 0:
            raise ValueError(f"OVERFLOW in \"{title}\" (len={len(r)}, max={w-4}):\n  -> {r}")
        res.append(f"│ {r}" + " " * max(0, pad) + " │")
    res.append(footer)
    return "\n".join(res)

# 1. Neofetch Box
term_logo = [
    "  .------------.  ",
    "  | .--------. |  ",
    "  | | >_ dev | |  ",
    "  | | active | |  ",
    "  | '--------' |  ",
    "  '------------'  ",
    "     /      \\     ",
    "    /________\\    "
]

specs = [
    "USER      :: Sajal Kumar Mishra (@snipy09)",
    "ROLE      :: Systems Architect & Full-Stack Engineer",
    "FOCUS     :: High-Throughput Automation & SaaS",
    "FLAGSHIP  :: Nomadic [Universal Career OS]",
    "DOMAINS   :: Full-Stack, DOM Automation, Desktop Apps",
    "UPTIME    :: 24/7 [Shipping resilient code]",
    "PALETTE   :: Dark (#09090b) + Powder Blue (#bae2fd)",
    "LOCATION  :: India (UTC+05:30)"
]

combined_neofetch = []
for i in range(max(len(term_logo), len(specs))):
    l = term_logo[i] if i < len(term_logo) else " " * 18
    r = specs[i] if i < len(specs) else ""
    combined_neofetch.append(f"{l}│ {r}")

box_neofetch = make_box("SYS_TELEMETRY // NEOFETCH.SH", combined_neofetch, width)

# 2. Stack Box
tech_stack = [
    "LANGUAGES   :: TypeScript, JavaScript, Python 3.11, SQL, HTML5/CSS3",
    "FRONTEND    :: React 18, Next.js, TailwindCSS, Vite, Zustand, Radix UI",
    "BACKEND     :: Node.js, Express, FastAPI, RESTful APIs, WebSockets",
    "DESKTOP/APP :: Electron, Windows Authenticode, Chrome DevTools Protocol",
    "DATABASE    :: PostgreSQL, Supabase (RLS & Realtime), Redis, Prisma",
    "INFRA/TOOLS :: Git/GitHub, Docker, Vercel, Turborepo, Bash, Linux"
]
box_stack = make_box("MODULES_LOADED // TECH_STACK", tech_stack, width)

# 3. Metrics Box
skills_meter = [
    "Frontend & UI Systems     [████████████████████░░░░] 85%",
    "Full-Stack & API Design   [██████████████████████░░] 92%",
    "DOM & Form Automation     [████████████████████████] 98%",
    "Desktop & Native Run      [██████████████████░░░░░░] 78%",
    "Database & Schema Design  [████████████████████░░░░] 84%",
    "Deterministic CI/CD       [████████████████████░░░░] 86%"
]
box_metrics = make_box("COMPUTE_METRICS // PROFICIENCY_INDEX", skills_meter, width)

# 4. Projects Box
featured_projects = [
    "01. NOMADIC // Universal Career OS",
    "    ├── Deployment : https://nomadicai.vercel.app",
    "    ├── Stack      : React 18, Supabase RLS, Electron Desktop (Signed)",
    "    ├── Core Engine: OmniForm DOM Solver (>95% accuracy) & AI Pilot",
    "    └── Features   : Sub-30ms pagination, 428+ Question Bank, Tier sync",
    "",
    "02. DCUBOID CRM // Enterprise Sales & Operations Cockpit",
    "    ├── Target     : Pipeline telemetry & high-efficiency execution",
    "    └── Stack      : 3-column cockpit, dark telemetry, low-latency sync",
    "",
    "03. HIGH-THROUGHPUT AUTOMATION HARNESSES",
    "    ├── Targets    : Ashby, Greenhouse, Lever, Internshala scrapers",
    "    └── Mechanics  : Prototype setter injection & CDP session hooks"
]
box_projects = make_box("OPERATIONAL_BUILDS // REPOSITORIES", featured_projects, width)

# 5. Core Paradigms Box
paradigms = [
    "[01] DETERMINISTIC AUTOMATION :: End-to-end perception loops with fallback",
    "                                 arbitration and zero hardcoded fragility.",
    "[02] RESILIENT CLIENT STATE  :: Sub-30ms query budgets, optimized local",
    "                                 caching, and instant optimistic UI sync.",
    "[03] MONOTONE DESIGN LOGIC   :: High-contrast, zero-noise dark interfaces",
    "                                 with subtle powder-blue accents only.",
    "[04] SYSTEM INTEGRITY        :: Strict RLS policies, Authenticode signing,",
    "                                 and robust server-side tier validation."
]
box_paradigms = make_box("SYSTEM_ARCHITECTURE // CORE_PARADIGMS", paradigms, width)

# 6. Ping Box
contact_block = [
    "PING PROTOCOLS ::",
    "  EMAIL    -> sajalmishra0906@gmail.com",
    "  GITHUB   -> https://github.com/snipy09",
    "  LINKEDIN -> https://linkedin.com/in/sajal-mishra",
    "  LIVE APP -> https://nomadicai.vercel.app",
    "",
    "TERMINAL INVOCATIONS ::",
    "  $ git clone https://github.com/snipy09/<repository>.git",
    "  $ curl -sL https://api.github.com/users/snipy09 | jq '.public_repos'"
]
box_contact = make_box("COMM_CHANNELS // CONNECT", contact_block, width)

footer_box = [
    "Status  :: Process completed with exit code 0x00 [OK]",
    "Session :: snipy09-core @ workstation [active]",
    "Keymap  :: [Ctrl+C] to interrupt | [Enter] to execute",
    "Hash    :: 0x8F3C...A4B1"
]
box_footer = make_box("PROCESS_TERMINATION // EXIT 0", footer_box, width)

# Typing SVG params
typing_lines = [
    "snipy09@workstation:~$ whoami --verbose",
    "> Sajal Kumar Mishra // Systems & Full-Stack Architect",
    "snipy09@workstation:~$ launch --product=Nomadic",
    "> Career OS online: OmniForm DOM Solver + AI Pilot active",
    "snipy09@workstation:~$ run --telemetry",
    "> Sub-30ms query latency | 98.4% DOM automation accuracy",
    "snipy09@workstation:~$ status",
    "> Shipping deterministic, zero-noise engineering 24/7."
]
typing_query = urllib.parse.quote(";".join(typing_lines))
typing_url = f"https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=15&duration=2800&pause=900&color=bae2fd&background=09090B00&center=true&vCenter=true&width=750&lines={typing_query}"

readme_content = f"""<div align="center">

<img src="./assets/header.svg" alt="snipy09 Terminal Banner" width="100%" />

<br/><br/>

<a href="https://github.com/snipy09">
  <img src="{typing_url}" alt="Terminal Typing Telemetry" />
</a>

<br/>

<img src="https://komarev.com/ghpvc/?username=snipy09&label=PROFILE%20VIEWS&color=0284c7&style=for-the-badge" alt="views" />
<img src="https://img.shields.io/github/followers/snipy09?style=for-the-badge&logo=github&label=FOLLOWERS&color=0284c7" alt="followers" />
<img src="https://img.shields.io/badge/STATUS-OPERATIONAL-0284c7?style=for-the-badge" alt="status" />

</div>

```text
{box_neofetch}
```

```text
{box_stack}
```

```text
{box_metrics}
```

```text
{box_projects}
```

```text
{box_paradigms}
```

<div align="center">

### ─── [ SYSTEM_TELEMETRY // GITHUB_METRICS ] ───

<br/>

<img src="https://github-readme-stats.vercel.app/api?username=snipy09&show_icons=true&theme=transparent&title_color=bae2fd&text_color=e2e8f0&icon_color=0284c7&border_color=1e293b&hide_border=false&count_private=true&include_all_commits=true" alt="Sajal's GitHub Stats" width="48%" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=snipy09&layout=compact&theme=transparent&title_color=bae2fd&text_color=e2e8f0&icon_color=0284c7&border_color=1e293b&hide_border=false" alt="Top Languages" width="48%" />

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=snipy09&theme=transparent&background=09090B&ring=0284c7&fire=bae2fd&currStreakLabel=bae2fd&stroke=1e293b&dates=94a3b8" alt="GitHub Streak" width="97%" />

</div>

```text
{box_contact}
```

```text
{box_footer}
```
"""

out_path = "C:/Users/sajal/snipy09/README.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(readme_content.strip() + "\n")

print(f"SUCCESS: Written to {out_path}")
