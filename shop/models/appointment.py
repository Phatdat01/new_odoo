from odoo import api, fields, models

class ShopAppointment(models.Model):
    _name = "shop.appointment"
    _inherit = ["mail.thread"]
    _description = "User Appointment"
    _rec_name="user_id"

    reference = fields.Char(string="Reference", default="New")
    user_id = fields.Many2one("shop.user", string="User", tracking=True)
    date_appointment = fields.Date(string="Date")
    note = fields.Text(string="Note")
    state = fields.Selection([("draft","Draft"),("confirmed","Confirmed"),
        ("ongoing","Ongoging"),("done","Done"),("cancel","Cancel"),                        
    ], default="draft", tracking=True)
    appointment_line_ids = fields.One2many(
        "shop.appointment.line","appointment_id",string="Lines"
    )

    @api.model_create_multi
    def create(self, vals_list):
        print("odoo mates", vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference']=="New":
                vals['reference'] = self.env['ir.sequence'].next_by_code('shop.appointment')
        return super().create(vals_list)
    
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_ongoging(self):
        for rec in self:
            rec.state = 'ongoing'

    def action_done(self):
        for rec in self:
            rec.state = 'done'
    
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

class ShopAppointmentLines(models.Model):
    _name="shop.appointment.line"
    _description="User appointment Lines"

    appointment_id = fields.Many2one("shop.appointment", string="Appointment")
    product_id = fields.Many2one("product.product", string="Product")
    qty = fields.Float(string="Quantity")