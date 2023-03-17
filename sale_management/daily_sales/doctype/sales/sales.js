// Copyright (c) 2023, metamenu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Sales", {
	refresh(frm) {
        frm.set_df_property('items', 'hidden', true);
        frappe.call({
            method: 'sale_management.daily_sales.doctype.sales.sales.getUserCateringSite',
            freeze: true,
            freeze_message: __('Loading Your Catering Site... Please Wait'),
            callback: (r) => {
                if(r.message){
                    frm.set_value('site_name', r.message);
                frm.set_df_property('site_name', 'read_only', true);
                frappe.call({
                    method: 'sale_management.daily_sales.doctype.sales.sales.getSiteItems',
                    args: {
                        site_name: r.message
                    },
                    freeze: true,
                    freeze_message: __('Loading Items... Please Wait'),
                    callback: (r) => {
                        console.log(r.message.map((a) => (a.name)));
                        frm.set_df_property('dummy_items', 'options', r.message.map((a) => (a.name)));
                    }
                })
                }
            }
        });
        
	},

    dummy_items(frm) {
        console.log("enter", frm.doc.dummy_items);
        frm.set_df_property('items', 'hidden', false);
        frm.set_value('items', frm.doc.dummy_items);
        frm.set_df_property('items', 'hidden', true);
    },

    quantity(frm){
        if(frm.doc.price){
            frm.set_value('net_price', frm.doc.price * frm.doc.quantity);
        }
    },

    price(frm){
        if(frm.doc.quantity){
            frm.set_value('net_price', frm.doc.quantity * frm.doc.price);
        }
    }

});
