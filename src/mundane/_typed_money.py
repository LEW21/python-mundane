from decimal import Decimal as decimal

from ._money import Money
from ._currency import Currency
from ._typed_money_mixin import TypedMoneyMixin


class TypedMoney(TypedMoneyMixin, Money, metaclass = Currency):

	def __init__(self, value: decimal | str | int):
		...
