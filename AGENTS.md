# AGENTS.md

This repository is a Django training workspace made up of many independent project folders, not a single app. Each numbered lab or day folder is usually a standalone Django project with its own `manage.py`, app files, templates, and SQLite database.

## Project layout conventions

- Example roots include `Day_1`, `Day2`, `Day3`, `Day4`, `Task1`, `Task2`, `Task3`, `Task4`, `Task10`, `MLproject`, and similar folders.
- Each project folder is self-contained and should be treated as its own Django project.
- The active project is the folder that contains `manage.py` and the project settings package (for example `Task3/Task3/settings.py`).

## Working rules for AI agents

- Always work inside the relevant project directory instead of assuming the repository root is the Django project root.
- Run Django commands from the target project folder, for example:
  - Activate the virtual environment: `& .\workplace\Scripts\Activate.ps1`
  - Start the server: `python manage.py runserver`
  - Create or apply migrations: `python manage.py makemigrations` and `python manage.py migrate`
  - Run tests: `python manage.py test`
  - Create an admin user: `python manage.py createsuperuser`
- Prefer project-local configuration and app names. Do not assume code or settings are shared across folders.
- Keep edits scoped to the current task or day folder unless the task explicitly says otherwise.

## Editing guidance

- Follow Django conventions already used in the task: `settings.py`, `urls.py`, app folders, templates, static files, and migrations.
- Preserve the existing structure of the task project; this repo contains many generated starter projects and lab exercises.
- If multiple apps exist inside one project, keep URLs, models, and app registration inside that same task project.
- Avoid creating cross-project imports or shared global state between task folders.

## Common pitfalls

- Do not run a `manage.py` command from the workspace root when the intended project is a subfolder.
- Do not treat `db.sqlite3` files as shared across tasks; they are local to each project.
- This repo contains many independent exercises, so unrelated projects should not be modified while resolving one task.

## Good default behavior

- Inspect the target task’s `manage.py` and settings before making changes.
- Keep fixes minimal, project-scoped, and aligned with the task’s current architecture.
- Treat this workspace as a collection of small learning projects rather than one production codebase.
