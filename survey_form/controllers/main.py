from odoo import http
from odoo.http import request

class Survey(http.Controller):

    @http.route('/survey', auth='public', website=True)
    def survey(self, **kwargs):
        submitted = kwargs.get('submitted')
        return request.render('survey_form.survey_form_template', {
            'submitted': submitted
        })

    @http.route('/survey_form', type='http', auth="public", website=True, csrf=True)
    def survey_form(self, **post):
        name = post.get('name')
        email = post.get('email')
        phone = post.get('phone')
        dob = post.get('dob')
        qualification = post.get('qualification')

        if name and email and phone:
            request.env['survey.form'].sudo().create({
                'name': name,
                'email': email,
                'phone': phone,
                'dob': dob,
                'qualification': qualification
            })
            return request.redirect('/survey?submitted=1')
        return request.render('survey_form.survey_form_template', {
            'submitted': False
        })
