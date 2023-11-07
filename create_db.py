from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

def create_table():

    # Define your SQLAlchemy engine
    engine = create_engine('sqlite:///weather.db', echo=True)

    # Define your table
    metadata = MetaData()
    city_table = Table(
        'city',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
    )

    # Create the table in the database
    metadata.create_all(engine)