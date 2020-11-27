from django.db.models import CharField
import json


class JsonField(CharField):
    def __init__(
            self,
            *,
            max_length=10000,
            **kwargs,
    ):
        super().__init__(max_length=max_length, **kwargs)

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def to_python(self, value):
        if isinstance(value, dict):
            return value

        if value is None:
            return value
        return json.loads(value)

    def get_prep_value(self, value):
        return json.dumps(value)
