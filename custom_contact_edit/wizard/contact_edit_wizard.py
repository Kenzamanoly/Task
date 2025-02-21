from odoo import models, fields, api

class ContactEditWizard(models.TransientModel):
    _name = 'contact.edit.wizard'
    _description = 'Wizard for Editing Contacts'

    partner_id = fields.Many2one('res.partner', string="Contact", required=True)
    name = fields.Char(string="Name", related="partner_id.name", readonly=False)
    email = fields.Char(string="Email", related="partner_id.email", readonly=False)
    phone = fields.Char(string="Phone", related="partner_id.phone", readonly=False)

    def action_open_edit_wizard(self):
        """Opens the Edit Wizard"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Edit Contact',
            'res_model': 'contact.edit.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_partner_id': self.id}
        }

    def save_contact_changes(self):
        """Save changes to the contact"""
        self.partner_id.write({
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
        })
        return {'type': 'ir.actions.act_window_close'}
