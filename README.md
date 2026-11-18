# Student Course API

A beginner-friendly, read-only Flask backend for the System Integration and Architecture
Lesson 3 laboratory. It uses fictional sample course data and does **not** connect to a
database or store real student records.

## Project files

- `app.py` — Flask application, sample data, and API routes.
- `requirements.txt` — Python dependencies, including Gunicorn.
- `render.yaml` — Render Web Service configuration.
- `Procfile` — Alternative process declaration.
- `tests/test_api.py` — Automated endpoint tests.

## Requirements

- Python 3.10 or newer
- pip

## Run locally

1. Open a terminal in this project folder.
2. Create and activate a virtual environment (recommended).
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the API:

   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000/api/health`.

## API endpoints

| Method | Endpoint | Successful result |
|---|---|---|
| GET | `/api/health` | API status JSON, HTTP 200 |
| GET | `/api/courses` | Array of five fictional courses, HTTP 200 |
| GET | `/api/courses/1` | Course with ID 1, HTTP 200 |
| GET | `/api/courses/9999` | Helpful error JSON, HTTP 404 |

Example course response:

```json
{
  "id": 1,
  "code": "ITAS 3228",
  "name": "Web and Mobile Development",
  "description": "Introduction to web and mobile application development."
}
```

## Run automated tests

Install the requirements, then run:

```bash
python -m unittest discover -s tests -v
```

The tests check the health route, course list, valid course ID, and invalid course ID.
A passing automated test run is evidence for the local test environment; it does not
replace testing the deployed Render URL.

## Deploy to Render

1. Push the contents of this folder to a GitHub repository named `student-course-api`.
2. In Render, choose **New > Web Service** and connect that repository.
3. Use these settings (or let Render read `render.yaml`):

   - Runtime: Python
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
   - Health check path: `/api/health`

4. Create the service and wait for the deployment to finish.
5. Copy the actual HTTPS URL shown in your Render dashboard.
6. Test these URLs in a browser, replacing `YOUR-RENDER-URL` with your service URL:

   - `https://YOUR-RENDER-URL/api/health`
   - `https://YOUR-RENDER-URL/api/courses`
   - `https://YOUR-RENDER-URL/api/courses/1`
   - `https://YOUR-RENDER-URL/api/courses/9999`

`app:app` means: load the Flask variable named `app` from the Python file `app.py`.
If you rename either one, update the start command accordingly.

## CORS configuration

For this fictional-data classroom prototype, the default allows cross-origin requests.
To restrict browser access to known frontend origins, set the Render environment variable
`CORS_ORIGINS` to a comma-separated list, for example:

```text
https://your-website.example,https://your-mobile-web.example
```

CORS is not authentication. It does not prevent non-browser clients from calling a public
API. A real student system needs backend authentication, authorization, validation,
secure data handling, and a persistent database.

## Architecture overview

A website or mobile application (client) sends an HTTP GET request to an API endpoint.
Flask handles the route and returns JSON with an HTTP status code. Both clients can use
the same backend URL, while keeping their own user interfaces.

## Important limitations

- All course records are fictional and stored in memory in `app.py`.
- No database, login, authentication, enrollment, or write operations are implemented.
- This is a learning prototype, not a production student information system.
- A successful deployment does not by itself prove security or frontend integration.
- Render free services may have availability and spin-down limitations; check Render's
  current plan details before relying on the service.
