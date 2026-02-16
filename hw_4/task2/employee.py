from __future__ import annotations

class Employee:

    def __init__(self):
        pass


    def __str__(self):
        pass


    def get_position(self) -> str:
        pass


    def get_id(self) -> int:
        pass


    def get_contacts(self) -> list[ContactInfo]:
        pass


    def set_position(self, new_position: str) -> None:
        pass


    def add_contact(self, contact: ContactInfo) -> None:
        pass


    def remove_contact(self, contact: ContactInfo) -> None:
        pass


class ContactInfo:

    def __init__(self):
        pass


    def __str__(self):
        pass


    def get_type(self) -> str:
        pass


    def get_value(self) -> str:
        pass


    def set_type(self) -> None:
        pass


    def set_value(self) -> None:
        pass