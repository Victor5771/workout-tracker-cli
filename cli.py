import argparse
from .workout_tracker import WorkoutTracker
from .exercise import Exercise

def main():
    parser = argparse.ArgumentParser(description="Workout Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_exercise_parser = subparsers.add_parser("add_exercise", help="Add a new exercise")
    add_exercise_parser.add_argument("name", help="Exercise name")
    add_exercise_parser.add_argument("muscle_groups", help="Muscle groups targeted, separated by commas")
    add_exercise_parser.add_argument("calories_per_minute", type=float, help="Calories burned per minute")

    log_workout_parser = subparsers.add_parser("log_workout", help="Log a new workout")
    log_workout_parser.add_argument("user_id", type=int, help="User ID")
    log_workout_parser.add_argument("exercises", nargs="+", type=int, help="Exercise IDs")
    log_workout_parser.add_argument("duration",type=int, help="Workout duration in minutes")
    log_workout_parser.add_argument("intensity", type=float, help="Workout intensity")

    view_statistics_parser = subparsers.add_parser("view_statistics", help="View workout statistics")
    view_statistics_parser.add_argument("user_id", type=int, help="User ID")

    set_goals_parser = subparsers.add_parser("set_goals", help="Set fitness goals")
    set_goals_parser.add_argument("user_id", type=int, help="User ID")
    set_goals_parser.add_argument("target_calories_per_week", type=int, help="Target calories burned per week")
    set_goals_parser.add_argument("muscle_group_improvements", help="Muscle group improvements, separated by commas")

    args = parser.parse_args()

    db_uri = "sqlite:///workout_tracker.db"
    workout_tracker = WorkoutTracker(db_uri)

    if args.command == "add_exercise":
        exercise = Exercise(args.name, args.muscle_groups, args.calories_per_minute)
        workout_tracker.add_exercise(exercise)

    elif args.command == "log_workout":
        user_id = args.user_id
        exercises = [workout_tracker.session.query(Exercise).filter_by(id=exercise_id).first() for exercise_id in args.exercises]
        workout_tracker.log_workout(user_id, exercises, args.duration, args.intensity)

    elif args.command == "view_statistics":
        workout_tracker.view_workout_statistics(args.user_id)

    elif args.command == "set_goals":
        user_id = args.user_id
        target_calories_per_week = args.target_calories_per_week
        muscle_group_improvements = args.muscle_group_improvements
        workout_tracker.set_fitness_goals(user_id, target_calories_per_week, muscle_group_improvements)

if __name__ == "__main__":
    main()