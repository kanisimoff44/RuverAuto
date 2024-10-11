from pydantic import BaseModel, ConfigDict


class STextPages(BaseModel):
    our_contacts: str | None
    delivery_and_payment: str | None
    privacy_policy: str | None
    user_agreement: str | None

    model_config = ConfigDict(from_attributes=True)
