from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("sqlite:///test.db", echo=True)


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "usertable"

    id: Mapped[int] =  mapped_column(primary_key =True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] 


    def __repr__(self) -> str:
        return f"User(id={self.id!r}), name={self.name!r}, age={self.age!r}"

Base.metadata.create_all(engine)


with Session(engine) as session:
    daniel = User(
        name= "daniel",
        age= 12,
            )

    session.add(daniel)

    session.commit()

    smt = select(User).where(User.name == 'daniel')
    result = session.execute(smt).scalars().all()
    print(result)
