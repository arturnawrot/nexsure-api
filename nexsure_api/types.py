from enum import IntEnum, StrEnum


class SearchType(IntEnum):
    ExactMatch = 0
    Contains = 1
    StartsWith = 2


class AddressType(StrEnum):
    Physical = "Physical"
    Mailing = "Mailing"


class ClientType(StrEnum):
    Personal = "Personal"
    Commercial = "Commercial"


class ClientStage(StrEnum):
    Prospect = "Prospect"
    Client = "Client"
    Suspect = "Suspect"


class LegalEntity(StrEnum):
    Individual = "Individual"
    Partnership = "Partnership"
    Corporation = "Corporation"
    JointVenture = "JointVenture"
    LLC = "LLC"
    NPCorp = "NPCorp"
    Other = "Other"


class PolicyMode(StrEnum):
    New = "New"
    Renew = "Renew"
    RenewCo = "RenewCo"
    NewOnExisting = "NewOnExisting"


class PolicyStage(StrEnum):
    Marketing = "Marketing"
    Policy = "Policy"
    Endorsement = "Endorsement"
    Cancellation = "Cancellation"
    Audit = "Audit"
    Edit = "Edit"
    Claim = "Claim"
    Opportunity = "Opportunity"


class PolicyType(StrEnum):
    Package = "Package"
    Monoline = "Monoline"


class LOBType(StrEnum):
    Personal = "Personal"
    Commercial = "Commercial"
    Benefits = "Benefits"
    Bond = "Bond"
    FinancialServices = "FinancialServices"


class AttachmentAssignmentType(StrEnum):
    Client = "Client"
    Policy = "Policy"
    RetailAgent = "RetailAgent"


class LookupCategory(StrEnum):
    AdditionalInterest = "Additional Interest"
    Carrier = "Carrier"
    Client = "Client"
    DocumentIntegration = "Document Integration"
    FinancialEntity = "Financial Entity"
    Miscellaneous = "Miscellaneous"
    Organization = "Organization"
    People = "People"
    Policy = "Policy"
    PremiumFinanceCompany = "Premium Finance Company"
    RetailAgent = "Retail Agent"
    TaxAuthority = "Tax Authority"
    Vendor = "Vendor"
