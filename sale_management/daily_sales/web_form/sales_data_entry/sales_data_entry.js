frappe.ready(function() {
	frappe.web_form.on('price', (field,value) => {
		if(frappe.web_form.get_value('quantity')!=0) {
			frappe.web_form.set_value('net_price', frappe.web_form.get_value('quantity') * frappe.web_form.get_value('price'));
		}
	});
	
	frappe.web_form.on('quantity', (field,value) => {
		if(frappe.web_form.get_value('price')!=0) {
			frappe.web_form.set_value('net_price', frappe.web_form.get_value('quantity') * frappe.web_form.get_value('price'));
		}
	});

	frappe.web_form.on('site_name', (field,value) => {
		frappe.call({
			method: 'sale_management.daily_sales.doctype.sales.sales.getSiteItems',
			args: {
				site_name: value
			},
			freeze: true,
			freeze_message: __('Loading Data... Please Wait'),
			callback: (r) => {
				console.log(r.message.map((a) => (a.name1)));
				frappe.web_form.set_df_property('dummy_items', 'options', r.message.map((a) => (a.name1)));
			}
		})
	});

	frappe.web_form.on('dummy_items', (field, value) => {
		frappe.web_form.set_df_property('items', 'hidden', false);
		frappe.web_form.set_value('items', value);
		frappe.web_form.set_df_property('items', 'hidden', true);
	});

	frappe.call({
		method: 'sale_management.daily_sales.doctype.sales.sales.getUserCateringSite',
		freeze: true,
		freeze_message: __('Loading Your Catering Site... Please Wait'),
		callback: (r) => {
			if(r.message){
				frappe.web_form.set_value('site_name', r.message);
			frappe.web_form.set_df_property('site_name', 'read_only', true);
			}
		}
	})
	
})