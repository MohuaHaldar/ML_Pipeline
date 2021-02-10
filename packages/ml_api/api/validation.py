from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t


class InvalidInputError(Exception):
    """ Invalid model inputs"""


class TitanicDataRequestSchema(Schema):
    PassengerId = fields.Integer()
    Pclass = fields.Integer()
    Name = fields.Str()
    Sex = fields.Str()
    Age = fields.Float()
    SibSp = fields.Integer()
    Parch = fields.Integer()
    Ticket = fields.Str()
    Fare = fields.Float()
    Cabin = fields.Str()
    Embarked = fields.Str()


def _filter_error_rows(errors: dict, validated_input: t.List[dict]) -> t.List[dict]:
    indexes = errors.keys()
    for index in sorted(indexes, reverse=True):
        del validated_input[index]
    return validated_input


def validate_inputs(input_data):
    schema = TitanicDataRequestSchema(strict=True, many=True)
    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages
    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
