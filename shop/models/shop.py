from odoo import api, fields, models

class ShopManagement(models.Model):
    _name = "shop.user"
    _inherit = ["mail.thread"]
    _description = "Book User"

    name = fields.Char(string="Name", required=True, tracking=True)
    dob = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([("male","Male"),("female","Female")], string="Gender", tracking=True)
    
    reference = fields.Char(string="Reference", default="New")
    user_id = fields.Many2one("shop.user", string="User", tracking=True)
    date_appointment = fields.Date(string="Date")
    note = fields.Text(string="Note")
    state = fields.Selection([("draft","Draft"),("confirmed","Confirmed"),
        ("ongoing","Ongoging"),("done","Done"),("cancel","Cancel"),                        
    ], default="draft", tracking=True)

    tag_ids = fields.Many2many("shop.tag","shop_tag_rel","user_id","tag_id",string="Tags")

    product_ids = fields.Many2many("product.product",string="Products")