import urllib.parse

typing_lines = [
    "snipy09@workstation:~$ whoami --role",
    "> Systems Architect & Full-Stack Builder",
    "snipy09@workstation:~$ launch --product=Nomadic",
    "> Career OS active: OmniForm DOM Solver + AI Pilot loop online",
    "snipy09@workstation:~$ bench --latency",
    "> Sub-30ms client query state synced | 98.4% automation precision",
    "snipy09@workstation:~$ status",
    "> Shipping deterministic, high-throughput systems 24/7."
]
typing_query = urllib.parse.quote(";".join(typing_lines))
typing_url = f"https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=15&duration=2800&pause=900&color=bae2fd&background=09090B00&center=true&vCenter=true&width=750&lines={typing_query}"

readme_content = f"""<div align="center">

<img src="./assets/header.svg" alt="snipy09 System Header" width="100%" />

<br/><br/>

<a href="https://github.com/snipy09">
  <img src="{typing_url}" alt="Terminal Telemetry" />
</a>

<br/>

<img src="./assets/engine.svg" alt="Engine & Capability Telemetry" width="100%" />

<br/><br/>

### ─── [ SYSTEM_TELEMETRY // GITHUB_METRICS ] ───

<br/>

<img src="https://github-readme-stats.vercel.app/api?username=snipy09&show_icons=true&theme=transparent&title_color=bae2fd&text_color=cbd5e1&icon_color=0284c7&border_color=1e293b&hide_border=false&count_private=true&include_all_commits=true" alt="GitHub Stats" width="48%" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=snipy09&layout=compact&theme=transparent&title_color=bae2fd&text_color=cbd5e1&icon_color=0284c7&border_color=1e293b&hide_border=false" alt="Top Languages" width="48%" />

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=snipy09&theme=transparent&background=09090B&ring=0284c7&fire=bae2fd&currStreakLabel=bae2fd&stroke=1e293b&dates=94a3b8" alt="GitHub Streak" width="97%" />

<br/><br/>

### ─── [ COMM_CHANNELS // CONNECT ] ───

<br/>

<a href="mailto:sajalmishra0906@gmail.com"><img src="https://img.shields.io/badge/EMAIL-sajalmishra0906%40gmail.com-09090b?style=for-the-badge&logo=gmail&logoColor=bae2fd&labelColor=09090b&color=1e293b" alt="Email" /></a>
<a href="https://nomadicai.vercel.app"><img src="https://img.shields.io/badge/LIVE_APP-NOMADIC_OS-09090b?style=for-the-badge&logo=vercel&logoColor=bae2fd&labelColor=09090b&color=0284c7" alt="Nomadic" /></a>
<a href="https://github.com/snipy09"><img src="https://img.shields.io/badge/GITHUB-snipy09-09090b?style=for-the-badge&logo=github&logoColor=bae2fd&labelColor=09090b&color=1e293b" alt="GitHub" /></a>

<br/><br/>

```text
[PROCESS COMPLETED // EXIT 0x00] ──────────────────────────────────────────────
Session :: snipy09-core @ workstation [active] | 24/7 continuous ops
──────────────────────────────────────────────────────────────────────────────
```

</div>
"""

out_path = "C:/Users/sajal/snipy09/README.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(readme_content.strip() + "\n")

print(f"SUCCESS: Written refined animated README to {out_path}")
