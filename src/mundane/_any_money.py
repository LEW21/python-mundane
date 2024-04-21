from decimal import Decimal as decimal
from types import NotImplementedType
from typing import Self, overload

from ._money import Money, OverloadPaddingType1, OverloadPaddingType2


class AnyMoney(Money):
	__slots__ = ()

	def __init__(self, value: decimal | str | int):
		raise TypeError("AnyMoney cannot be instantiated")

	@overload
	def __lt__(self, other: OverloadPaddingType1) -> NotImplementedType:
		pass

	@overload
	def __lt__(self, other: OverloadPaddingType2) -> NotImplementedType:
		pass

	@overload
	def __lt__(self, other: Self) -> bool:
		...

	def __lt__(self, other: object) -> bool | NotImplementedType:
		return super().__lt__(other)  # type: ignore

	@overload
	def __le__(self, other: OverloadPaddingType1) -> NotImplementedType:
		pass

	@overload
	def __le__(self, other: OverloadPaddingType2) -> NotImplementedType:
		pass

	@overload
	def __le__(self, other: Self) -> bool:
		...

	def __le__(self, other: object) -> bool | NotImplementedType:
		return super().__le__(other)  # type: ignore

	@overload
	def __gt__(self, other: OverloadPaddingType1) -> NotImplementedType:
		pass

	@overload
	def __gt__(self, other: OverloadPaddingType2) -> NotImplementedType:
		pass

	@overload
	def __gt__(self, other: Self) -> bool:
		...

	def __gt__(self, other: object) -> bool | NotImplementedType:
		return super().__gt__(other)  # type: ignore

	@overload
	def __ge__(self, other: OverloadPaddingType1) -> NotImplementedType:
		pass

	@overload
	def __ge__(self, other: OverloadPaddingType2) -> NotImplementedType:
		pass

	@overload
	def __ge__(self, other: Self) -> bool:
		...

	def __ge__(self, other: object) -> bool | NotImplementedType:
		return super().__ge__(other)  # type: ignore

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
		return super().__add__(other)  # type: ignore

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
		return super().__sub__(other)  # type: ignore

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
		return super().__truediv__(other)  # type: ignore
