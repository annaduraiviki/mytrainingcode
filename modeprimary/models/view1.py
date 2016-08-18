from openerp import models, fields, api

class viewclassone(models.Model):
    _name="personal.details"
    _inherit="personal.details"
    
    msg=fields.Text(string="Text's")
    #phone=fields.Integer()