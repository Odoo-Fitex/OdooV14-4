# -*- coding: utf-8 -*-
from odoo import models, fields, api
 

# class action_routing_operation(models.Model):
#     _name = 'router.operation'
 
#     name = fields.Char(string="Operation Name")
#     workcenter_id = fields.Many2one('mrp.workcenter', 'Work Center', required=True, check_company=True, store=True)
#     time_cycle_manual = fields.Float(
#         'Manual Duration', default=60,
#         help="Time in minutes. Is the time used in manual mode, or the first time supposed in real time when there are not any work orders yet.")
#     company_id = fields.Many2one(
#         'res.company', 'Company', store=True)



# class action_routing_operation_name(models.Model):
#     _inherit = 'mrp.routing.workcenter'
    
#     operation_name = fields.Many2one(
#         'router.operation', string="Operation")
    
#     company_id = fields.Many2one( string="Company",
#         compute='onchange_routing_operation_name')
# #     company_id2 = fields.Many2one(
# #         'res.company', 'Company',
# #         readonly=True, related='routing_id.company_id', store=True)
#     workcenter_id = fields.Many2one('mrp.workcenter', 'Work Center',
#                                      readonly=True, related='operation_name.workcenter_id')
#     time_cycle_manual = fields.Float(
#         'router.operation', 'Duration',
#         readonly=False, related='operation_name.time_cycle_manual', store=True)


#     @api.onchange('operation_name')
#     def onchange_routing_operation_name(self):
#         if self.operation_name:
#             self.name = self.operation_name.name
#             self.company_id = self.company_id2
#         else:
#             self.name = 0
#             self.company_id = 0
            
class action_bom_name(models.Model):
    _inherit = 'mrp.bom'
    name = fields.Many2one('mrp.routing.workcenter')
