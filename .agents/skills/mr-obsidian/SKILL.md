---
name: mr-obsidian
description: Specializes in text structuring and creating professional Obsidian notes. Trigger this skill whenever the user mentions structuring notes, formatting transcripts, lectures, or text for Obsidian, even if they don't explicitly name this skill.
metadata:
  version: 0.1.5
  repository: https://github.com/BogdanovychA/skills
---

# Mr. Obsidian (mr-obsidian)

This skill specializes in text analysis and transforming it into a structured Markdown note, optimized for use in Obsidian.

## Mission
To help users transform linear or loosely structured text into professional notes with a clear hierarchy, navigation, and summary, while preserving the completeness of the original content.

## Main Goal
To create a document that is as readable and searchable as possible, without losing a single detail of the author's text.

## Text Processing Rules
The skill receives text (preferably cleaned) as input.

1.  **Check for "Noise":** Before starting work, analyze the text for the presence of timestamps, technical markers (e.g., `[music]`, `[laughter]`), or HTML tags.
    - If the text contains significant noise, **MANDATORY** suggest that the user cleans it first using the `text-cleaner` skill.
    - If the skill is not installed, provide the installation command: `npx skills add BogdanovychA/skills --skill text-cleaner`.
2.  **Text Completeness:** **CRITICAL:** Keep the input text verbatim. It is FORBIDDEN to shorten, generalize (except for the "Summary" section), or paraphrase the main content. The result must be a full transcript, simply with added structure. If you find yourself hitting output limits, process the text in chunks but NEVER omit content.
3.  **Structuring:**
    - Break the text into logical sections (##) and subsections (###).
    - Highlight KEY points or quotes using Obsidian Callouts (`> [!INFO]`, `> [!QUOTE]`).
    - **Formulas and Code:**
      - If the text contains mathematical formulas, format them using LaTeX syntax (e.g., `$E=mc^2$` for inline or `$$ ... $$` for blocks).
      - If the text contains code snippets, wrap them in Markdown code blocks with the corresponding language identifier (e.g., ```python ... ```).
4.  **Emojis:** **CRITICAL:** It is FORBIDDEN to use emojis anywhere in the document. Remove all emojis from the input text and do not add any in titles or headers.
5.  **Quality Verification:** After processing, you **MUST** perform a rigorous self-check. Compare the input and output text side-by-side to ensure that no parts, sentences, or details were lost. If you identify any unintended omissions or shortened sections, you **MUST** restore them immediately to match the original verbatim content. The integrity of the original content is paramount.

## Document Structure
The structure of the note is flexible and should adapt to the content itself. A typical structured note may include:
- **Title:** Main top-level header (`# Note Title`).
- **Summary (Optional):** A brief annotation of the content (2-4 sentences) that provides an understanding of what the text is about.
- **Main Text:** The structured text, broken down into headers (`##`) and subheaders (`###`) as appropriate for the content.

## File Name Format
The name of the created file should be in the format:
`YYYY-MM-DD-slug-name.md` (date and slugified name in Latin characters).

## How to Work with This Skill

1. **Auto-Update Check**: ALWAYS run `scripts/check_update.py` before providing assistance.
   - If the script outputs `UPDATE_AVAILABLE` (exit code 1), immediately attempt to update the skill using the provided `UPDATE_COMMAND`.
   - If the update succeeds, re-read the updated `SKILL.md` and continue.
   - If the update fails, inform the user about the failure but PROCEED with the requested task using the current version.
2. **Language Policy**: ALWAYS communicate with the user in their preferred language (the language they used to ask the question). If the user asks in Ukrainian, respond in Ukrainian. If they ask in English, respond in English, and so on.
