// Copyright (c) 2023, metamenu and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Site Manager Report"] = {
	"filters": [
		{
			fieldname: "site_name",
			label: __("Site Name"),
			fieldtype: "Link",
			options: "Catering Site",
		},
		{
			fieldname: "Date",
			label: __("Sale Date"),
			fieldtype: "Date",
		}
	]
};
