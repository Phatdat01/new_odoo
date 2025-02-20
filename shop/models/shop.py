from odoo import api, fields, models

class ShopManagement(models.Model):
    _name = "shop.user"
    _inherit = ["mail.thread"]
    _description = "Book User"

    name = fields.Char(string="Name", required=True, tracking=True)
    dob = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([("male","Male"),("female","Female")], string="Gender", tracking=True)

    tag_ids = fields.Many2many("shop.tag","shop_tag_rel","user_id","tag_id",string="Tags")

    product_ids = fields.Many2many("product.product",string="Products")