# VARSTREET Sample Django Project

This repository contains a minimal Django project used for demonstration.
The project includes a placeholder client for LLM calls, a simple API
for advanced filtering, and a temporary store of prompts and knowledge.

## Structure

- `VARSTREET/` – Django project root.
  - `manage.py` – Django management script.
  - `VARSTREET/` – Project settings and URLs.
  - `filterapp/` – Application providing the advanced filter API.
  - `llm_client.py` – Placeholder code for calling an LLM.
  - `temp_vars/` – Temporary variables such as prompt store and
    knowledge base.
  - `utils.py` – Empty utility module.

## Requirements

Install the required packages using `pip install -r requirements.txt`.

To run the development server:

```bash
python manage.py runserver
```

