// Copyright (c) 2023, metamenu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Sales", {
	refresh(frm) {
        frappe.call({
            method: 'sale_management.daily_sales.doctype.sales.sales.getUserCateringSite',
            freeze: true,
            freeze_message: __('Loading Your Catering Site... Please Wait'),
            callback: (r) => {
                if(r.message){
                    frm.set_value('site_name', r.message);
                frm.set_df_property('site_name', 'read_only', true);
                }
            }
        })
	},
});
