from openerp import models, fields, api

class ProjectIssue(models.Model):
    
    _inherit='project.issue'
    
    
    
    
    def valuedef(self):
        res=self.env['project.task'].browse(['name','=',self.name])
        for i in res:
            if self.name:
                i.name=self.name
                val=i.name                   
                i.write({'name':val})
        return {}
             
         
             
    
    