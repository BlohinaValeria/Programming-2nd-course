# from http.client import HTTPException
# from typing import Optional, Union
# from fastapi import FastAPI, HTTPException
# from datetime import datetime
# from pydantic import BaseModel, Field
# from sqlmodel import Field as SQLModelField, Session, SQLModel, create_engine, select
# import os
#
# app = FastAPI()
# #
# # class TermDB(SQLModel, table=True):
# #     id: Optional[int] = SQLModelField(default=None, primary_key=True)
# #     keyword: str = SQLModelField(index=True, unique=True)
# #     description: str = SQLModelField()
# #     created_at: datetime = SQLModelField(default_factory=datetime.now)
# #     updated_at: datetime = SQLModelField(default_factory=datetime.now)
# #
# # class Term(BaseModel):
# #     id: Optional[int] = Field(default=None, primary_key=True)
# #     name: str = Field(index=True)  # Removed unique constraint for BaseModel
# #     description: str = Field(default='error')
# #
# # DATABASE_URL = os.environ.get("DATABASE_URL", 'mysql+pymysql://lera:1234@db/lab6')
# # engine = create_engine(DATABASE_URL)
# #
# # def create_db_and_tables():
# #     SQLModel.metadata.create_all(engine)
# #
# # @app.on_event("startup")
# # def on_startup():
# #     create_db_and_tables()
# #
# # @app.get('/dbconnect')
# # def get_db_info():
# #     return str(engine)
#
# @app.get("/terms/{term}")
# def get_term(term: str):
#     with Session(engine) as session:
#         statement = select(TermDB).where(TermDB.keyword == term)  # Use TermDB
#         results = session.execute(statement)
#         term = results.scalars().first()
#         if not term:
#             raise HTTPException(status_code=404, detail="Term not found")
#         return term
#
# @app.post("/terms", response_model=Term)
# def post_term(term: Term):
#     db_term = TermDB(keyword=term.name, description=term.description) # create TermDB object
#     with Session(engine) as session:
#         try:
#             session.add(db_term)
#             session.commit()
#             session.refresh(db_term)
#             return Term(id=db_term.id, name=db_term.keyword, description=db_term.description)  # return Term object
#         except Exception as e:
#             session.rollback()
#             raise HTTPException(status_code=500, detail=str(e))
#
# @app.put("/terms/{term_id}", response_model=Term)
# def change_term(term_id: int, term_data: Term):
#     with Session(engine) as session:
#         statement = select(TermDB).where(TermDB.id == term_id) # Use TermDB
#         results = session.execute(statement)
#         term = results.scalars().first()
#         if not term:
#             raise HTTPException(status_code=404, detail="Term not found")
#
#         term.keyword = term_data.name # Use TermDB's field
#         term.description = term_data.description # Use TermDB's field
#         session.commit()
#         session.refresh(term)
#         return Term(id=term.id, name=term.keyword, description=term.description) #return Term object
#
# @app.delete("/terms/{term_id}")
# def del_term(term_id: int):
#     with Session(engine) as session:
#         statement = select(TermDB).where(TermDB.id == term_id) # Use TermDB
#         results = session.execute(statement)
#         term = results.scalars().first()
#         if not term:
#             raise HTTPException(status_code=404, detail="Term not found")
#         session.delete(term)
#         session.commit()
#         return {"result": "deleted successfully"}
#
# @app.get("/terms")
# def all_get_term():
#     with Session(engine) as session:
#         statement = select(TermDB) # Use TermDB
#         results = session.execute(statement)
#         terms = results.scalars().all()
#         return [Term(id=term.id, name=term.keyword, description=term.description) for term in terms]
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

from http.client import HTTPException
from typing import Optional, Union
from fastapi import FastAPI, HTTPException
from datetime import datetime
from pydantic import BaseModel, Field
from sqlmodel import Field as SQLModelField, Session, SQLModel, create_engine, select
import os

app = FastAPI()

# # Define the database model
# class TermDB(SQLModel, table=True):
#     id: Optional[int] = SQLModelField(default=None, primary_key=True)
#     keyword: str = SQLModelField(index=True, unique=True)
#     description: str = SQLModelField()
#     created_at: datetime = SQLModelField(default_factory=datetime.now)
#     updated_at: datetime = SQLModelField(default_factory=datetime.now)

# Define the API model
class Term(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)  # Removed unique constraint for BaseModel
    description: str = Field(default='error')

# # Database connection
# DATABASE_URL = os.environ.get("DATABASE_URL", 'mysql+pymysql://lera:1234@db/lab6')
# engine = create_engine(DATABASE_URL)
#
# # Create database tables
# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)
#
# # Startup event to create tables
# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()
#
# # Endpoint to get database connection info
# @app.get('/dbconnect')
# def get_db_info():
#     return str(engine)

# Endpoint to get a term by keyword
@app.get("/terms/{term}")
def get_term(term: str):
    with Session(engine) as session:
        statement = select(TermDB).where(TermDB.keyword == term)  # Use TermDB
        results = session.execute(statement)
        term = results.scalars().first()
        if not term:
            raise HTTPException(status_code=404, detail="Term not found")
        return term

# Endpoint to create a new term
@app.post("/terms", response_model=Term)
def post_term(term: Term):
    db_term = TermDB(keyword=term.name, description=term.description) # create TermDB object
    with Session(engine) as session:
        try:
            session.add(db_term)
            session.commit()
            session.refresh(db_term)
            return Term(id=db_term.id, name=db_term.keyword, description=db_term.description)  # return Term object
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=str(e))

# Endpoint to update a term
@app.put("/terms/{term_id}", response_model=Term)
def change_term(term_id: int, term_data: Term):
    with Session(engine) as session:
        statement = select(TermDB).where(TermDB.id == term_id) # Use TermDB
        results = session.execute(statement)
        term = results.scalars().first()
        if not term:
            raise HTTPException(status_code=404, detail="Term not found")

        term.keyword = term_data.name # Use TermDB's field
        term.description = term_data.description # Use TermDB's field
        session.commit()
        session.refresh(term)
        return Term(id=term.id, name=term.keyword, description=term.description) #return Term object

# Endpoint to delete a term
@app.delete("/terms/{term_id}")
def del_term(term_id: int):
    with Session(engine) as session:
        statement = select(TermDB).where(TermDB.id == term_id) # Use TermDB
        results = session.execute(statement)
        term = results.scalars().first()
        if not term:
            raise HTTPException(status_code=404, detail="Term not found")
        session.delete(term)
        session.commit()
        return {"result": "deleted successfully"}

# Endpoint to get all terms
@app.get("/terms")
def all_get_term():
    with Session(engine) as session:
        statement = select(TermDB) # Use TermDB
        results = session.execute(statement)
        terms = results.scalars().all()
        return [Term(id=term.id, name=term.keyword, description=term.description) for term in terms]

# Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}