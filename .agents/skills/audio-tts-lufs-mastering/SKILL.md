---
name: audio-tts-lufs-mastering
description: Build zero-marginal-cost GPU TTS narration pipelines (Kokoro-82M / Chatterbox / F5-TTS), phonetic pronunciation lexicons, WhisperX forced word-level alignment, and FFmpeg BGM sidechain ducking + SFX sync + broadcast -14 LUFS mastering. Use whenever implementing Track T05 (AUD-01..AUD-05).
---

# GPU TTS, Forced Alignment & Broadcast Audio Mastering Skill

Use this skill when building or debugging `src/audio/` narration synthesis, alignment, or FFmpeg audio mixing.

## Core Standards
1. **Zero-Marginal-Cost GPU TTS:** Default to self-hosted local GPU models (**Kokoro-82M**, **Chatterbox TTS**, or **F5-TTS**) behind a clean `TTSProvider` protocol so upgrading to ElevenLabs later is a one-line config switch.
2. **Pronunciation Lexicon (`config/pronunciation.json`):** Pre-process narration text before TTS synthesis (while keeping original clean text for SRT captions!) so acronyms, currencies, and tricky country names sound natural:
   - `OECD` → `"O-E-C-D"`, `PPP` → `"P-P-P"`, `Gini` → `"Jee-nee"`, `CAGR` → `"compound annual growth rate"`, `CHF` → `"Swiss francs"`, `UAE` → `"U-A-E"`.
3. **Forced Word-Level Alignment (`WhisperX` / `stable-ts`):**
   - Run forced alignment per scene WAV (`48kHz`, mono, 16-bit PCM).
   - Persist `data/episodes/<ep>/audio/<scene_id>.words.json` containing `[{"word": "Switzerland", "start_ms": 4120, "end_ms": 4780}]`.
   - Downstream `src/render/` reads these exact timestamps to trigger visual spotlights and counter animations.
4. **3-Track Documentary Sound Design (`src/audio/mixer.py`):**
   - **Track 1 (Voice):** High-pass filter at `80 Hz`, gentle de-essing/compression, target speech level before mix.
   - **Track 2 (Ambient BGM):** Loopable licensed documentary stem ducked smoothly beneath narration via FFmpeg `sidechaincompress` (`threshold=0.02:ratio=6:attack=40:release=450`), sitting around `-24 dB` under active voice and swelling gently on chapter transitions.
   - **Track 3 (Micro-SFX):** Crisp `whoosh`, `pop`, `tick`, `riser`, `counter_roll` inserted at exact `adelay` millisecond offsets derived from scene animation events.
5. **Broadcast Loudness Mastering (YouTube & Facebook Standard):**
   - Two-pass FFmpeg `loudnorm` filter targeting:
     - Integrated Loudness (`I`): **`-14.0 LUFS`** (`±0.5 LUFS`)
     - True Peak (`TP`): **`-1.0 dBTP`** (hard ceiling)
     - Loudness Range (`LRA`): **`7.0 LU`**
   - Output `48 kHz` stereo AAC (`192–256 kbps`) for master muxing.

## Verification Checklist
- [ ] `ffprobe` / `loudnorm` pass-1 audit confirms `-14.0 ± 0.5 LUFS` and `<= -1.0 dBTP`.
- [ ] Zero dead silence gaps longer than `2.5s` inside narration tracks.
- [ ] Every BGM & SFX asset used is registered with its commercial license in `assets/licenses.json`.
