from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy import create_engine, String, select
from typing import List
class Base(DeclarativeBase):
    pass


class Weather(Base):
    __tablename__ = "weather"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    city: Mapped[str] = mapped_column(String(30))
    temp_lo: Mapped[int] 
    temp_hi: Mapped[int]
    
    def __repr__(self) -> str:
        return f"User(id=({self.id!r}, city={self.city!r}, temp_lo = {self.temp_lo!r}, temp_hi = {self.temp_hi!r})"

engine = create_engine("postgresql://localhost/mydb", echo=False)
Base.metadata.create_all(engine)

with Session(engine) as session:
    Miami = Weather(
        city = "Miami",
        temp_lo = 12,
        temp_hi = 40,
            )
#   session.add(Miami)
    result = session.execute(select(Weather).where((Weather.temp_lo > 10) & (Weather.temp_hi < 50) )).scalars().all()
    session.executej(select(Weather).where(city = 'Miami') = 10;
    session.commit()
    print(result)
    print(type(Weather.city))
