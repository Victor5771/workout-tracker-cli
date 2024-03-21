import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Workout, ExerciseLog, User, Goal
from .exercise import Exercise

class WorkoutTracker:
    def __init__(self, db_uri):
        engine = create_engine(db_uri)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_exercise(self, exercise):
        new_exercise = Exercise(
            name=exercise.name,
            targeted_muscle_groups=exercise.targeted_muscle_groups,
            calories_burned_per_minute=exercise.calories_burned_per_minute
        )
        self.session.add(new_exercise)
        self.session.commit()

    def log_workout(self, user_id, exercises, duration, intensity):
        workout = Workout(
            date=datetime.date.today().strftime('%Y-%m-%d'),
            duration=duration,
            user_id=user_id
        )
        self.session.add(workout)
        self.session.commit()

        for exercise in exercises:
            exercise_log = ExerciseLog(
                exercise_id=exercise.id,
                workout_id=workout.id,
                duration=exercise.duration,
                intensity=intensity
            )
            self.session.add(exercise_log)

        self.session.commit()

    def view_workout_statistics(self, user_id):
        workouts = self.session.query(Workout).filter_by(user_id=user_id).all()
        total_calories_burned = sum([workout.total_calories_burned for workout in workouts])
        average_intensity = sum([workout.average_intensity for workout in workouts]) / len(workouts)
        most_frequent_muscle_groups = self.get_most_frequent_muscle_groups(user_id)

        print(f"Total Calories Burned: {total_calories_burned}")
        print(f"Average Intensity: {average_intensity}")
        print("Most Frequent Muscle Groups:")
        for muscle_group in most_frequent_muscle_groups:
            print(muscle_group)

    def get_most_frequent_muscle_groups(self, user_id):
        exercise_logs = self.session.query(ExerciseLog).filter_by(user_id=user_id).all()
        muscle_group_counts = {}

        for exercise_log in exercise_logs:
            for muscle_group in exercise_log.exercise.targeted_muscle_groups.split(','):
                muscle_group = muscle_group.strip()
                if muscle_group not in muscle_group_counts:
                    muscle_group_counts[muscle_group] = 0
                muscle_group_counts[muscle_group] += 1

        sorted_muscle_groups = sorted(muscle_group_counts.items(), key=lambda x: x[1], reverse=True)
        return [muscle_group[0] for muscle_group in sorted_muscle_groups]

    def set_fitness_goals(self, user_id, target_calories_per_week, muscle_group_improvements):
        user = self.session.query(User).filter_by(id=user_id).first()
        user.goals.target_calories_per_week = target_calories_per_week
        user.goals.muscle_group_improvements = muscle_group_improvements
        self.session.commit()

    def __del__(self):
        self.session.close()