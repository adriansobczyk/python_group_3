from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
# from alembic.config import Config

# alembic_cfg = Config("alembic.ini")
# url = alembic_cfg.get_main_option("sqlalchemy.url")
# Session = sessionmaker(bind=url)

engine = create_engine("sqlite:///mynotes.db")
Session = sessionmaker(bind=engine)
session = Session()
