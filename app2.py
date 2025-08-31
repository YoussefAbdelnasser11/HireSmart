from fastapi import FastAPI, UploadFile, File, HTTPException
from hire_smart import extract_text_from_pdf, parse_cv_content

app = FastAPI(title="HireSmart API")

@app.post("/parse_cv/")
async def parse_cv(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    file_content = await file.read()
    cv_text = extract_text_from_pdf(file_content)
    
    output_data = parse_cv_content(cv_text)
    return output_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)