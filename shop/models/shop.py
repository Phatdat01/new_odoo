from odoo import api, fields, models

class ShopManagement(models.Model):
    _name = "shop.user"
    _inherit = ["mail.thread"]
    _description = "Book User"

    name = fields.Char(string="Name", required=True, tracking=True)
    dob = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([("male","Male"),("female","Female")], string="Gender", tracking=True)