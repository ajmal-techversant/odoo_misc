# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    order_type_id = fields.Many2one('sale.order.type',  string="Sale Order Type")

    @api.model
    def create(self, vals):
        if 'company_id' in vals:
            self = self.with_company(vals['company_id'])
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            order_type = self.env['sale.order.type'].search([('id', '=', vals['order_type_id'])])
            if order_type:
                if not order_type.sequence_id:
                    raise UserError(_("Please set a sequence on Order"))
                vals['name'] = self.env['ir.sequence'].next_by_code(order_type.sequence_id.code, sequence_date=seq_date) or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('sale.order', sequence_date=seq_date) or _('New')
        return super(SaleOrder, self).create(vals)


class SaleOrderType(models.Model):
    _name = "sale.order.type"

    name = fields.Char(string="Order Type")
    sequence_id = fields.Many2one('ir.sequence', string="Sequence")




