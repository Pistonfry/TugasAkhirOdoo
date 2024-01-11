from odoo import api, fields, models,_
from odoo.exceptions import ValidationError

class HostpitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit='mail.thread'
    _description = "Patient Records"

    name=fields.Char(string='Name',
                     required=True, 
                     tracking=True)
    age = fields.Integer(string="Age", 
                         tracking=True)
    is_child = fields.Boolean(string="Is Child ?", 
                              tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Others")],
        string="Gender", 
        tracking=True)
    capitalized_name=fields.Char(string='Capitalized Name', 
                                 compute='_compute_capitalized_name', 
                                 store=True)
    
    #Check if it's child, age must be filled
    @api.constrains('is_child','age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recoded !"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name=self.name.upper()
            else:
                rec.capitalized_name=''

    @api.onchange('age')
    def _onchance_age(self):
        if self.age <=10:
            self.is_child = True
        else:
            self.is_child = False