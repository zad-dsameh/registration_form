from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
import logging

_logger = logging.getLogger(__name__)


class ExtendedAuthSignupHome(AuthSignupHome):

    def do_signup(self, qcontext):
        try:
            """Override do_signup to create a partner record and save the custom field value"""
            res = super(ExtendedAuthSignupHome, self).do_signup(qcontext)
            if res.qcontext.get('uid'):
                user = request.env['res.users'].sudo().browse(res.qcontext['uid'])
                partner = request.env['res.partner'].sudo().create({
                    'name': user.name,
                    'email': user.email,
                    'mobile_field': int(request.params.get('mobile_field', 0)),
                    'phone_field': int(request.params.get('phone_field', 0)),
                })
                user.partner_id = partner.id
        except Exception as e:
            _logger.exception('Error during signup: %s', str(e))

        return res
