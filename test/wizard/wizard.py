from odoo import fields, models, api


class Testwizardtask(models.TransientModel):
    _name="test.testwizard"

    name = fields.Char()
