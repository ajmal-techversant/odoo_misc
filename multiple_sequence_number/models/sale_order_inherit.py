# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    order_type_id = fields.Many2one('sale.order.type',  string="Sequence")

    @api.model
    def create(self, vals):
        if 'company_id' in vals:
            self = self.with_company(vals['company_id'])
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            order_type = self.env['sale.order.type'].search([('id', '=', vals['order_type_id'])])
            if not order_type.sequence_id:
                raise UserError(_("Please set a sequence first"))
            if order_type.name == 'Consumer':
                vals['name'] = self.env['ir.sequence'].next_by_code(order_type.sequence_id.code, sequence_date=seq_date) or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('sale.order', sequence_date=seq_date) or _('New')
        return super(SaleOrder, self).create(vals)


class SaleOrderType(models.Model):
    _name = "sale.order.type"

    name = fields.Char(string="OrderType")
    sequence_id = fields.Many2one('ir.sequence', string="Sequence")




