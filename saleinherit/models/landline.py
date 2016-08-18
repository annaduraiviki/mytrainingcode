from openerp import models, fields, api

class SaleInherit(models.Model):
    _name='res.partner'
    
    _inherit='res.partner'
    
    sale_percentage=fields.Float(size=14,string="Percentage")
    last_name=fields.Char(size=14,string="LastName")
    full_name=fields.Char(compute="fullname")
    surname_select=fields.Many2one("surname.selection",string="Surname")
    home_address=fields.Text(string="Home Address")
    priority_name=fields.Selection([('0', 'very low'), ('1', 'low'), ('2', 'medium'), ('3', 'high'), ('4', 'very high'), ('5', 'highest')], string="Priority",default='2')
    
    @api.one
    @api.depends('name','last_name')
    def fullname(self):
        if self.name or self.last_name:
            self.full_name= str(self.name)+'   '+str(self.last_name)
            self.full_name=str(self.full_name).upper()
     
class SurName(models.Model):
    _name="surname.selection"
    _rec_name="surname"
    
    surname=fields.Char("Surname")
    
