from odoo import api, fields, models

class ShopAppointment(models.Model):
    _name = "shop.appointment"
    _inherit = ["mail.thread"]
    _description = "User Appointment"
    _rec_name_search = ["reference", "user_id"]
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
    total_qty = fields.Float(compute="_compute_total_qty", string="Total Quantity", store=True)
    date_of_birth = fields.Date(string="DOB", related="user_id.dob", store=True)

    @api.model_create_multi
    def create(self, vals_list):
        print("odoo mates", vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference']=="New":
                vals['reference'] = self.env['ir.sequence'].next_by_code('shop.appointment')
        return super().create(vals_list)
    
    @api.depends("appointment_line_ids","appointment_line_ids.qty")
    def _compute_total_qty(self):
        for rec in self:
            rec.total_qty = sum(rec.appointment_line_ids.mapped("qty"))
            # rec.total_qty = 0
            # for line in rec.appointment_line_ids:
            #     total_qty = total_qty+line.qty
            # rec.total_qty = total_qty
    
    def compute_display_name(self):
        for rec in self: 
            rec.display_name = f"[{rec.reference}] {rec.user_id.name}"
    
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
    product_id = fields.Many2one("product.product", string="Product", required=True)
    qty = fields.Float(string="Quantity")