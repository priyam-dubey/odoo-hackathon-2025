from odoo import models, fields

class SwapRequest(models.Model):
    _name = 'skill.swap'
    _description = 'Swap Request'

    requester_id = fields.Many2one('skill.user', string="Requester", required=True)
    receiver_id = fields.Many2one('skill.user', string="Receiver", required=True)
    offered_skill_id = fields.Many2one('skill.skill', string="Skill Offered", required=True)
    requested_skill_id = fields.Many2one('skill.skill', string="Skill Requested", required=True)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], default='pending')
    
