from typing import Any


def all_thing_is_obj(object: Any) -> int:
    ty = type(object)
    if (ty == list):
        print("List :", ty)
    elif (ty == tuple):
        print("Tuple :", ty)
    elif (ty == set):
        print("Set :", ty)
    elif (ty == dict):
        print("Dict :", ty)
    elif (ty == str):
        print(object, "is in the kitchen :", ty)
    else:
        print("Type not found")
    return 42
