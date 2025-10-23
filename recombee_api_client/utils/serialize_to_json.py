from datetime import datetime


def serialize_to_json(val):
    if hasattr(val, "to_dict") and callable(val.to_dict):
        return val.to_dict()
    elif isinstance(val, datetime):
        return val.isoformat()
    return val
