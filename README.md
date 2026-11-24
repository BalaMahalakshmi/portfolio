# Bala Mahalakshmi S. — Portfolio

A personal portfolio for **Bala Mahalakshmi S.** — AI Product Developer / AI & ML Engineer — built as a fast, single-file static website with a distinctive **Neural Bloom** (violet/pink) visual identity.

## Highlights

- **Neural Bloom design** — deep plum-dark base, violet→magenta→pink accents, glass surfaces, subtle grid, and a neural signal canvas.
- **Signature Resume Capsule** — creative, accessible download button with gradient border, shimmer scan, icon micro-interaction, and real PDF download.
- **Merged content** — combines current portfolio content, resume details, and newly added projects.
- **Responsive & accessible** — semantic sections, skip link, visible focus, keyboard-friendly dialog/navigation, AA-minded contrast, and `prefers-reduced-motion` support.
- **Interactive** — scroll progress, reveal animations, project filters, project detail dialog, mobile nav, theme toggle, and download toast.

## Files

| File | Purpose |
| --- | --- |
| `porti.html` | The canonical portfolio site. Self-contained HTML/CSS/JS — deploy as-is. |
| `Maha_ai_resume_trainer.pdf` | Resume file used by all Resume Capsule/download actions. |

## Run locally

Open `porti.html` directly, or serve the folder:

```bash
python -m http.server 8000
# then open http://localhost:8000/porti.html
```

## Deploy

`porti.html` is static: push it to GitHub and enable **Pages**, or drag it into Netlify Drop / Cloudflare Pages. No build step or dependencies.

## Before publishing

1. **Verify merged details** — experience dates/institution details that were unclear in extraction are marked as placeholders/TODOs in content; update them as needed.
2. **Profile links** — LinkedIn and GitHub are wired to your provided URLs; update if they change.
3. **Resume filename** — resume downloads currently point to `Maha_ai_resume_trainer.pdf`. Rename/copy to a cleaner name if you prefer, and update links.

## Design system

| Token | Dark | Light |
| --- | --- | --- |
| Background | `#0B0814` / `#151024` | `#FBF8FF` / `#F3EEFF` |
| Text | `#F7F4FF` | `#1A102B` |
| Muted | `#B8AECF` | `#55466E` |
| Violet | `#8B5CF6` | `#7C3AED` |
| Pink | `#EC4899` | `#DB2777` |
| Bloom | `#D946EF` | `#C026D3` |
| Success | `#34D399` | `#059669` |

Typography: **Space Grotesk** (display), **Inter** (body), **JetBrains Mono** (labels/data).

## Content notes

- **Name:** Bala Mahalakshmi S.
- **Merged experience:** WrenchWise, Wynsync, InLighnX, TM Innovations, Rounds Edge, Main Flow.
- **Merged projects:** AI Coding Agent with Docker Sandbox, LearnOS, Medical Image Classification, Fake News Detection, AI Resume Analyser, Face Recognition Attendance, Python Web Apps/APIs, AI Legacy Data Extraction, Data Analysis Dashboards.
- **Recognition:** Kodaikanal Solar Observatory 1st Prize, corporate hackathon participation, selected certifications.