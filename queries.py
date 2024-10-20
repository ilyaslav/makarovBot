import asyncio
from sqlalchemy.future import select
from sqlalchemy import between

from database import session_factory
from models import *

async def insert_user(user_id: str):
    user = UserBase(
        id = user_id
    )
    async with session_factory() as sf:
        sf.add(user)
        await sf.commit()

async def select_user(user_id: str) -> UserBase:
    async with session_factory() as sf:
        user = await sf.get(UserBase, user_id)
        return user

async def update_user_state(user_id: str, state: str):
    if state not in State._value2member_map_:
        return
    async with session_factory() as sf:
        user = await sf.get(UserBase, user_id)
        if user:
            user.state = state
            await sf.commit()

async def update_user_tafiff(user_id: str, tariff: int):
    async with session_factory() as sf:
        user = await sf.get(UserBase, user_id)
        if user:
            user.tariff = tariff
            await sf.commit()


async def check_admin(user_id: str) -> bool:
    async with session_factory() as sf:
        admin = await sf.get(AdminBase, user_id)
        return bool(admin)


async def select_tariff(tariff_id: str) -> TariffBase:
    async with session_factory() as sf:
        tariff = await sf.get(TariffBase, tariff_id)
        return tariff


async def insert_journal(user_id: str, text: str):
    journal = JournalBase(
        user_id = user_id,
        text = text
    )
    async with session_factory() as sf:
        sf.add(journal)
        await sf.commit()

async def select_journal(user_id: str, start_date: datetime) -> list[JournalBase]:
    async with session_factory() as sf:
        journals = await sf.execute(
            select(JournalBase)
            .filter(JournalBase.user_id == user_id)
            .filter(JournalBase.date >= start_date)
        )
        return journals.scalars().all()


async def insert_training_profile(user_id: str):
    training_profile = TrainingProfileBase(
        user_id = user_id
    )
    async with session_factory() as sf:
        sf.add(training_profile)
        await sf.commit()

async def update_gender(user_id: str, gender: str):
    async with session_factory() as sf:
        training_profile = await sf.get(TrainingProfileBase, user_id)
        if training_profile:
            training_profile.gender = gender
            await sf.commit()

async def update_purpose(user_id: str, purpose: str):
    async with session_factory() as sf:
        training_profile = await sf.get(TrainingProfileBase, user_id)
        if training_profile:
            training_profile.purpose = purpose
            await sf.commit()

async def update_number_of_training(user_id: str, number_of_training: int):
    async with session_factory() as sf:
        training_profile = await sf.get(TrainingProfileBase, user_id)
        if training_profile:
            training_profile.number_of_training = number_of_training
            await sf.commit()

async def select_training_profile(user_id: str) -> TrainingProfileBase:
    async with session_factory() as sf:
        training_profile = await sf.get(TrainingProfileBase, user_id)
        return training_profile


async def insert_video(id: str, text: str):
    video = VideoBase(
        id = id,
        text = text
    )
    async with session_factory() as sf:
        sf.add(video)
        await sf.commit()

async def select_video(id: str) -> VideoBase:
    async with session_factory() as sf:
        video = await sf.get(VideoBase, id)
        return video

async def delete_video(id: str):
    async with session_factory() as sf:
        video = await sf.get(VideoBase, id)
        if video:
            await sf.delete(video)
            await sf.commit()


async def select_exercises(category: str) -> list[ExerciseBase]:
    async with session_factory() as sf:
        exercises = await sf.execute(
            select(ExerciseBase)
            .filter(ExerciseBase.category == category)
        )
        return exercises.scalars().all()


async def insert_image(id: str, text: str, category: str):
    image = ImageBase(
        id = id,
        text = text,
        category = category
    )
    async with session_factory() as sf:
        sf.add(image)
        await sf.commit()

async def select_images(category: str) -> list[ImageBase]:
    async with session_factory() as sf:
        images = await sf.execute(
            select(ImageBase)
            .filter(ImageBase.category == category)
        )
        return images.scalars().all()

async def delete_images(category: str):
    async with session_factory() as sf:
        result = await sf.execute(
            select(ImageBase)
            .where(ImageBase.category == category)
        )
        images = result.scalars().all()
        for image in images:
            await sf.delete(image)
            await sf.commit()


# asyncio.run(insert_user("1234"))
async def main():
    j = await select_journal("123", datetime.datetime.now())
    for i in j:
        print(i.date, i.text)

if __name__ == "__main__":
    asyncio.run(main())
