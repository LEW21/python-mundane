from decimal import Decimal as decimal
from types import NotImplementedType
from typing import Self, overload

from ._money import OverloadPaddingType1, OverloadPaddingType2


class TypedMoneyMixin:
	__slots__ = ()

	def __init__(self, value: decimal | str | int):
		...

	@overload
	def __lt__(self, other: OverloadPaddingType1) -> NotImplementedType:
		...

	@overload
	def __lt__(self, other: OverloadPaddingType2) -> NotImplementedType:
		...

	@overload
	def __lt__(self, other: Self) -> bool:
		...

	def __lt__(self, other: object) -> bool | NotImplementedType:
		...

	@overload
	def __le__(self, other: OverloadPaddingType1) -> NotImplementedType:
		...

	@overload
	def __le__(self, other: OverloadPaddingType2) -> NotImplementedType:
		...

	@overload
	def __le__(self, other: Self) -> bool:
		...

	def __le__(self, other: object) -> bool | NotImplementedType:
		...

	@overload
	def __gt__(self, other: OverloadPaddingType1) -> NotImplementedType:
		...

	@overload
	def __gt__(self, other: OverloadPaddingType2) -> NotImplementedType:
		...

	@overload
	def __gt__(self, other: Self) -> bool:
		...

	def __gt__(self, other: object) -> bool | NotImplementedType:
		...

	@overload
	def __ge__(self, other: OverloadPaddingType1) -> NotImplementedType:
		...

	@overload
	def __ge__(self, other: OverloadPaddingType2) -> NotImplementedType:
		...

	@overload
	def __ge__(self, other: Self) -> bool:
		...

	def __ge__(self, other: object) -> bool | NotImplementedType:
		...

	@overload
	def __add__(self, other: OverloadPaddingType1) -> NotImplementedType:
		...

	@overload
	def __add__(self, other: OverloadPaddingType2) -> NotImplementedType:
		...

	@overload
	def __add__(self, other: Self) -> Self:
		...

	def __add__(self, other: object) -> Self | NotImplementedType:
		...

	@overload
	def __sub__(self, other: OverloadPaddingType1) -> NotImplementedType:
		...

	@overload
	def __sub__(self, other: OverloadPaddingType2) -> NotImplementedType:
		...

	@overload
	def __sub__(self, other: Self) -> Self:
		...

	def __sub__(self, other: object) -> Self | NotImplementedType:
		...

	@overload
	def __truediv__(self, other: OverloadPaddingType1) -> NotImplementedType:
		...

	@overload
	def __truediv__(self, other: int | decimal) -> Self:
		...

	@overload
	def __truediv__(self, other: Self) -> decimal:
		...

	def __truediv__(self, other: object) -> decimal | Self | NotImplementedType:
		...
