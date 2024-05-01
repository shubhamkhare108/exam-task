from odoo import fields, models, api
from odoo.exceptions import UserError
from datetime import datetime, timedelta
import re

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        # Check and handle backdated orders
        if 'date_order' in vals:
            current_date = fields.Date.context_today(self)
            if isinstance(vals['date_order'], str):
                vals['date_order'] = fields.Date.from_string(vals['date_order'])
            if vals['date_order'] < current_date:
                raise UserError("You cannot create a backdated order.")

        # Format client_order_ref if provided
        if 'client_order_ref' in vals and isinstance(vals['client_order_ref'], str):
            vals['client_order_ref'] = self._format_client_order_ref(vals['client_order_ref'])

        return super(SaleOrder, self).create(vals)

    @api.model
    def _format_client_order_ref(self, ref):
        if isinstance(ref, str):
            # Remove any non-alphanumeric characters and replace them with dashes
            formatted_ref = re.sub(r'[^a-zA-Z0-9]', '-', ref)
            # Add dashes between letters and numbers
            formatted_ref = re.sub(r'([a-zA-Z])(\d)', r'\1-\2', formatted_ref)
            return formatted_ref
        return ref



    #for validating_date (expiration date)
    # @api.model
    # def create(self, vals):
    #     if 'date_order' in vals:
    #         date_order = fields.Datetime.from_string(vals['date_order'])
    #         current_datetime = datetime.now()
    #         if date_order < current_datetime:
    #             raise UserError("You cannot create a backdated order.")
    #         validity_date_str = vals.get('validity_date')
    #         if validity_date_str:
    #             validity_date = fields.Datetime.from_string(validity_date_str)
    #             min_validity_date = date_order + timedelta(days=5)
    #             if validity_date < min_validity_date:
    #                 raise UserError("Validity date must be at least 5 days ahead of the order date.")
    #     print('------->',validity_date_str)
    #     return super(SaleOrder, self).create(vals)
