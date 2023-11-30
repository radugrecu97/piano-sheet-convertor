from fastapi import FastAPI, File, UploadFile
import consts
import processor
import util

app = FastAPI()

# Load configuration
cfg = util.getYamlDict(f'{consts.ROOT_DIR}/assets/config.yaml')

@app.post("/uploadfile/")
async def createUploadFile(file: UploadFile = File(...)):
    # processor.processFile()
    return {"filename": file.filename}
