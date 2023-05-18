# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RegistrationForm(models.Model):
    _inherit = "res.partner"
    # _inherit = "res.users"

    phone_number = fields.Integer()

    @api.model
    def create(self, vals):
        res = super(RegistrationForm, self).create(vals)
        # create a partner
        partner_obj = self.env['res.partner']
        partner = partner_obj.create({
            'name': vals['name'],
            'phone': vals['phone_number'],  # Set the phone number
            'email': vals.get('email', False),
            'user_id': res.id,
        })
        return res