from pydantic import BaseModel, field_validator


def shishkebab(s: str) -> str:
    return s.replace("_", "-")


class Foo(BaseModel, alias_generator=shishkebab):
    some_field: str

    @field_validator("some_field")
    @classmethod
    def _strip(cls, value: str) -> str:
        return value.strip()


class Bar(BaseModel, alias_generator=shishkebab):
    an_attr: str

    @property
    def a_property(self) -> str:
        return self.an_attr * 2
