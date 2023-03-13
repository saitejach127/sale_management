# Copyright (c) 2023, metamenu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Sales(Document):
	pass

@frappe.whitelist()
def getSiteItems(site_name):
	fields = frappe.get_all('Site Item', filters={'catering_site_id': site_name})
	return fields

@frappe.whitelist()
def getUserCateringSite():
	useremail = frappe. get_user(). doc.email
	name = frappe.get_all('Catering Site', filters={'manager': useremail}, fields=['name'])
	if len(name) > 0:
		return name[0].name
	return ''
