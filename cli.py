import argparse
from workout_tracker import WorkoutTracker

def main():
    parser = argparse.ArgumentParser(description="Workout Logger CLI")
    parser.add_argument("--add-exercise", help="Add a new exercise to the database")
    parser.add_argument("--log-workout", help="Log a workout session")
    parser.add_argument("--add-goal", help="Add a new goal for a user")
    args = parser.parse_args()

    tracker = WorkoutTracker()

    if args.add_exercise:
        tracker.add_exercise(args.add_exercise)
    elif args.log_workout:
        tracker.log_workout(args.log_workout)
    elif args.add_goal:
        tracker.add_goal(args.add_goal)
    else:
        print("Invalid command. Use --help for usage information.")

if __name__ == "__main__":
    main()
