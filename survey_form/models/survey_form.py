from odoo import models, fields

class SurveyForm(models.Model):
    _name = 'survey.form'
    _description = 'Survey Form'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Title', required=True,tracking=True)
    dob = fields.Date('Release Date',tracking=True)
    qualification = fields.Char('Qualification',tracking=True)
    phone = fields.Char('Phone', required=True,tracking=True)
    email = fields.Char('Email', required=True,tracking=True)
