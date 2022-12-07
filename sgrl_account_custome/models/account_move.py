# -*- coding: utf-8 -*-
# from odoo import fields, models, api
from pathlib import Path
import os
from PyPDF2 import PdfFileMerger, PdfFileReader
# import os
# from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
#
# from PyPDF2 import PdfFileReader, PdfFileWriter
# from page_objects import PageObject, PageElement
#
# pdf1File = ('pdf_files(Scan.pdf)')
# pdf1Reader = PdfFileReader(pdf1File)
#
# pages = []
# for pageNum in range(pdf1Reader.numPages):
#     pageObj = pdf1Reader.getPage(pageNum)
#     pages.append(pageObj)
#
# #Calculate width and height for final output page
# width = pages[1].mediaBox.getWidth() * 2
# height = pages[1].mediaBox.getHeight()
#
# merged_page = PageObject.createBlankPage(None, width, height)
# writer = PdfFileWriter()
# y =0
# merged_page = PageObject.createBlankPage(None, width, height)
# for page in range(len(pages)):
#     y+=1
#     if y%2!=0:
#         merged_page.mergePage(pages[page])
#         x=float(pages[page+1].mediaBox.getWidth())
#         merged_page.mergeScaledTranslatedPage(pages[page+1], 1,x, 0)
#     if y%2==0:
#         writer.addPage(merged_page)
#         merged_page = PageObject.createBlankPage(None, width, height)
#         y=0
#
# fname = os.path.splitext(os.path.basename(Path))[0]
# pdf = PdfFileReader(Path)
# input_paths = []
# for page in range(pdf.getNumPages()):
#         print("3333333333333333333333333",page)
#         pdf_writer = PdfFileWriter()
#         pdf_writer.addPage(pdf.getPage(page))
#         output_filename = 'hello.pdf'.format(fname, page+1)
#         input_paths.append(output_filename)
#         with open(output_filename, 'wb') as out:
#             print("###########################")
#             pdf_writer.write(out)
#
#         print('Created: {}'.format(output_filename))
#
#         # every 2 pages!
#         # Change the two if you need every other number of pages!
#         if page % 2 == 1:
#             print("++++++++++++++++++++++++++++++++")
#             pdf_merger = PdfFileMerger() #create pdfilemerger
#             for path in input_paths:
#                 print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
#                 pdf_merger.append(path) #read the single pages
#
#             # we call it pages_N-1_N, so first would be pages_0_1!
#             output_path = '{}_pages_{}_{}.pdf'.format(fname, page-1, page)
#             with open(output_path, 'wb') as fileobj:
#                 print("//////////////////////////////////////////")
#                 pdf_merger.write(fileobj) # write the two pages pdf!
#
#             input_paths = []
#
# if __name__ == '__main__':
#     print("------------------------------------")
#
# Path = '/home/odoo/Downloads/Tax_Invoice.pdf'
# pdf_splitter(path)


# "results" is a list containing

# class AccountMove(models.Model):
    # _inherit = "account.move"
    # _description = "Account move"
    #
    # lr_number = fields.Char(string="LR Number:")
    # lr_date = fields.Date(string="LR Date:")
    # motor_vehicle_no = fields.Char(string="Motor Vehicle No.")
    # dispatch_throug = fields.Char(string="Dispatch throug/Carrier name")
    # destination = fields.Char(string="Destination")
    # narration = fields.Text(string="Narration")
    # country = fields.Many2one('res.country', string="Country")
    # notify = fields.Many2one('res.partner', string="Notify")
    # container_no = fields.Char(string="Ontainer No.")
    # cont_seal_no = fields.Char(string="Cont Seal No.")
    # rfid_seal_no = fields.Char(string="Reld Seal No.")
    # freight = fields.Char(string="Freight")
    # insurance = fields.Char(string="Insurance")
    # export_under = fields.Selection(
    #     [('under duty drawback', 'Under Duty Drawback'), ('under advance license', 'Under Advance License')])
    # export_info = fields.Text(string="Export Info.")
    # gross_wight = fields.Float(string="Gross Wt.")
    # net_wight = fields.Float(string="Net Wt.")
    # eway_bill = fields.Char(string="Eway Bill no.")

    # merger = PdfFileMerger()
    # Downloads = ['Downloads/Scan.pdf', 'Downloads/4_4_merged.pdf']
    # print("\n\n\n\n",Downloads)
    # for pdf_file in Downloads:
    #     merger.append(pdf_file)
    # merger.write("hello_merged_2_pages.pdf")
    # print('\n\\n\n\n\n\n',merger.write)
    # merger.close()
#
# merge = PdfFileMerger()
# for items in  os.listdir():
#     print('---------------------',items)
#     if items.endswith('.pdf'):
#         merge.append(items)
#         print('3333333333333333333333',merge.append)
# merge.write("xyz_hello.pdf")
# merge.close()


#

pdf_dir = Path(__file__).parent / "pdf_files"
pdf_output_dir = Path(__file__).parent /"OUTPUT"
pdf_output_dir.mkdir(parents=True, exist_ok=True)
print("\n\n\n\n\n-------------------------------",pdf_output_dir)
pdf_files = list(pdf_dir.glob("*.pdf"))
keys = set([file.name[:3] for file in pdf_files])

BASE_FILE_NAME_LENGTH = 20
#
for key in keys:
    merger = PdfFileMerger()
    print("\n\n\n\n\n------23456789-------------------------",merger)
    for file in pdf_files:
        print("\n\n\n\n\n---------------------WERTYUIOJHBVB----------",file)
        if file.name.startswith(key):
            print("\n\n\n\n\n------------------asdfghjkl-------------",file.name)
            merger.append(PdfFileReader(str(file),"rb"))
            if len(file.name) >= BASE_FILE_NAME_LENGTH:
                print("33333333333333333333333333333")
                base_file_name = file.name
                print('00000000000000000000000000000000000000000000000',base_file_name)
                merger.write(str(pdf_output_dir / base_file_name))
        print("\n\n\n\n\n--===================-------------",merger.write)
        merger.close()
# merger = PdfFileMerger()
# path_to_files = r'Downloads/'
# for root, dirs, file_names in os.walk(path_to_files):
#     for file_name in file_names:
#         print("\n\n\n----------------")
#         merger.append(path_to_files + file_name)
# merger.write("merged_all_pages.pdf")
# print("======================",merger.write)
# merger.close()