from openerp import models, fields, api


class CustomerFormWizard(models.TransientModel):

    _name = 'customer.form.wizard2'
    _inherit= "customer.car"

    session_id = fields.Many2one('customer.car',string="Session", required=True)
    area=fields.Char("location")
    
    
    @api.multi
    def subscribe2(self):
      
        return {
                   'name': _('Journal Items'),
                   'view_type': 'form',
                   'view_mode': 'tree',
                   'res_model': 'customer.form.wizard2',
                  # 'view_id': wizard_form_views2,
                  'target' :'new',
                   'type': 'ir.actions.act_window',
                   
                   }
         
    
