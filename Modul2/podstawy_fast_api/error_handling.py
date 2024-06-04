from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette import status

app = FastAPI()

# 1
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     item = {"item_id": item_id, "name": "Foo"}
#     item = None
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item


# 2
# class Item(BaseModel):
#     name: str

# @app.post("/items")
# async def create_item(item: Item):
#     if item.name is None:
#         raise HTTPException(status_code=400, detail="Name is required")
#     return item


# 3
# @app.exception_handler(HTTPException)
# def handle_http_exception(request: Request, exc: HTTPException):
#     return {"message": str(exc.detail)}


# 4
# @app.exception_handler(ValidationError)
# def validation_error_handler(request: Request, exc: ValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_400_BAD_REQUEST,
#         content={"message": "Invalid input data"}
#     )

# @app.exception_handler(HTTPException)
# def http_exception_handler(request: Request, exc: HTTPException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"message": exc.detail},
#     )

# @app.exception_handler(Exception)
# def unexpected_exception_handler(request: Request, exc: Exception):
#     return JSONResponse(
#         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#         content={"message": "An unexpected error occurred"},
#     )

# class Item(BaseModel):
#     name: str


# @app.post("/items/")
# async def create_item(item: Item):
#     if item.price < 0:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Price should be a positive number",
#         )
#     return item

# 5
class ItemNotFoundError(Exception):
    pass

@app.exception_handler(ItemNotFoundError)
def item_not_found_error_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": "Item not found"},
    )

def get_item_by_id(item_id: int):
    # This is a placeholder for your actual data source
    items = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
    ]

    # Find the item with the matching ID
    for item in items:
        if item["id"] == item_id:
            return item

    # If no item was found, return None
    return None

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = get_item_by_id(item_id)
    if item is None:
        raise ItemNotFoundError
    return item
