from database import create_connection
from models import User, Exercise, Workout, ExerciseLog
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

class WorkoutTracker:
    def __init__(self):
        self.engine = create_connection("workout_tracker.db")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_exercise(self, name):
        try:
            new_exercise = Exercise(name=name)
            self.session.add(new_exercise)
            self.session.commit()
            print(f"Exercise '{name}' added successfully.")
        except SQLAlchemyError as e:
            self.session.rollback()
            print("Error occurred while adding exercise:", e)

    def log_workout(self, username):
        try:
            user = self.session.query(User).filter_by(username=username).first()
            if not user:
                print(f"User '{username}' not found.")
                return

            date = datetime.now().date()
            duration = int(input("Enter workout duration (minutes): "))
            goal_id = int(input("Enter goal ID (if applicable): "))

            workout = Workout(date=date, duration=duration, user_id=user.id, goal_id=goal_id)
            self.session.add(workout)

            exercise_logs = []
            while True:
                exercise_name = input("Enter exercise name (or type 'done' to finish): ")
                if exercise_name.lower() == "done":
                    break

                exercise = self.session.query(Exercise).filter_by(name=exercise_name).first()
                if not exercise:
                    print(f"Exercise '{exercise_name}' not found. Please add it first.")
                    continue

                duration = int(input(f"Enter duration of '{exercise_name}' (minutes): "))
                intensity = int(input("Enter intensity level (1-10): "))

                exercise_log = ExerciseLog(exercise_id=exercise.exercise_id, workout_id=workout.workout_id,
                                           duration=duration, intensity=intensity)
                exercise_logs.append(exercise_log)

            workout.exercise_logs = exercise_logs
            self.session.commit()
            print("Workout logged successfully.")
        except (SQLAlchemyError, ValueError) as e:
            self.session.rollback()
            print("Error occurred while logging workout:", e)

    def __del__(self):
        self.session.close()

# Usage example:
# tracker = WorkoutTracker()
# tracker.add_exercise("Push-ups")
# tracker.log_workout("your_username")
