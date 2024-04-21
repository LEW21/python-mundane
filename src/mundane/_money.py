import math
import sys
from decimal import Decimal as decimal
from typing import TYPE_CHECKING, Generic, Self, TypeVar, overload

from ._currency import Currency

if sys.version_info >= (3, 13) or TYPE_CHECKING:
	C = TypeVar('C', bound = Currency, default = Currency, covariant = True)
else:
	C = TypeVar('C', bound = Currency, covariant = True)


class Money(Generic[C]):
	__slots__ = ['currency', 'value']
	currency: C
	value: decimal

	def __init__(self, currency: C, value: decimal | str | int):
		self.currency = currency
		self.value = decimal(value)

	def __str__(self):
		return f"{self.currency} {self.value:f}"

	def __repr__(self):
		return f"{self.currency}('{self.value:f}')"

	def __hash__(self):
		return hash((self.currency, self.value))

	def __eq__(self, other: object) -> bool:
		if isinstance(other, Money):
			return (self.currency, self.value) == (other.currency, other.value)
		return NotImplemented

	def __lt__(self, other: Self) -> bool:
		if not isinstance(other, Money):
			return NotImplemented
		if self.currency != other.currency:
			raise TypeError(f"'<' not supported between money in '{self.currency}' and '{other.currency}'")
		return self.value < other.value

	def __le__(self, other: Self) -> bool:
		if not isinstance(other, Money):
			return NotImplemented
		if self.currency != other.currency:
			raise TypeError(f"'<=' not supported between money in '{self.currency}' and '{other.currency}'")
		return self.value <= other.value

	def __gt__(self, other: Self) -> bool:
		if not isinstance(other, Money):
			return NotImplemented
		if self.currency != other.currency:
			raise TypeError(f"'>' not supported between money in '{self.currency}' and '{other.currency}'")
		return self.value > other.value

	def __ge__(self, other: Self) -> bool:
		if not isinstance(other, Money):
			return NotImplemented
		if self.currency != other.currency:
			raise TypeError(f"'>=' not supported between money in '{self.currency}' and '{other.currency}'")
		return self.value >= other.value

	def __pos__(self) -> Self:
		return type(self)(self.currency, +self.value)

	def __neg__(self) -> Self:
		return type(self)(self.currency, -self.value)

	def __abs__(self) -> Self:
		return type(self)(self.currency, abs(self.value))

	def __add__(self, other: Self) -> Self:
		if not isinstance(other, Money):
			return NotImplemented
		if self.currency != other.currency:
			raise TypeError(f"'+' not supported between money in '{self.currency}' and '{other.currency}'")
		return type(self)(self.currency, self.value + other.value)

	def __sub__(self, other: Self) -> Self:
		if not isinstance(other, Money):
			return NotImplemented
		if self.currency != other.currency:
			raise TypeError(f"'-' not supported between money in '{self.currency}' and '{other.currency}'")
		return type(self)(self.currency, self.value - other.value)

	def __mul__(self, other: int | decimal) -> Self:
		if isinstance(other, int) or isinstance(other, decimal):  # type: ignore
			return type(self)(self.currency, self.value * other)
		return NotImplemented

	def __rmul__(self, other: int | decimal) -> Self:
		if isinstance(other, int) or isinstance(other, decimal):  # type: ignore
			return type(self)(self.currency, self.value * other)
		return NotImplemented

	@overload
	def __truediv__(self, other: Self) -> decimal:
		...

	@overload
	def __truediv__(self, other: int | decimal) -> Self:
		...

	def __truediv__(self, other: Self | int | decimal) -> decimal | Self:
		if isinstance(other, int) or isinstance(other, decimal):
			return type(self)(self.currency, self.value / other)
		if not isinstance(other, Money):  # type: ignore
			return NotImplemented
		if self.currency != other.currency:
			raise TypeError(f"'/' not supported between money in '{self.currency}' and '{other.currency}'")
		return self.value / other.value

	def __round__(self, ndigits: int | None = None) -> Self:
		return type(self)(self.currency, round(self.value, ndigits))

	def __trunc__(self) -> Self:
		return type(self)(self.currency, math.trunc(self.value))

	def __floor__(self) -> Self:
		return type(self)(self.currency, math.floor(self.value))

	def __ceil__(self) -> Self:
		return type(self)(self.currency, math.ceil(self.value))
