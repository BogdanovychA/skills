---
name: transcript-downloader
description: Download YouTube transcripts in various languages using the mr-transcript library. Trigger this skill whenever the user provides a YouTube link and wants to download or save the transcript/subtitles.
metadata:
  version: 0.1.3
  repository: https://github.com/BogdanovychA/skills
---

# Transcript Downloader (transcript-downloader)

This skill enables you to download and save YouTube transcripts to your local disk. It uses the `mr-transcript` Python library to fetch available languages and download the text.

## Workflow

1.  **Identify URL**: Extract the YouTube URL from the user's message.
2.  **List Languages**: Run the `scripts/downloader.py` script with the `--list` flag and the URL to get a list of available subtitle languages.
3.  **User Selection**: Present the list of languages (e.g., "en: English", "uk: Ukrainian") to the user and ask which one they would like to download.
4.  **Download**: Once the user chooses a language, run the `scripts/downloader.py` script with the `--download` flag, the URL, the chosen language code, and an optional output filename.
5.  **Confirmation**: Confirm to the user that the transcript has been saved and provide the file path.

## Scripts

### `scripts/downloader.py`
This script handles the interaction with the `mr-transcript` library. It automatically manages its dependencies by trying to use `uv` first, and falling back to a local virtual environment (`.venv`) if `uv` is not available.

**Usage:**
- `python3 scripts/downloader.py --list <URL>`
- `python3 scripts/downloader.py --download <URL> --lang <LANG_CODE> [--output <FILENAME>]`

*Note: You can also use `uv run --with mr-transcript python3 scripts/downloader.py ...` directly if you know `uv` is available, as it is slightly faster.*

## Example

**User:** "Download the transcript for this video: https://www.youtube.com/watch?v=dQw4w9WgXcQ"
**Agent:** (Runs list command, shows languages) "Available languages: en (English), de-DE (German), ja (Japanese), pt-BR (Portuguese), es-419 (Spanish). Which language should I choose?"
**User:** "en"
**Agent:** (Runs download command) "Transcript saved to file `dQw4w9WgXcQ_en.txt`."

## How to Work with This Skill

1. **Auto-Update Check**: ALWAYS run `scripts/check_update.py` before providing assistance.
   - If the script outputs `UPDATE_AVAILABLE` (exit code 1), immediately attempt to update the skill using the provided `UPDATE_COMMAND`.
   - If the update succeeds, re-read the updated `SKILL.md` and continue.
   - If the update fails, inform the user about the failure but PROCEED with the requested task using the current version.
2. **Language Policy**: Respond to the user in the same language they used to ask their question to ensure a natural and clear communication flow.

## Important Notes

- Requires **Python >= 3.10**.
- Requires **youtube-transcript-api >= 1.1.0**
- Requires **mr-transcript >= 0.1.2**
- Always check if the library is installed (`pip install mr-transcript` or `uv add mr-transcript`).
