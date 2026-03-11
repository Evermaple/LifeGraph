from fastapi import FastAPI
from analytics.charts import generate
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def home():

    generate()

    return FileResponse("charts_sleep.html")
