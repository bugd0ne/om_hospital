from odoo import fields, api, models

class HospitalPatient(models.Model):

    _name = "hospital.patient"
    _description = "Hospital Patient"

    first_name = fields.Char(string="First Name", required="True")
    last_name = fields.Char(string="Last Name", required="True")
    uin = fields.Integer(string="UIN")
    date_of_birth = fields.Date(string="Birth date")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    note = fields.Text(string="Patient's notes")