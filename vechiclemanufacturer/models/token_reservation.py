from openerp import models,fields,api
import time


class tokenreservation(models.Model):
    _name="token.vechicle"
    
    _defaults= {'date_display': lambda *a: time.strftime('%Y-%m-%d'),}
    
    customer_id=fields.Many2one("customer.car",string="Customer ID",required=True)
    seq_numb=fields.Char(string="order",readonly=True)
    reserve_token=fields.Many2one("selecttoken.vechicle",string="Allot Token")
    date_display=fields.Date(string="Date")
    quantity=fields.Integer(string="Quantity")
    quantity_no=fields.Integer(compute="quantity_value")
    deduction=fields.Integer(string="Deduct")
    samp_cal1=fields.Integer(string="a")
    samp_cal2=fields.Integer(string="b")
    samp_cal3=fields.Integer(string="c",readonly=True)
    
    @api.onchange('samp_cal1','samp_cal2')
    def adding_samp(self):
        self.samp_cal3=self.samp_cal1+self.samp_cal2
        
    @api.model
    def create(self,vals):
        if  self.samp_cal3:    
            vals['samp_cal3']=self.samp_cal1+self.samp_cal2
        res = super(tokenreservation, self).create(vals)    
        return  res    
        
    @api.multi
    def write(self,vals):
        if not self.samp_cal3:
            vals['samp_cal3'] = self.samp_cal1+self.samp_cal2
#            vals['samp_cal3'] = vals['samp_cal1']+vals['samp_cal2']  
                        
        res = super(tokenreservation, self).write(vals) 
        return res
        
    _defaults={'seq_numb':lambda obj,cr,uid,context:obj.pool.get('ir.sequence').get(cr,uid,'token.vechicle'),}


    @api.one
    @api.depends('deduction','quantity')
    def quantity_value(self):
        self.quantity_no=self.quantity-self.deduction
   
class selecttoken(models.Model):    
    _name="selecttoken.vechicle"
    _rec_name="select_token"
    
    no_slots=fields.Integer(string="Slots available",default=10,copy=False)
    select_token=fields.Integer(compute="numb_token",string="Select Token",required=True,copy=False)
     
    @api.one
    @api.depends('no_slots')
    def numb_token(self):
        i=0       
        if i<=10:
            for i in range(self.no_slots):
                self.select_token= int(i)+1
     
     
    
    
    