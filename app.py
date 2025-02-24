from fastapi import FastAPI, UploadFile, File
import whisper
import os

app = FastAPI()
model = whisper.load_model("medium")  # You can change to "small", "medium", "large" as needed

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # Transcribe the audio
    result = model.transcribe(temp_path)
    transcription = result["text"]
    
    # Clean up
    os.remove(temp_path)
    
    return {"transcription": transcription}

@app.get("/")
async def root():
    return {"message": "Whisper HTTP API is running"}