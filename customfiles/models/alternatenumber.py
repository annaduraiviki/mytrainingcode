from openerp import models,fields,api


class alternatenumber(models.Model):
    
    
    
    _inherit='customercustom.vms'
    
    alternate_number=fields.Char(size=10,string="Alternate number")
    
    

