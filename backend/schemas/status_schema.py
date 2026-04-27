from apiflask import Schema
from apiflask.fields import Srting, Integer


class StatusOutSchema(Schema):
    status = String()
    message = String()
    service = String()
    items_count = Integer()