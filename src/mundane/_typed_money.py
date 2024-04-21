from ._any_money import AnyMoney
from ._currency import Currency


class TypedMoney(AnyMoney, metaclass = Currency):
	pass
