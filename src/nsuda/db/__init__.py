from nsuda.db.database import engine
from nsuda.db import models

try:
    models.Base.metadata.create_all(bind=engine)
    print("Database initialized successfully")
    isDataBaseInited = True
except:
    print("Database initialized error")

