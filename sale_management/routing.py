import frappe

def get_home_page(user):
    print("user is", user)
    userdoc = frappe.get_doc(doctype ="User", filter={'email': user})
    print(userdoc.roles, "user doc")
    print("something")
    return "login"