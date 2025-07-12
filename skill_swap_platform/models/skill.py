from odoo import models, fields

class Skill(models.Model):
    _name = 'skill.skill'
    _description = 'Skill'

    name = fields.Char(string="Skill Name", required=True)
    description = fields.Text(string="Description")
