from fastapi import FastAPI

app = FastAPI(title="Speats API")

@app.get("/health")
def health():
    return {"status": "ok", "service": "speats-api"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Ciao {name}!"}


@app.get("/test")
def test():
    return {"test": "ok", "version": "1.0.1", "message": "Endpoint aggiunto da locale!"}
