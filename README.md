# CSC 325 CI/CD Pipeline

A small Django + Django REST Framework backend with a four-stage GitHub Actions pipeline
(Setup, Dependencies, Test, Deploy).

## Endpoints

| Method | Path | Response |
|---|---|---|
| GET | `/api/health/` | `{"status": "ok"}` |
| GET | `/api/hello/?name=Rory` | `{"message": "Hello, Rory!", "course": "CSC 325"}` |

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py test -v 2       # run the test suite
python manage.py runserver       # http://127.0.0.1:8000/api/hello/
```

## Pipeline

Defined in `.github/workflows/csc325_ci_cd.yml`. Runs on every push to `main`
(and on pull requests into `main`, without Deploy).

1. **Setup**: checks out the code and installs Python.
2. **Dependencies**: installs `requirements.txt`.
3. **Test**: runs `python manage.py test`; any failure stops the pipeline.
4. **Deploy**: `needs: test`, so it only starts after Test passes. Triggers the Render
   deploy hook when the `RENDER_DEPLOY_HOOK` secret is set, otherwise echoes the deploy.

## Workflow

`main` is protected by a ruleset (pull request required, `Test` check must pass).
Changes are made on a feature branch and merged through a pull request.
