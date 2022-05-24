if __name__ == "__main__":
    from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, Boolean, ForeignKey
    from sqlalchemy.orm import declarative_base

    Base = declarative_base()

    class Role(Base):
        __tablename__ = 'role'

        id = Column(Integer, primary_key=True)
        name = Column(String(10), unique=True, nullable=False)

    class Patent(Base):
        __tablename__ = 'patent'

        id = Column(Integer, primary_key=True)
        name = Column(String(10), unique=True, nullable=False)

    class Team(Base):
        __tablename__ = 'team'

        id = Column(Integer, primary_key=True)
        name = Column(String(30), unique=True, nullable=False)

    class User(Base):
        __tablename__ = 'user'
        
        id = Column(Integer, primary_key=True)
        username = Column(String(30), unique=True, nullable=False)
        email = Column(String(100), unique=True, nullable=False)
        password = Column(String(255), nullable=False)
        created_at = Column(DateTime(6), default=func.current_timestamp())
        updated_at = Column(DateTime(6), onupdate=func.current_timestamp())
        active = Column(Boolean(), default=True)
        team = Column(Integer, ForeignKey(Team.id), nullable=False)
        patent = Column(Integer, ForeignKey(Patent.id), nullable=False)
        role = Column(Integer, ForeignKey(Role.id), nullable=False)
        
    engine = create_engine('sqlite:///database.db', echo=True)
    Base.metadata.create_all(engine)
