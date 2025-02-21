from odoo import models, fields, api



class ContactArchiveWizard(models.TransientModel):
    _name = 'contact.archive.wizard'
    _description = 'Wizard for Archiving Contacts'

    partner_id = fields.Many2one('res.partner', string="Contact", required=True)

    def confirm_archive(self):
        """Archives the selected contact"""
        self.partner_id.active = False
        return {'type': 'ir.actions.act_window_close'}

class ResPartner(models.Model):
    _inherit = 'res.partner'

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

    def action_open_archive_wizard(self):
        """Opens the Archive Confirmation Wizard"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Confirm Archive',
            'res_model': 'contact.archive.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_partner_id': self.id}
        }

