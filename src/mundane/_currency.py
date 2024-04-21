from decimal import Decimal as decimal
from typing import Any

from ._money import Money


class Currency(type):

	def __instancecheck__(self, instance: object) -> bool:
		return isinstance(instance, Money) and instance.currency == self.__name__

	def __call__(self, value: decimal | str | int) -> Any:  # type: ignore
		return Money(self.__name__, value)
