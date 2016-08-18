
from openerp import models, fields, api


class CustomerFormWizard(models.TransientModel):

    _name = 'customer.form.wizard'
  
    session_id = fields.Many2one('customer.car',string="Session", required=True)
    locations=fields.Char("location")
    #attendee_ids = fields.Many2many('company.car', string="Attendees")
   
    @api.multi
    def subscribe(self):
        res = self.env['customer.car'].search([])
        for i in res:
            if i.customer_name==self.session_id.customer_name:
                i.address="PONDICHERRY CITY,PY,INDIA"
                val=i.address                    
                i.write({'address':val})
        return {}
    
  
    @api.multi
    def subscribe2(self):
        #form_views = self.env.ref('vechiclemanufacturer.wizard_form_views2', False)    
        res = self.env['customer.car'].search([])
        for i in res:
            if i.customer_name==self.session_id.customer_name:
                i.address="Chennai City, TN , INDIA"
                val=i.address
                i.write({'address':val})       
                
        form_views = self.env.ref('vechiclemanufacturer.wizard_form_views', False)        
        
        return {
                'name' :'wiz in customer wizard',
           'type': 'ir.actions.act_window',
           'res_model': 'customer.form.wizard',
           'view_mode': 'form',
           'views': [(form_views.id, 'form')],
           
           'target': 'new',
                } 
    
    
    
    
    
    
    
    
    
    
    
#     def _default_session(self):
#         return self.env['customer.car'].browse(self._context.get('active_id'))

    