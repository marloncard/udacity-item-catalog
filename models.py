from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(90), nullable=False)
    email = Column(String(150), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(90), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in serializable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String(90), nullable=False)
    category = relationship(Category)
    category_id = Column(Integer, ForeignKey('category.id'))
    instructions = Column(String(450))
    ingredients = Column(String(350))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in serializable format"""
        return {
            'name': self.name,
            'id': self.id,
            'instructions': self.instructions,
            'ingredients': self.ingredients,
        }


engine = create_engine('sqlite:///recipes.db')
Base.metadata.create_all(engine)
