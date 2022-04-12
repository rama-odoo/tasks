from odoo import models


class HrApplicant(models.Model):
    _inherit = "hr.applicant"

    def archive_applicant(self):
        for res in self:

            res.partner_id.unlink()
        return super().archive_applicant()

    def unlink(self):
        res = super(HrApplicant, self).unlink()

        return res
