from odoo import api, fields, models

class HostpitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit='mail.thread'
    _description = "Patient Records"

    name=fields.Char(string='Name',required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    is_child = fields.Boolean(string="Is Child ?", tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Others")],
        string="Gender", tracking=True)
    
    @api.onchange('age')
    def _onchance_age(self):
        if self.age <=10:
            self.is_child = True
        else:
            self.is_child = False