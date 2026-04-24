from dataclasses import dataclass, field

from nexsure_api.types import AddressType


@dataclass
class AddressInput:
    street: str
    city: str
    state: str
    zip_code: str
    address_type: AddressType = AddressType.Physical


@dataclass
class ContactInput:
    first_name: str
    last_name: str
    is_primary: bool = True


@dataclass
class AssignmentInput:
    branch_id: str
    department_id: str
    is_primary: bool = True
