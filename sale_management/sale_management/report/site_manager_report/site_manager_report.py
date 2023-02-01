# Copyright (c) 2023, metamenu and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe import msgprint
from datetime import datetime

def execute(filters=None):
	if not filters: filters = {}
	columns, data = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		msgprint(_('No Records Found'))
		return columns, cs_data

	data = cs_data

	chart = get_chart_data(data)
	report_summary = get_report_summary(data, filters)

	return [], data, None, chart, report_summary

def get_columns():
	return [
		{
			"fieldname": "site_name",
			"label": _("Site Name"),
			"fieldtype": "Link",
			"options": "Catering Site",
			"width": 120
		},
		{
			"fieldname": "date",
			"label": _("Sale Date"),
			"fieldtype": "Date",
			"width": 120
		}
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype='Sales',
		fields=['site_name', 'date', 'net_price'],
		filters=conditions,
		order_by='site_name desc'
	)
	print ("data is", data)
	return data

def get_conditions(filters):
	conditions = {}
	for key,value in filters.items():
		if filters.get(key):
			conditions[key] = value

	return conditions

def get_chart_data(data):
	if not data:
		return None

	catering_site = dict()
	
	labels = []
	for d in data:
		if catering_site.get(str(d.get("date"))) is None:
			catering_site[str(d.get("date"))] = d.get("net_price")
			labels.append(str(d.get("date")))
		else :
			catering_site[str(d.get("date"))] += d.get("net_price")

	labels = sorted(labels)
	print(catering_site)
	datasets = []
	datasets.append({
		'name': 'Net Value',
		'values': [catering_site[label] for label in labels]
	})

	chart = {
		'data': {
			'labels': labels,
			'datasets': datasets
		},
		'type': 'line',
		'height': 300,
	}

	return chart
	
def get_report_summary(data, filters):
	if not data: return None

	daily_sales = 0
	date = str(filters.get("Date")) if (filters.get("Date") is not None) else datetime.now().strftime('%Y-%m-%d')
	print(date, filters)
	for entry in data:
		if str(entry.get("date")) == date:
			daily_sales += entry.get("net_price")
	
	return [
		{
			'value': daily_sales,
			'label': 'Daily Sales',
			'datatype': 'Currency',
			'currency': 'INR'
		}
	]
