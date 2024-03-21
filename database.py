from sqlalchemy import create_engine

def create_connection(db_file):
    engine = create_engine(f"sqlite:///{db_file}")
    return engine

def create_tables(engine):
    create_query = """
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username VARCHAR,
        email VARCHAR
    );

    CREATE TABLE IF NOT EXISTS Goals (
        goal_id INTEGER PRIMARY KEY,
        user_id INTEGER REFERENCES Users(id),
        target_calories_per_week INTEGER,
        muscle_group_improvements TEXT
    );

    CREATE TABLE IF NOT EXISTS Exercises (
        exercise_id INTEGER PRIMARY KEY,
        name VARCHAR,
        targeted_muscle_groups TEXT,
        calories_burned_per_minute FLOAT
    );

    CREATE TABLE IF NOT EXISTS Workouts (
        workout_id INTEGER PRIMARY KEY,
        date DATE,
        duration INTEGER,
        user_id INTEGER REFERENCES Users(id),
        goal_id INTEGER REFERENCES Goals(goal_id)
    );

    CREATE TABLE IF NOT EXISTS ExerciseLogs (
        log_id INTEGER PRIMARY KEY,
        exercise_id INTEGER REFERENCES Exercises(exercise_id),
        workout_id INTEGER REFERENCES Workouts(workout_id)
    );
    """
    try:
        with engine.connect() as connection:
            connection.execute(create_query)
    except Exception as e:
        print(e)

def main():
    database = "workout_tracker.db"
    engine = create_connection(database)
    create_tables(engine)

if __name__ == "__main__":
    main()
