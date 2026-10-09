from fastapi import FastAPI

app = FastAPI(title="FastAPI Demo App")

@app.get("/")
def read_root():
    return {"message": "خوش آمدید! آپ کا FastAPI پراجیکٹ کامیابی سے چل رہا ہے۔"}
