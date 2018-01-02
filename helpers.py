def filter_contacts(contact_list):
    return list(map(filter_contact, contact_list))

def filter_contact(contact):
    contact_fields = {'firstname', 'lastname', 'dob', 'address', 'phone', 'email', 'id'}
    if('_id' in contact):
        contact["id"] = str(contact['_id'])
    return {k: v for k, v in contact.items() if k in contact_fields}
