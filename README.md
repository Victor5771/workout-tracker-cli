# workout-tracker-cli

## Description
The Workout Tracker CLI is a command-line application designed to help users track their workouts, log exercises, and set fitness goals. It provides functionality to add exercises, log workouts with details such as duration and intensity, and view statistics about workouts.

## Features
- Add exercises: Users can add new exercises to the database.
- Log workouts: Users can log their workouts by specifying the duration, exercises performed, and intensity levels.
- Set goals: Users can set fitness goals, including target calories burned per week and muscle group improvements.
- View statistics: Users can view statistics about their workouts, including total duration, calories burned, and muscle groups targeted.

## Installation
1. Clone the repository:
    git@github.com:Victor5771/workout-tracker-cli.git

2. Navigate to the project directory:
    cd workout-tracker-cli

3. Install dependencies:
    pip install -r requirements.txt

4. Create the SQLite database:
   python3 database.py


## Usage

- Add exercise:
   python3 cli.py --add-exercise "Push-ups"

- Log workout:
   python3 cli.py --log-workout "your_username" (john_doe)

- To test the add_goal functionality, you can use the following command:
   python3 cli.py --add-goal "john_doe"

## Tests for  the SQLite database
- To view the goals made, you can execute the following SQLite command in your terminal:
   sqlite3 workout_tracker.db

-  view the goals:
  SELECT * FROM Goals;
- view all the logged workouts, you can run:
  SELECT * FROM Workouts;
- view the exercise logs associated with the workouts, you can run:
  SELECT * FROM ExerciseLogs;
- View all Exercises:
   SELECT * FROM Exercises;






## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make your changes and commit them (`git commit -am 'Add new feature'`)
4. Push your changes to the branch (`git push origin feature/new-feature`)
5. Create a new pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- This project was inspired by the need for a simple and intuitive workout tracking tool.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make your changes and commit them (`git commit -am 'Add new feature'`)
4. Push your changes to the branch (`git push origin feature/new-feature`)
5. Create a new pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- This project was inspired by the need for a simple and intuitive workout tracking tool.


## Contact
For any questions or feedback, feel free to reach out:
- Email:  vkyalo25@gmail.com
- GitHub: [Victor5771](https://github.com/Victor5771)


