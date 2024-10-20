from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import text
import datetime
import enum


class Base(DeclarativeBase):
    pass

class State(enum.Enum):
    main_menu = 'main_menu'
    training = 'training'
    gym_training = 'gym_training'
    change_gym_training = 'change_gym_training'
    load_gym_training = 'load_gym_training'
    home_training = 'home_training'
    change_home_training = 'change_home_training'
    training_profile = 'training_profile'
    change_profile = 'change_profile'
    male = 'male'
    female = 'female'
    gain_muscle_mass = 'gain_muscle_mass'
    weight_loss = 'weight_loss'
    maintaining_muscle_mass = 'maintaining_muscle_mass'
    workouts_2 = 'workouts_2'
    workouts_3 = 'workouts_3'
    add_training_record = 'add_training_record'
    get_training_record = 'get_training_record'
    necessary_equipment = 'necessary_equipment'
    change_necessary_equipment = 'change_necessary_equipment'
    base_of_exercises = 'base_of_exercises'
    legs = 'legs'
    breast = 'breast'
    back = 'back'
    shoulders = 'shoulders'
    biceps = 'biceps'
    triceps = 'triceps'
    press = 'press'
    stretching = 'stretching'
    MFR = 'MFR'
    add_exercise_video = 'add_exercise_video'
    exercises_video = 'exercises_video'
    tariffs = 'tariffs'
    tarif1 = 'tarif1'
    tarif2 = 'tarif2'
    manual = 'manual'

class UserBase(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True)
    state: Mapped[State] = mapped_column(default=State.main_menu)
    tariff: Mapped[int] = mapped_column(ForeignKey("tariffs.id"), default=0)

class AdminBase(Base):
    __tablename__ = "admins"

    id: Mapped[str] = mapped_column(primary_key=True)

class TariffBase(Base):
    __tablename__ = "tariffs"

    id: Mapped[int] = mapped_column(primary_key=True)
    cost: Mapped[int]

class VideoBase(Base):
    __tablename__ = "videos"

    id: Mapped[str] = mapped_column(primary_key=True)
    text: Mapped[str]

class Category(enum.Enum):
    legs = "legs"
    breast = "breast"
    back = "back"
    shoulders = "shoulders"
    biceps = "biceps"
    triceps = "triceps"
    press = "press"
    stretching = "stretching"
    MFR = "MFR"

class ExerciseBase(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[Category]
    button_name: Mapped[str]
    video: Mapped[str] = mapped_column(ForeignKey("videos.id"))

class ImageBase(Base):
    __tablename__ = "images"

    id: Mapped[str] = mapped_column(primary_key=True)
    text: Mapped[str]
    category: Mapped[str]

class JournalBase(Base):
    __tablename__ = "journals"

    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    date: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow
    )
    text: Mapped[str]

class Gender(enum.Enum):
    M = "M"
    F = "F"

class Purpose(enum.Enum):
    gain_muscle_mass = "gain_muscle_mass"
    weight_loss = "weight_loss"
    maintaining_muscle_mass = "maintaining_muscle_mass"

class TrainingProfileBase(Base):
    __tablename__ = "training_profiles"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), primary_key=True)
    gender: Mapped[Gender]
    purpose: Mapped[Purpose]
    number_of_training: Mapped[int]
