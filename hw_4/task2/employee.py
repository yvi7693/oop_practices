from __future__ import annotations

class Employee:

    __name: str
    __position: str
    __id: int
    __contacts: list[ContactInfo]

    def __init__(self, name: str, position: str, id: int, contacts: list[ContactInfo]):
        self.__name = name
        self.__position = position
        self.__id = id
        self.__contacts = contacts


    def __str__(self):
        return (f"name: {self.__name}"
                f"position: {self.__position}"
                f"id: {self.__id}"
                f"contacts: {self.__contacts}")


    def get_position(self) -> str:
        return self.__name


    def get_id(self) -> int:
        return self.__id


    def get_contacts(self) -> list[ContactInfo]:
        return self.__contacts


    def set_position(self, new_position: str) -> None:
        self.__position = new_position


    def add_contact(self, contact: ContactInfo) -> None:
        is_may = True

        for contact in self.__contacts:
            if contact.type == contact.type:
                is_may = False

        if is_may:
            self.__contacts.append(contact)


    def remove_contact(self, contact_delete: ContactInfo) -> None:
        contacts = self.__contacts
        delete_index = None

        for i in range(len(contacts)):
            if contacts[i] == contact_delete:
                delete_index = i

        if not delete_index is None:
            contacts.pop(delete_index)



class ContactInfo:

    __type: str
    __value: str

    def __init__(self, type: str, value: str):
        self.__type = type
        self.__value = value


    def __str__(self):
        return (f"type: {self.__type}"
                f"value: {self.__value}")


    def __get_type(self) -> str:
        return self.__type


    def get_value(self) -> str:
        return self.__value

    type = property(get_type)