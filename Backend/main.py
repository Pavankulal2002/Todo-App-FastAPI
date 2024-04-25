from fastapi import FastAPI
from routes import mysql_routes,mongodb_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



app.include_router(mysql_routes.router, prefix="/mysql")
app.include_router(mongodb_routes.router, prefix="/mongodb")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# from config.openapi import tags_metadata

# app = FastAPI(
#     title="todos API",
#     description="a REST API using python and mysql",
#     version="0.0.1",
#     openapi_tags=tags_metadata,
# )


