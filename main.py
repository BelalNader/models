import warnings
warnings.filterwarnings('ignore')
import os  # Importing the os module for interacting with the operating system
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import logging
logging.getLogger('tensorflow').disabled = True
from fastapi import FastAPI, UploadFile, File
from color import get_colour_name # type: ignore
from mony import cash_detector
import io
import tempfile

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/extract-colors")
async def extract_colors_from_image(image: UploadFile = File(...)):
    colors = get_colour_name(image.file)
    return {"colors": colors}



@app.post("/cash-detector")
async def extract_cash_from_image(image: UploadFile = File(...)):
    # Check if the input is a valid file-like object
    if not isinstance(image.file, io.IOBase):
        return {"error": "Invalid input type. Please upload a valid image file."}

    # Convert the file-like object to bytes
    image_bytes = await image.read()

    # Pass the bytes to the ocr_core function
    cash = cash_detector(image_bytes)

    return {"Cash": cash}
