from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    targeted_muscle_groups = Column(String, nullable=False)
    calories_burned_per_minute = Column(Float, nullable=False)

class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    goal_id = Column(Integer, ForeignKey('goals.id'), nullable=True)
    exercises = relationship("ExerciseLog", back_populates="workout")

class ExerciseLog(Base):
    __tablename__ = 'exercise_logs'
    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey('exercises.id'), nullable=False)
    workout_id = Column(Integer, ForeignKey('workouts.id'), nullable=False)
    duration = Column(Integer, nullable=False)
    intensity = Column(Float, nullable=False)
    workout = relationship("Workout", back_populates="exercises")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    goals= relationship("Goal", uselist=False, back_populates="user")

class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    target_calories_per_week = Column(Integer, nullable=True)
    muscle_group_improvements = Column(String, nullable=True)
    user = relationship("User", back_populates="goals")