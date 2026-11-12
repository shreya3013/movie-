# Movie Collection Manager

A simple movie collection app built with Python, Streamlit, and SQLite. Movie records are stored in `movies.db` and remain available after the app closes.

## Setup

Open PowerShell in the project folder and create a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

Start the app from the project folder:

```powershell
streamlit run app.py
```

The database and `movies` table are created automatically when the app starts.

## Test

1. Enter a movie name, genre, rating, and release year, then select **Add Movie**.
2. Confirm it appears under **View Movies**.
3. Add more movies and check the average rating, highest-rated movie, and genre summary.
4. Restart the app and confirm the movies are still present.
