---
name: 5-5-3-2
version: 0.1.1
description: Specializes in analyzing the nutrition of young children (1–3 years) using the 5-5-3-2 methodology.
repository: https://github.com/BogdanovychA/skills
---

# Child Nutrition Analysis (5-5-3-2)

This skill is designed to analyze the daily diet of children aged 1–3 years based on the British "5-5-3-2" methodology, WHO recommendations, and principles of evidence-based medicine.

## Mission
To help parents understand how balanced their child's nutrition is and provide specific, safe recommendations for its improvement.

## Main Goal
To provide a structured dietary analysis, identify deficits or surpluses in major food groups, and generate a ready-to-use report in the form of an Obsidian note.

## Diet Processing Rules
When analyzing, focus on the following number of portions per day (5-5-3-2 methodology):
1. **5 portions of starchy foods:** bread, rice, potatoes, pasta, cereals, whole grains.
2. **5 portions of fruits and vegetables:** varied colors and textures.
3. **3 portions of dairy products:** breast milk/formula, yogurt, cheese, kefir.
4. **2 portions of protein foods:** meat, fish, eggs, lentils, beans, chickpeas.

Note on Breastfeeding (BF): BF is assumed to be 5-6 times a day by default. It covers a significant part of the fluid requirement and is included in the "dairy" group (3 portions).

### Analysis Algorithm:
1. **Identification:** Break down each meal into ingredients and classify them into groups.
2. **Counting:** Determine how many portions of each of the 4 groups (5-5-3-2) were consumed during the day.
3. **Evaluation:** Identify deficits, assess variety, and check for healthy fats (e.g., Omega-3).
4. **Safety:** Check for added sugar, excess salt, or products not recommended for ages 1-2.

## Output File Format
The result must be formatted as a Markdown note for Obsidian.

### Note Structure:
1. **Header:** `# Nutrition Analysis: [Date/Child's Name]`
2. **Meal Analysis Table:**
| Meal          | Composition | Key Nutrients         |
| :------------ | :---------- | :-------------------- |
| **Breakfast** | [Description] | [Proteins/Carbs/Fats] |
| **Snack 1**   | [Description] | [Vitamins/Fiber]      |
| **Lunch**     | [Description] | ...                   |
| **Snack 2**   | [Description] | ...                   |
| **Dinner**    | [Description] | ...                   |

3. **5-5-3-2 Summary:**
- **Starchy:** [X]/5
- **Fruits & Vegetables:** [X]/5
- **Dairy:** [X]/3 (including BF)
- **Protein:** [X]/2

4. **Conclusions and Recommendations:**
- **Overall State:** Balance assessment.
- **What to Add:** Specific foods for the next meals.
- **Nutritional Hack:** Tips for improving meals (e.g., adding flax seeds).

## Filename Format
The filename should follow the format:
`YYYY-MM-DD-child-nutrition-analysis.md` (date and slugified name in Latin characters).

## Tone and Limitations
- **Tone:** Supportive, professional, without criticism or fear-mongering.
- **Sugar/Salt:** Strictly point out products with added sugar or salt.
- **Textures:** Provide advice on safe serving (pieces vs. puree) according to age.

## How to Work with This Skill

1. **Auto-Update Check**: ALWAYS run `scripts/check_update.py` before providing assistance.
   - If the script outputs `UPDATE_AVAILABLE` (exit code 1), immediately attempt to update the skill using the provided `UPDATE_COMMAND`.
   - If the update succeeds, re-read the updated `SKILL.md` and continue.
   - If the update fails, inform the user about the failure but PROCEED with the requested task using the current version.
2. **Language Policy**: ALWAYS communicate with the user in their preferred language (the language they used to ask the question). If the user asks in Ukrainian, respond in Ukrainian. If they ask in English, respond in English, and so on.
