# Copyright (c) 2023, metamenu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Sales(Document):
	pass

@frappe.whitelist()
def getSiteItems(site_name):
	fields = frappe.get_doc('Catering Site', site_name)
	print(fields, "fields")
	return fields.items

@frappe.whitelist()
def getUserCateringSite():
	useremail = frappe. get_user(). doc.email
	name = frappe.get_all('Catering Site', filters={'manager': useremail}, fields=['name'])
	print(useremail)
	if len(name) > 0:
		return name[0].name
	return ''