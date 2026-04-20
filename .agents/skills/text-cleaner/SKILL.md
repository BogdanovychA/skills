---
name: text-cleaner
version: 0.0.1
description: Specializes in cleaning text from technical noise (timestamps, comments like [laughter], [music], HTML tags) while preserving the original text unchanged. Outputs clean text in Markdown format with minimal sectioning.
repository: https://github.com/BogdanovychA/skills
---

# Text Cleaner (text-cleaner)

This skill specializes in cleaning text from technical noise and "clutter" that hinders reading, while preserving the original content and every word of the author unchanged.

## Mission
To help users get clean, readable text from "dirty" transcripts, subtitles, or text copied from web pages. **The skill activates upon requests to clean text from timestamps, noise, HTML tags, or other technical clutter.**

## Main Goal
To remove everything that is not part of the speech or the main content, without resorting to shortening, paraphrasing, or summarizing.

## Language Policy
**CRITICAL:** Always communicate with the user in the language they used to ask the question. If the request is in Ukrainian — reply in Ukrainian. If in English — reply in English.

## Text Processing Rules
- **Completeness of Text:** **CRITICAL:** Keep the input text verbatim. It is FORBIDDEN to shorten, generalize, or throw out any sentences. Every word of the author must remain in place.
- **Noise Cleaning:**
    - Remove timestamps in any format (e.g., `00:00:10`, `[12:34]`, `12:34.567`).
    - Remove comments about background sounds or non-verbal actions (e.g., `[laughter]`, `[music]`, `(laughs)`, `[applause]`, `[сміх]`, `[музика]`).
    - Remove HTML tags and unnecessary attributes (e.g., `<div>`, `<p class="...">`, `&nbsp;`).
    - Remove promotional inserts if they are clearly technical (e.g., "Subscribe to the channel", "Subscribe", if it's a system subtitle insert).
    - Remove all emojis.
- **Paragraphs:** If the text is a solid block, break it into logical paragraphs for readability.
- **Minimal Formatting:**
    - Output the result in Markdown format (`.md`).
    - Use a minimal number of headers (`##`) only to separate very large blocks of text by meaning, if logically necessary. In other cases, paragraph separation is sufficient.
    - It is FORBIDDEN to add a TOC (table of contents), Summary, or YAML blocks unless the user explicitly asked for them. The output should be just clean text.

## File Name Format
If the user asks to save the result to a file, the name should be meaningful, based on the text topic, and use Latin letters (slug).
Format: `YYYY-MM-DD-slug-name.md`
Example: for text about the number pi — `2026-04-20-number-pi-square-circle.md`

## Skill Update
Before starting work, the skill MUST run the `scripts/check_update.py` script to check the relevance of the version.
If a new version is available, suggest that the user updates.
