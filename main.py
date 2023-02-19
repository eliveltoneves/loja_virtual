from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request




app = FastAPI(docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount('/media', StaticFiles(directory='media'), name='media')


@app.get('/')
async def index(request: Request):
    context = {
        "request": request
    }

    return templates.TemplateResponse('index.html', context=context)

@app.get('/diferenciais')
async def diferenciais(request: Request):
    context = {
        "request": request
    }

    return templates.TemplateResponse('diferenciais.html', context=context)

@app.get('/produtos')
async def produtos(request: Request):
    context = {
        "request": request
    }

    return templates.TemplateResponse('produtos.html', context=context)

@app.get('/login')
async def login(request: Request):
    context = {
        "request": request
    }

    return templates.TemplateResponse('login.html', context=context)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)