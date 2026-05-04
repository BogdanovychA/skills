# AI Agent Skills Repository

![Made in Ukraine](https://img.shields.io/badge/Made%20in-Ukraine-blue?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjgwMCI%2BCjxyZWN0IHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjgwMCIgZmlsbD0iIzAwNTdCNyIvPgo8cmVjdCB3aWR0aD0iMTIwMCIgaGVpZ2h0PSI0MDAiIHk9IjQwMCIgZmlsbD0iI0ZGRDcwMCIvPgo8L3N2Zz4%3D)

This repository contains a set of specialized skills for AI agents.

## Prerequisites

Before using these skills, ensure you have **Node.js** installed on your system. We recommend using [nvm (Node Version Manager)](https://github.com/nvm-sh/nvm) for installation.

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

### 4. Child Nutrition Analysis (5-5-3-2)
Specializes in analyzing the nutrition of young children (1–3 years) using the 5-5-3-2 methodology. It helps parents evaluate daily diets based on British standards and WHO recommendations, generating structured reports for Obsidian.

**Installation Command:**
```bash
npx skills add BogdanovychA/skills --skill 5-5-3-2
```
