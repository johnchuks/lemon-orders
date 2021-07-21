from fastapi import FastAPI, Body

from app.models import Order


app = FastAPI()


@app.post("/orders/")
async def create_stock_orders(order: Order = Body(..., embed=True)):
    return {"order": order}
