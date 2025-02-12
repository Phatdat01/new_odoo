from odoo import api, fields, models

class ShopTag(models.Model):
    _name = "shop.tag"
    _description = "Shop Tag"
    _order = "sequence,id"

    name = fields.Char(string="Name", required=True)

    sequence = fields.Integer(default=10)