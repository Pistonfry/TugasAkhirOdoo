from odoo import api, fields, models    

class attendaces(models.Model):
    _name="attendance.data"
    _description="Track attendance data of employees."

    emp_id=fields.Char(string='ID')
    name=fields.Char(string='Name',
                      required=True)
                    #   tracking=True)
    check_in=fields.Char()
    check_out=fields.Char()
    work_hours=fields.Char()