from odoo import api, fields, models

class HostpitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Records"

    name=fields.Char(string='Name',required=True)
    age = fields.Integer(string="Age")
    is_child = fields.Boolean(string="Is Child ?")
    notes = fields.Text(string="Notes")
    gender = fields.Selection([
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Others")],
        string="Gender")