from openerp import models, fields, api

class viewclasstwo(models.Model):
    _name='model.two'
    
    phone=fields.Integer(string="phone")
    
    