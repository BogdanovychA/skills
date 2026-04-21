# AI Agent Skills Repository

This repository contains a set of specialized skills for AI agents.

## Available Skills

### 1. Mr. Obsidian (mr-obsidian)
Specializes in transforming raw text into structured notes optimized for Obsidian. This skill helps agents automatically generate a table of contents (TOC), summaries, and logical sections while strictly preserving the completeness of the original text.

**Installation Command:**
```bash
npx skills add BogdanovychA/skills --skill mr-obsidian
```

### 2. Text Cleaner (text-cleaner)
Allows agents to efficiently clean text of "technical noise": timestamps, HTML tags, technical comments, and emojis. It is ideal for preparing "dirty" transcripts for further analysis or structuring.

**Installation Command:**
```bash
npx skills add BogdanovychA/skills --skill text-cleaner
```

### 3. Transcript Downloader (transcript-downloader)
Enables agents to download and save YouTube transcripts to the local disk. By default, it saves the transcript in the project root directory, unless specified otherwise by the user.

**Installation Command:**
```bash
npx skills add BogdanovychA/skills --skill transcript-downloader
```
