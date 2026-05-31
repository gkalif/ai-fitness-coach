from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Fitness API is running"}

@app.get("/api/workouts")
def get_workouts():
    return {
        "workouts": [
            {"id": 1, "name": "Push Day", "exercises": ["Bench Press", "Shoulder Press", "Tricep Dips"]},
            {"id": 2, "name": "Pull Day", "exercises": ["Pull Ups", "Barbell Row", "Bicep Curls"]},
            {"id": 3, "name": "Leg Day", "exercises": ["Squat", "Romanian Deadlift", "Lunges"]},
        ]
    }