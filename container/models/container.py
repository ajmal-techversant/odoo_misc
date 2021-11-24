from odoo import fields, models, api


class Container (models.Model):
    _name = 'container.container'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    title = fields.Char(string="BL Tittle")
    log_no = fields.Char(string="Log No")
    diameter = fields.Float(string="Diameter")
    grade = fields.Char(string="Quality/Grade")
    length = fields.Float(string="Length")
    volume = fields.Float(string="Volume")
    container_no = fields.Char(string="Cont No.")
    


