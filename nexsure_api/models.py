from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Address:
    AddressType: str | None = None
    StreetAddress1: str | None = None
    StreetAddress2: str | None = None
    City: str | None = None
    State: str | None = None
    ZipCode: str | None = None
    Country: dict | None = None
    InternationalAddress: str | None = None


@dataclass
class PersonPhone:
    PhoneID: int | None = None
    PhoneNumber: str | None = None
    Extenstion: str | None = None
    Description: str | None = None
    IsPrimaryPhone: bool | None = None
    PersonPhoneID: int | None = None
    PhoneType: str | None = None


@dataclass
class Person:
    PersonID: int | None = None
    FirstName: str | None = None
    MiddleInitial: str | None = None
    LastName: str | None = None
    GoesBy: str | None = None
    Prefix: str | None = None
    Suffix: str | None = None
    Title: str | None = None
    IsEmployee: bool | None = None
    Phone: list[PersonPhone] = field(default_factory=list)
    DateOfBirth: str | None = None
    SSN: str | None = None
    MaritalStatus: str | None = None
    Sex: str | None = None
    DriversLicenseNo: str | None = None
    LicensedState: str | None = None
    LicensedDt: str | None = None
    Email: list[str] = field(default_factory=list)
    CreatedDt: str | None = None
    LastModifiedDt: str | None = None
    EnterpriseApplicationID: str | None = None
    ReplicationID: str | None = None


@dataclass
class Location:
    LocationID: int | None = None
    LocationTypeCode: str | None = None
    LocationName: str | None = None
    Address: list[Address] = field(default_factory=list)
    IsPrimaryLocation: bool | None = None
    IsBillingLocation: bool | None = None
    LastModifiedDt: str | None = None
    EnterpriseApplicationID: str | None = None
    ReplicationID: str | None = None


@dataclass
class ClientName:
    ClientNameID: int | None = None
    Name: str | None = None
    LegalEntityCd: str | None = None
    Status: str | None = None
    IsPrimaryName: bool | None = None
    IsDBAName: bool | None = None
    URL: str | None = None
    NoEmployees: int | None = None
    FEIN: str | None = None
    SSN: str | None = None
    GrossReceiptsBasis: str | None = None
    GrossReceipts: str | None = None
    ClientLongName: str | None = None
    Notes: str | None = None
    NatureOfBusiness: str | None = None
    YearStarted: str | None = None
    CreatedDt: str | None = None
    LastModifiedDt: str | None = None
    EnterpriseApplicationID: str | None = None
    ReplicationID: str | None = None


@dataclass
class Client:
    ClientID: int | None = None
    EnterpriseCode: str | None = None
    IsActive: bool | None = None
    ClientType: str | None = None
    ClientStage: str | None = None
    ClientSince: str | None = None
    CreatedDt: str | None = None
    LastModifiedDt: str | None = None
    LastModifiedBy: Person | None = None
    ClientNames: list[ClientName] = field(default_factory=list)
    Contacts: list[dict[str, Any]] = field(default_factory=list)
    Locations: list[Location] = field(default_factory=list)
    RelatedAccounts: list[dict[str, Any]] = field(default_factory=list)
    Assignments: list[dict[str, Any]] = field(default_factory=list)
    Classifieds: list[dict[str, Any]] = field(default_factory=list)
    Actions: list[dict[str, Any]] = field(default_factory=list)
    Policies: list[dict[str, Any]] = field(default_factory=list)
    EnterpriseApplicationID: str | None = None
    ReplicationID: str | None = None


@dataclass
class Premium:
    Estimated: str | None = None
    Annualized: str | None = None
    Billed: str | None = None


@dataclass
class Policy:
    PolicyID: int | None = None
    ClientID: int | None = None
    PolicyNumber: str | None = None
    EffDate: str | None = None
    ExpDate: str | None = None
    CovEffDate: str | None = None
    CovExpDate: str | None = None
    OriginationDate: str | None = None
    PolicyMode: str | None = None
    PolicyStage: str | None = None
    PolicyStatus: str | None = None
    PolicyType: str | None = None
    PolicyDescription: str | None = None
    IsNonRenewing: bool | None = None
    IsInHistory: bool | None = None
    HistoryNotes: str | None = None
    Premiums: Premium | None = None
    Assignments: list[dict[str, Any]] = field(default_factory=list)
    Actions: list[dict[str, Any]] = field(default_factory=list)
    Classifieds: list[dict[str, Any]] = field(default_factory=list)
    CreatedDt: str | None = None
    LastModifiedDt: str | None = None
    EnterpriseApplicationID: str | None = None
    ReplicationID: str | None = None


@dataclass
class AttachmentAssignmentType:
    AssignmentType: str | None = None
    AssignmentReplicationID: str | None = None
    AssignmentTypeID: int | None = None


@dataclass
class Attachment:
    AttachmentID: int | None = None
    AssignedTo: AttachmentAssignmentType | None = None
    AttachmentName: str | None = None
    AttachmentDesc: str | None = None
    FileName: str | None = None
    LastModifiedDt: str | None = None
    ActionID: int | None = None
    ReplicationID: str | None = None


@dataclass
class LookupDefinitionValueType:
    ItemID: int | None = None
    ItemCode: str | None = None
    ItemValue: str | None = None
    IsSystemType: bool | None = None
    CreatedDt: str | None = None
    LastModifiedDt: str | None = None


@dataclass
class LookupDefinitionType:
    TypeID: int | None = None
    TypeName: str | None = None
    TypeSize: int | None = None
    DataItem: list[LookupDefinitionValueType] = field(default_factory=list)
    CreatedDt: str | None = None
    LastModifiedDt: str | None = None


@dataclass
class LookupCategoryType:
    CategoryID: int | None = None
    CategoryName: str | None = None
    IsSystemType: bool | None = None
    Type: list[LookupDefinitionType] = field(default_factory=list)
    CreatedDt: str | None = None
