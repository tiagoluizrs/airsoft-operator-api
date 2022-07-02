if __name__ == "__main__":
    from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, Boolean, ForeignKey, Text, Float, UniqueConstraint
    from sqlalchemy.orm import declarative_base
    from config import app_config, app_active
    config = app_config[app_active]

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
        image = Column(String(50), nullable=True)

    class User(Base):
        __tablename__ = 'user'
        
        id = Column(Integer, primary_key=True)
        username = Column(String(30), unique=True, nullable=False)
        email = Column(String(100), unique=True, nullable=False)
        password = Column(String(255), nullable=False)
        created_at = Column(DateTime(6), default=func.current_timestamp())
        updated_at = Column(DateTime(6), onupdate=func.current_timestamp())
        active = Column(Boolean(), default=True)
        team_id = Column(Integer, ForeignKey(Team.id), nullable=False)
        patent_id = Column(Integer, ForeignKey(Patent.id), nullable=False)
        role_id = Column(Integer, ForeignKey(Role.id), nullable=False)

    class Brand(Base):
        __tablename__ = 'brand'
        
        id = Column(Integer, primary_key=True)
        name = Column(String(30), unique=True, nullable=False)
        image = Column(Text, nullable=True)

    class Category(Base):
        __tablename__ = 'category'

        id = Column(Integer, primary_key=True)
        name = Column(String(30), unique=True, nullable=False)

    class Weapon(Base):
        __tablename__ = 'weapon'

        id = Column(Integer, primary_key=True)
        name = Column(String(30), unique=True, nullable=False)
        image = Column(Text, nullable=True)
        fps = Column(Float, nullable=False)
        category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
        brand_id = Column(Integer, ForeignKey(Brand.id), nullable=False)

    class UserWeapon(Base):
        __tablename__ = 'user_weapon'
        
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey(User.id), nullable=False)
        weapon_id = Column(Integer, ForeignKey(Weapon.id), nullable=False)
        created_at = Column(DateTime(6), default=func.current_timestamp())
        updated_at = Column(DateTime(6), onupdate=func.current_timestamp())

    class WeaponRating(Base):
        __tablename__ = 'weapon_rating'
        __table_args__ = (
            UniqueConstraint('user_id', 'user_weapon_id', 'upped'),
        )
        
        id = Column(Integer, primary_key=True)
        value = Column(Float, nullable=False)
        created_at = Column(DateTime(6), default=func.current_timestamp())
        updated_at = Column(DateTime(6), onupdate=func.current_timestamp())
        user_id = Column(Integer, ForeignKey(User.id), nullable=False)
        user_weapon_id = Column(Integer, ForeignKey(UserWeapon.id), nullable=False)
        upped = Column(Boolean, default=False)

    class FpsWeapon(Base):
        __tablename__ = 'fps_weapon'

        id = Column(Integer, primary_key=True)
        value = Column(Float, nullable=False)
        userWeapon_id = Column(Integer, ForeignKey(UserWeapon.id), nullable=False)
        created_at = Column(DateTime(6), default=func.current_timestamp())

    class Equipaments(Base):
        __tablename__ = 'equipaments'

        id = Column(Integer, primary_key=True)
        name = Column(Text)
        type = Column(Integer)
        price = Column(Float)
        
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
    Base.metadata.create_all(engine)
