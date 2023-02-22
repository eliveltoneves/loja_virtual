from fastapi import APIRouter
from fastapi import Request

from core.configs import settings

router = APIRouter()


@router.get('/')
async def index(request: Request):
    context = {
        "request": request
    }

    return settings.TEMPLATES.TemplateResponse('index.html', context=context)

@router.get('/diferenciais')
async def diferenciais(request: Request):
    context = {
        "request": request
    }

    return settings.TEMPLATES.TemplateResponse('diferenciais.html', context=context)

@router.get('/produtos')
async def produtos(request: Request):
    context = {
        "request": request
    }

    return settings.TEMPLATES.TemplateResponse('produtos.html', context=context)

@router.get('/login')
async def login(request: Request):
    context = {
        "request": request
    }

    return settings.TEMPLATES.TemplateResponse('login.html', context=context)