from decimal import Decimal as decimal
from typing import Self, overload


class Currency:
	__slots__ = []

	@property
	def id(self) -> str:
		raise NotImplementedError()

	@overload
	def __new__(cls) -> Self:
		...

	@overload
	def __new__(cls, value: decimal | str | int) -> '_money.Money[Self]':
		...

	def __new__(cls, value: decimal | str | int | None = None):
		if value is None:
			return object.__new__(cls)
		return _money.Money[cls](cls(), value)

	def __str__(self):
		return f"{self.id}"

	def __repr__(self):
		return f"{self.id}()"

	def __hash__(self):
		return hash(self.id)

	def __eq__(self, other: object):
		return self.id == other.id if isinstance(other, Currency) else self.id == other if isinstance(other, str) else NotImplemented


from . import _money  # type: ignore
