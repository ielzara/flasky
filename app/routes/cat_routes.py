from flask import Blueprint, abort, make_response, request
from ..db import db
from app.models.cat import Cat

cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")

@cats_bp.post("")
def create_cat():
    request_body = request.get_json()
    name = request_body["name"]
    color = request_body["color"]
    personality = request_body["personality"]


    new_cat = Cat(name=name, color=color, personality=personality)
    db.session.add(new_cat)
    db.session.commit()

    response = {
        "id": new_cat.id,
        "name": new_cat.name,
        "color": new_cat.color,
        "personality": new_cat.personality,
    }
    return response, 201

@cats_bp.get("")
def get_all_cats():
    query = db.select("Cat").order_by("Cat.id")
    cats = db.session.scalars(query)

    cats_response = [cat.to_dict() for cat in cats]
    return cats_response



    
# @cats_bp.get("")
# def get_all_cats():
#     results_list = []

#     for cat in cats:
#         results_list.append(dict(
#             id=cat.id,
#             name=cat.name,
#             color=cat.color,
#             personality=cat.personality
#         ))

#     return results_list

# def validate_cat(cat_id):
#     try:
#         cat_id = int(cat_id)
#     except:
#         response = {"message": f"cat {cat_id} invalid"}
#         abort(make_response(response, 400))

#         for cat in cats:
#             if cat.id == cat_id:
#                 return cat

#     response = {"message": f"cat {cat_id} not found"}
#     abort(make_response(response, 404))

# @cats_bp.get("/<cat_id>")
# def get_one_cat(cat_id):
#     cat = validate_cat(cat_id)
#     return cat.to_dict(), 200
