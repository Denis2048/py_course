"""Программа для импорта, экспорта и поиска контактов по фразе"""

from lab_phonebook import Phone


phone = Phone()
phone.import_contacts_from_csv("contacts.csv")
phone.show()
phone.search_contacts()
phone.export_contacts_to_csv("exported_contacts.csv")
