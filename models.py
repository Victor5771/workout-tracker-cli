# models.py
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

class Goal(Base):
    __tablename__ = "Goals"
    goal_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    target_calories_per_week = Column(Integer)
    muscle_group_improvements = Column(Text)
    user = relationship("User")

class Exercise(Base):
    __tablename__ = "Exercises"
    exercise_id = Column(Integer, primary_key=True)
    name = Column(String)
    targeted_muscle_groups = Column(Text)
    calories_burned_per_minute = Column(Float)

class Workout(Base):
    __tablename__ = "Workouts"
    workout_id = Column(Integer, primary_key=True)
    date = Column(Date)
    duration = Column(Integer)
    user_id = Column(Integer, ForeignKey("Users.id"))
    goal_id = Column(Integer, ForeignKey("Goals.goal_id"))
    user = relationship("User")
    goal = relationship("Goal")

class ExerciseLog(Base):
    __tablename__ = "ExerciseLogs"
    log_id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey("Exercises.exercise_id"))
    workout_id = Column(Integer, ForeignKey("Workouts.workout_id"))

