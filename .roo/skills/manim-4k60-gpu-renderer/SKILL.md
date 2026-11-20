---
name: manim-4k60-gpu-renderer
description: Engineer high-throughput 4K 60FPS GPU rendering pipelines with Manim OpenGL / ModernGL / Skia-PyCairo, atomic scene parallelism, static layer caching, WhisperX timestamp animation binding, and direct FFmpeg NVENC piping. Use whenever implementing Track T06 (REN-01..REN-09) or optimizing video render performance.
---

# 4K 60FPS GPU Rendering & Visual Template Skill

Use this skill when building or optimizing `src/render/` engines, templates, compositors, or FFmpeg export presets.

## Performance Architecture Rules
1. **Atomic Scene Splitting:** Never render a 10–18 min video as one monolithic process. Split into 25–45 independent scenes (`15–35s` each), keyed by `hash(scene_spec + audio_duration)` for crash-resumable caching.
2. **Zero Uncompressed PNG Sequences:** Stream `3840x2160` RGB24 frames directly over `stdin` pipe into FFmpeg hardware NVENC:
   ```bash
   ffmpeg -y -f rawvideo -pix_fmt rgb24 -s 3840x2160 -r 60 -i pipe:0 \
          -c:v hevc_nvenc -preset p5 -rc vbr -cq 18 -b:v 35M -maxrate 55M \
          -pix_fmt yuv420p -movflags +faststart scene_xxx.mp4
   ```
   (Fallback to `libx264 -preset fast -crf 18` ONLY in CPU CI test runs at `640x360`.)
3. **Static Layer Pre-Baking:** Pre-rasterize static dark-grid backgrounds, Natural Earth world polygons, and country flag sprites into memory/VRAM textures once per worker instead of re-parsing SVGs every frame.
4. **Audio-Driven Timing:** Read exact `duration_ms` and WhisperX word timestamps (`start_ms`, `end_ms`) for each scene so country highlights, counter rolls, and camera zooms trigger on the exact spoken word.

## 4K Documentary Design System Guardrails
* **Canvas & Safe Margins:** `3840x2160` (16:9). Keep all critical text inside a `5%` safe margin (`192px` horizontal, `108px` vertical) to avoid YouTube player overlays and TV overscan.
* **Mobile Legibility Rule:** Minimum label font size = `48px` at 4K (equivalent to `12px` at 540p mobile). Use tabular lining figures (`Inter` / `JetBrains Mono` / `IBM Plex Sans`) so animated counters never jitter horizontally.
* **Colorblind-Safe Dark Theme:** Deep charcoal/slate canvas (`#0B0F19`), muted grid (`#1E293B`), crisp off-white primary ink (`#F8FAFC`), high-contrast amber/cyan/emerald/coral accents (`#38BDF8`, `#10B981`, `#F59E0B`, `#F43F5E`).
* **Mandatory Attribution Footer:** Every data scene renders a subtle bottom-left source string (`Source: <Org> (<Year>) · <Unit>`).

## 8 Core Templates
1. `BarChartRace` — Interpolated rank easing (`ease_in_out_cubic`), flag badges, rolling year.
2. `WorldChoroplethMap` — Natural Earth 1:50m GeoJSON, smooth camera pan/zoom, animated legend.
3. `SpotlightCountryCard` — Hero flag, rank pill, 3 animated counters, sparkline.
4. `ChapterTitleCard` — 3-second kinetic act transition with chapter number.
5. `DualSplitComparison` — Side-by-side split (e.g., Nominal vs PPP) with delta callout.
6. `HistoricalLineRace` — Multi-country line plot with shock event pins (2008, 2020).
7. `AnimatedBubbleScatter` — X/Y correlation with population bubble radius & trails.
8. `DistributionHistogram` — Global percentile curve with viewer callout marker.

## Verification Checklist
- [ ] Every template includes a fast low-res smoke test (`640x360`, 10fps, 2s) in `pytest` verifying non-empty frame output and zero bounding-box label collisions.
- [ ] Concatenated master verified by `ffprobe`: exact `3840x2160`, `60.00 fps`, `yuv420p`, `0ms` AV drift.
