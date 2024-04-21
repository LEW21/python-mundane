from decimal import Decimal as decimal
from typing import Any

from ._money import Money


class Currency(type):

	@classmethod
	def __prepare__(cls, name: str, bases: tuple[type, ...], /, **kwds: object):
		namespace = super().__prepare__(name, bases, **kwds)
		namespace['__slots__'] = ()
		return namespace

	def __instancecheck__(self, instance: object) -> bool:
		return isinstance(instance, Money) and instance.currency == self.__name__

	def __call__(self, value: decimal | str | int) -> Any:  # type: ignore
		return Money(self.__name__, value)
