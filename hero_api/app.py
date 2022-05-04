from db.hero import Hero
from sqlmodel import Session, create_engine, SQLModel

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(Hero(name="Deadpond", secret_name="wilson"))
    session.commit()
