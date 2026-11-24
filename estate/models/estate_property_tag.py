from random import randint

from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tags of Properties"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer(default=lambda _: randint(1, 11))

    _check_name_unique = models.Constraint(
        "unique(name)",
        "The Tag's name must be unique."
    )
