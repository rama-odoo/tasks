from odoo import models,fields,_,api
from odoo.exceptions import UserError

class HrApplicant(models.Model):
    _inherit = "hr.applicant"

    def archive_applicant(self):
        for res in self:
            print("\n\n\n value is delete")
            res.partner_id.unlink()
        return super().archive_applicant()


    def unlink(self):
        res = super(HrApplicant, self).unlink()

        print("\n\n\n unlink vale is delete",res)
        return res
        