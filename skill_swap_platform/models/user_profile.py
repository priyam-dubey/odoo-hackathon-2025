from odoo import models, fields

class UserProfile(models.Model):
    _name = 'skill.user'
    _description = 'User Profile'

    name = fields.Char(string="Name", required=True)
    location = fields.Char(string="Location")
    profile_photo = fields.Binary(string="Profile Photo")
    skills_offered_ids = fields.Many2many('skill.skill', string="Skills Offered")
    skills_wanted_ids = fields.Many2many('skill.skill', string="Skills Wanted")
    availability = fields.Selection([
        ('weekends', 'Weekends'),
        ('evenings', 'Evenings'),
        ('anytime', 'Anytime')
    ], default='anytime')
    is_public = fields.Boolean(string="Public Profile", default=True)
