from fastapi import FastAPI, UploadFile, File
from color import get_colour_name #ignore

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/extract-colors")
async def extract_colors_from_image(image: UploadFile = File(...)):
    colors = get_colour_name(image.file)
    return {"colors": colors}