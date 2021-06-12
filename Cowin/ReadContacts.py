from string import Template

# Function to read the contacts from a given contact file and return a
# list of names and email addresses

def get_contacts(contactList):
    names = []
    emails = []
    with open(contactList, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails



def read_template(template):
    with open(template, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)    