from datetime import date
from datetime import datetime


def json_serializer(obj):
    """JSON serializer for objects not serializable by default json code

    Args:
        obj (obj): the object to be serialized

    Returns:
        str: Description

    Raises:
        TypeError: Type is not serializable
    """
    if isinstance(obj, (datetime, date)):
        serial = obj.isoformat()
        return serial
    raise TypeError("Type %s not serializable" % type(obj))
