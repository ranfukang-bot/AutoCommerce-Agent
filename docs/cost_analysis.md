# Cost Analysis

This project treats generation cost as a workflow variable.

## Cost Control Logic

1. Use lightweight generation for initial script and prompt exploration.
2. Use premium video generation only after angle confirmation.
3. Store reusable prompt templates by category.
4. Avoid scenes with high failure probability.
5. Track failure reasons and regenerate only when necessary.

## Common Failure Categories

| Category | Failure Type | Suggested Action |
|---|---|---|
| T-Shirt | Print deformation | Reduce body motion and increase close-up stability |
| Motor Oil | Unrealistic mechanical action | Use bottle display and motorcycle lifestyle scene |
| Household | Assembly distortion | Use before-after contrast instead of detailed assembly |
| Generic Product | Unclear product identity | Add opening close-up and simplify camera movement |
