

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class test(models.Model):
    _name = 'test.test'
    _description = 'test.test'

    name = fields.Char(required=True, index=True)
    address_street = fields.Char(string='Street Name')
    address_building = fields.Char(string='Building')
    address_floor_room = fields.Char(string='Floor/Room')
    address_street2 = fields.Char(string='Street 2')
    address_city = fields.Char(string='City')
    address_zip = fields.Char(string='ZIP')
    address_phone = fields.Char(string='Phone')
    address_email = fields.Char(string='Email', validate=lambda self, value: tools.email_normalize(value))
    state_id = fields.Many2one('res.country.state', string='State', domain="[('country_id', '=', county_id)]")
    county_id = fields.Many2one('res.country', string='County',required=True,)

    @api.constrains('address_phone')
    def _check_phone_number_length(self):
        for record in self:
            if record.address_phone and not record.address_phone.isdigit():
                raise ValidationError("Phone number should contain only digits.")
            if record.address_phone and len(record.address_phone) != 10:
                raise ValidationError("Phone number should be 10 digits long.")


# note do no how to use this but inbild odoo feture or method 'phone_validation'