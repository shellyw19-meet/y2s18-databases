from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(student_name, show, rate):
	hhh = Knowledge(student_name = student_name,
		show = show,
		rate = rate)
	session.add(hhh)
	session.commit()



add_article("Noa","70s show", 7)

def query_all_articles():
	return session.query(Knowledge).all()
print(query_all_articles())
	

def query_article_by_name(name1):
	return session.query(Knowledge).filter_by(name=name1).all()
print(query_article_by_name())
	

def delete_article_by_name():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
