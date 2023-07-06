from typing import List, Optional, Dict
from fastapi import FastAPI
from database import items_collection
from model import Item
from bson.objectid import ObjectId
import asyncio


async def read_items() -> List[Item]:
    items = []
    for item in items_collection.find():
        items.append(item)
    return items


async def read_item_by_id(item_id: str) -> Item:
    item = items_collection.find_one({"id", ObjectId(item_id)})
    if item:
        return item
    return None


async def create_item(item: Item) -> Item:
    item_dict = item.dict()
    result = items_collection.insert_one(item_dict)
    item_dict['_id'] = str(result.inserted_id)
    return Item(**item_dict)


async def update_item(
        item_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        price: Optional[str] = None,
        is_offer: Optional[bool] = None) -> Dict:
    item_dict = []
    if name is not None:
        item_dict["name"] = name
    if name is not None:
        item_dict["description"] = description
    if name is not None:
        item_dict["price"] = price
    if name is not None:
        item_dict["is_offer"] = is_offer

    result = items_collection.update_one(
        {"_id": ObjectId(item_id)}, {"$set": item_dict}
    )
    if result.modified_count == 0:
        return None
    return {"message": "Resume upadet success"}


async def delete_item(item_id: str) -> bool:
    result = items_collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0


# async def multiply_numbers(x: int, y: int) -> int:
#     await asyncio.sleep(5)
#     result = x * y
#     return result


# @app.get("/multiply")
# async def multiply_endpoint(x: int, y: int) -> int:
#     return await multiply_numbers(x, y)


# @app.get("/add")
# def add_numbers(x: int, y: int) -> int:
#     return x+y
