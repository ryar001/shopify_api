# 
 Changes Tracker
 this only works with the GEMINI.md file for now.
 ONLY RUN WHEN START WITH ai-tracker, else it will not work.

## Overview

The AI Changes Tracker is a smart command-line utility designed to help developers automatically monitor, summarize, and document changes within a software project.

It watches a specified set of files and directories for modifications. When requested, it intelligently analyzes the differences, categorizes them, and appends a summary to a central `UPDATES.md` file. This automates the tedious process of maintaining a changelog, making it easier to track progress and prepare release notes.

## Features

- **Git-Aware Context**: Automatically detects changes in your project by comparing the current state against the Git history. No need to manually track files.
- **On-Demand Updates**: Generate change summaries only when you need them.
- **AI-Powered Summarization**: Uses AI to analyze code diffs and generate concise, human-readable descriptions of what changed.
- **Automatic Categorization**: Automatically sorts changes into logical categories like `What's New`, `Bugfix`, `Refactor`, etc.
- **Structured Markdown Output**: Generates a clean, well-organized `UPDATES.md` file, perfect for project documentation.

## How It Works

The workflow is designed to be simple and unobtrusive, leveraging your existing Git workflow.

1.  **Development**: You work on your code as you normally would, making and staging changes with `git add`.

2.  **Update Generation**: When you're ready to document your progress, you run the `update` command.
    - The tracker uses `git diff` to find all staged changes.
    - For each modified file, it generates a diff against the `HEAD` of the current branch.
    - The `diff` is passed to an AI model, which produces a bullet-point summary of the changes and assigns a relevant category.
    - These summaries are then formatted and appended to the `UPDATES.md` file under the current date.
        - ignore updates if it is just changing of comments, removing space , or other non-code changes

## Usage

The tool is operated via a single, powerful command.

#### Generate or update the `UPDATES.md` file:

This command scans for staged changes and updates the log.

```bash
# Analyze staged changes and write them to UPDATES.md
ai-tracker update
```

You can also compare against a specific commit or branch:

```bash
# Compare against a specific commit
ai-tracker update --ref <commit-hash>

# Compare against another branch
ai-tracker update --ref <branch-name>
```

## `UPDATES.md` File Format

The generated `UPDATES.md` file is structured for maximum clarity. Changes are grouped by date, then category, then file.

### Example `UPDATES.md`

```markdown
# Project Updates

## 2023-10-27

### What's New

#### `src/features/auth.js`

- Implemented the core logic for the new user authentication flow.
- Added a new component for the login form.

### Bugfix

#### `src/components/Header.js`

- Fixed a layout issue where the logo would overlap navigation links on smaller screens.

### Refactor

#### `src/api/client.js`

- Refactored API call handling to use `async/await` for better readability.
- Centralized error handling for all API requests.

```

## Future Improvements

- **Commit Message Integration**: Use the user's commit messages to provide additional context to the AI for even better summaries.
- **Custom Categories**: Allow users to define their own change categories.
- **Interactive Mode**: Allow users to review, edit, and approve AI-generated summaries before they are written to the file.
- **Automated Commit Hooks**: Offer an option to automatically run the tracker as a `pre-commit` hook.
