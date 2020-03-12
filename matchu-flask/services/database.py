from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:@localhost:3306/matchu', convert_unicode=True, pool_size=10, max_overflow=0, pool_recycle=3600)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
metadata = MetaData(bind=engine)

def init_db(app):
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    db_session.app = app
    import classes
    Base.metadata.create_all(bind=engine)