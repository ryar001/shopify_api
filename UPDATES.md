## 2025-09-17

### What's New

#### `automation_scripts/ai-tracker.sh`

- Added a new bash script to automate the process of tracking changes, generating summaries, and committing them.
- The script uses `git diff` to capture staged changes and invokes a `gemini` CLI tool to produce summaries and commit messages.
- It automatically prepends the generated summary to a central `UPDATES.md` file.

### Refactor

#### `GEMIINI.md`

- Overhauled the entire set of instructions, replacing the previous workflow with a detailed guide for an "AI Coding Assistant".
- The new guidelines cover project context, code structure, data handling, testing, documentation, and specific AI guardrails.
- Introduced new conventions, including the use of `PLANNING.md` and `TASK.md` files and a syntax for special commands.

#### `AI_TRACKER_GENIE.md`

- Deleted the instruction file for the AI changes tracker, as its functionality has been automated and integrated into the new `ai-tracker.sh` script.
