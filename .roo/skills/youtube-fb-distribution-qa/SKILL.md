---
name: youtube-fb-distribution-qa
description: Implement automated video/audio QC gates, Playwright 3-variant thumbnail generators, Telegram mobile approval bots, YouTube Data API v3 uploads with ES/PT/HI/AR metadata & SRT localization, and Facebook In-Stream burned-caption cuts. Use whenever implementing Tracks T07, T08, T09, or T11.
---

# QA Gate, Thumbnail Factory & Multi-Platform Distribution Skill

Use this skill when building `src/thumbnail/`, `src/qa/`, or `src/publish/`.

## 1. Automated QC Gate (`src/qa/validator.py`)
Never upload a video that fails any of these automated checks:
* **Video Stream (`ffprobe`):** Exact `3840x2160`, `60.00 fps` (`r_frame_rate=60/1`), `yuv420p`, `movflags=+faststart`.
* **Audio/Video Drift:** `abs(video_duration - audio_duration) <= 0.15s`.
* **Visual Defects:** FFmpeg `blackdetect=d=0.3:pix_th=0.10` (0 unexpected black frames) and `freezedetect=n=-60dB:d=4` (0 unintended freezes >4s).
* **Audio Defects:** Loudness `-14.0 ± 0.5 LUFS`, true peak `<= -1.0 dBTP`, no dead silence `>2.5s` via `silencedetect`.
* **Policy & Anti-Demonetization Lint:** Verifies `>=5` distinct visual templates across the episode, `100%` Fact-Audit pass, persistent source attributions, and verified `assets/licenses.json` entries.

## 2. 3-Variant Thumbnail Factory (`src/thumbnail/generator.py`)
* Render HTML/CSS/SVG templates in Headless Chromium (`playwright`) at `1920x1080` PNG (`device_scale_factor=1`).
* Produce 3 distinct high-CTR angles per episode for YouTube **Test & Compare**:
  - `variant_a_map.png`: High-contrast world map (emerald vs crimson extremes) + 2–3 word bold headline.
  - `variant_b_versus.png`: 2 iconic country flags + dramatic numerical delta.
  - `variant_c_outlier.png`: Dramatic chart spike + large tabular numeral + directional callout.
* Always generate a `mobile_preview.png` contact sheet scaled down to `168x94px` so the founder confirms legibility on small phone screens during Telegram review.

## 3. YouTube Data API v3 + 4-Language Localization (`src/publish/youtube.py`, `localizer.py`)
* Use resumable chunked uploads (`MediaFileUpload(..., resumable=True, chunksize=10*1024*1024)`) with exponential backoff.
* Schedule publication at optimal Tier-1 window (**14:00–16:00 UTC / 19:30–21:30 IST**).
* Inject exact chapter timestamps (`00:00`, `01:30`, ...) derived from `SceneGraph` into the description.
* Translate Title, Description, and time-coded `.srt` subtitles into **Spanish (`es`)**, **Portuguese (`pt-BR`)**, **Hindi (`hi`)**, and **Arabic (`ar`)** — preserving all numbers/units verbatim — and attach via `videos.update(part="localizations")` and `captions.insert`.

## 4. Facebook In-Stream Cut (`src/publish/facebook.py`)
* Re-wrap the YouTube master for muted mobile autoplay:
  - Prepend/accent a high-motion `0:00–0:03` visual hook.
  - Burn in crisp, high-contrast bottom captions (`.ass` subtitle style) using FFmpeg.
  - Upload via Facebook Graph API Video endpoint with chapter pauses aligned for In-Stream ad breaks.
