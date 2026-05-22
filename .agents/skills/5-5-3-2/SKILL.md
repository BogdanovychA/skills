---
name: 5-5-3-2
description: Specializes in analyzing the nutrition of young children (1–3 years) using the 5-5-3-2 methodology. ALWAYS use this skill if the user asks to analyze a child's diet, daily food intake, meal plans, or requests nutritional advice for toddlers (1-3 years), even if they do not explicitly mention the "5-5-3-2" methodology.
metadata:
  version: 0.1.3
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

## Example

**Input:**
User: "My 1.5 year old daughter Emma today ate:
- Breakfast: oatmeal with banana and butter, glass of milk
- Lunch: chicken soup with potatoes, carrot and bread
- Snack: apple slices
- Dinner: boiled fish, pasta, broccoli
Please analyze Emma's diet."

**Output:**
(Saved to `2026-05-22-emma-nutrition-analysis.md`):
```markdown
# Nutrition Analysis: Emma (2026-05-22)

| Meal          | Composition | Key Nutrients         |
| :------------ | :---------- | :-------------------- |
| **Breakfast** | Oatmeal with banana, butter, milk | Complex carbs, potassium, healthy fats, calcium |
| **Lunch**     | Chicken soup (chicken, potatoes, carrot), bread | Proteins, vitamin A, complex carbs |
| **Snack**     | Apple slices | Fiber, vitamins |
| **Dinner**    | Boiled fish, pasta, broccoli | Omega-3 fatty acids, proteins, carbs, fiber |

### 5-5-3-2 Summary:
- **Starchy:** 3/5 (oatmeal, bread, pasta)
- **Fruits & Vegetables:** 4/5 (banana, carrot, apple, broccoli)
- **Dairy:** 1/3 (milk)
- **Protein:** 2/2 (chicken, fish)

### Conclusions and Recommendations:
- **Overall State:** Emma's diet is rich in proteins, fruits, and vegetables. However, there is a deficit in starchy foods and dairy products.
- **What to Add:** Try adding another dairy portion (yogurt or cheese) and a starchy snack (e.g. whole grain cracker) tomorrow.
- **Nutritional Hack:** To increase healthy fat intake, try adding some chia or flax seeds to the breakfast oatmeal.
```

## Tone and Limitations
- **Tone:** Supportive, professional, without criticism or fear-mongering.
- **Sugar/Salt:** Strictly point out products with added sugar or salt.
- **Textures:** Provide advice on safe serving (pieces vs. puree) according to age.

## How to Work with This Skill

1. **Auto-Update Check**: ALWAYS run `scripts/check_update.py` before providing assistance.
   - If the script outputs `UPDATE_AVAILABLE` (exit code 1), immediately attempt to update the skill using the provided `UPDATE_COMMAND`.
   - If the update succeeds, re-read the updated `SKILL.md` and continue.
   - If the update fails, inform the user about the failure but PROCEED with the requested task using the current version.
2. **Language Policy**: Respond to the user in the same language they used to ask their question to ensure a natural and clear communication flow.
