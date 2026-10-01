---
name: check-why-css-not-show
description: "Use when: CSS is not loading in a Django or HTML page, the page renders but styles are missing, or static files are not being served correctly."
---

# Check why CSS is not showing

This skill is for diagnosing missing styles in web pages without guessing.

## Goal

Find out whether the issue is caused by one of these common problems:
- the stylesheet file is missing or misnamed
- the template is not linking to the correct static path
- the static URL is configured incorrectly
- the app is not using the correct static directory structure
- the browser is requesting the wrong URL

## Workflow

### 1. Verify the CSS file exists

Check whether the project actually contains the stylesheet in a static folder.

Typical checks:
- app/static/style.css
- app/static/css/style.css
- base project static folder if applicable

If the file is missing, create or restore it before debugging the Django config.

### 2. Confirm the template is loading static files

At the top of the HTML file, verify:

```html
{% load static %}
```

Then verify the stylesheet link uses the static tag:

```html
<link rel="stylesheet" href="{% static 'mycss.css' %}">
```

If the template is using a raw hardcoded path like `href="/static/mycss.css"` or a wrong relative URL, fix that first.

### 3. Check the app static configuration

Inspect the Django settings for the following:

```python
STATIC_URL = '/static/'
```

Common issue:
- `STATIC_URL = 'static/'` is missing the leading slash
- This creates a relative path like `static/mycss.css` instead of `/static/mycss.css`, which often breaks when the page is nested under routes such as `/Student/`.

If using a custom static folder, also check:

```python
STATICFILES_DIRS = [BASE_DIR / 'static']
```

and ensure the app is installed correctly:

```python
INSTALLED_APPS = [
    'Student',
    'django.contrib.staticfiles',
]
```

### 4. Check the browser request

Open DevTools and inspect the Network tab.

Look for:
- a 404 on the CSS file
- the wrong URL being requested
- a different path than the one expected from the HTML template

The URL should usually resolve to something like:

```text
/static/mycss.css
```

not a nested relative value like:

```text
/Student/static/mycss.css
```

### 5. Verify Django dev-server behavior

In development, Django serves app static files automatically when the app and files are set up correctly.

If it still fails, check:
- the app is in `INSTALLED_APPS`
- the static file is inside the app's `static/` directory
- the file name matches exactly what the template asks for
- the server has been restarted after changes

## Decision points

- If the CSS file is missing → create it or correct the file name.
- If the template does not use `{% load static %}` → add it.
- If the template is pointing to the wrong URL → fix the href.
- If `STATIC_URL` is missing the leading slash → set it to `'/static/'`.
- If the browser shows 404 → confirm the file location and URL path.
- If the app is using a custom static root → configure `STATICFILES_DIRS` properly.

## Completion checklist

A CSS issue is fixed when all of these are true:
- the `.css` file exists in the correct static folder
- the template loads static correctly
- the browser requests the correct URL
- the page receives HTTP 200 for the stylesheet
- the styles appear on the page without console or network errors

## Example prompts

- "Why is my CSS not loading in Django?"
- "Check why the page renders but the styles are missing."
- "My static file is there, but the browser cannot load the stylesheet."
- "Diagnose the missing CSS in this Django app."

## Project-specific note

In this project, the app structure matches the expected Django pattern, but the static URL is configured as `STATIC_URL = 'static/'` instead of `'/static/'`. That missing leading slash is a common reason for CSS not showing when the page sits under a nested route such as `/Student/`.

## Related customizations

- create a debugging checklist for image and CSS issues
- create a Django static-files troubleshooting skill
- create a browser-network-debugging prompt for frontend rendering problems
