import math
import random
import unittest
from decimal import Decimal as decimal
from typing import assert_type

from mundane import *


class TestMoney(unittest.TestCase):

	def test_basic(self):
		assert isinstance(PLN(50), Money)
		assert isinstance(PLN(50).currency, PLN)

	def test_str(self):
		assert str(PLN(50).currency) == 'PLN'
		assert repr(PLN(50).currency) == 'PLN()'
		assert str(PLN(50)) == 'PLN 50'
		assert repr(PLN(50)) == 'PLN(\'50\')'
		assert hash(PLN(50))
		assert str(EUR('0.0000000000000000000001')) == 'EUR 0.0000000000000000000001'
		assert repr(EUR('0.0000000000000000000001')) == 'EUR(\'0.0000000000000000000001\')'

	def test_eq(self):
		assert_type(PLN(50) == PLN(100), bool)
		assert PLN(50) == PLN('50') == PLN(decimal('50'))
		assert PLN(50) == Money(PLN(), 50)
		assert PLN(50) != PLN(100)
		assert PLN(50) != EUR(50)

		assert PLN(50).currency == 'PLN'

	def test_order(self):
		assert_type(PLN(50) < PLN(100), bool)
		assert PLN(50) < PLN(100)
		assert not PLN(50) < PLN(50)
		assert not PLN(50) < PLN(20)
		assert PLN(50) > PLN(20)
		assert not PLN(50) > PLN(50)
		assert not PLN(50) > PLN(100)
		assert PLN(50) <= PLN(50)
		assert PLN(50) <= PLN(100)
		assert not PLN(50) <= PLN(20)
		assert PLN(50) >= PLN(50)
		assert PLN(50) >= PLN(20)
		assert not PLN(50) >= PLN(100)
		try:
			assert PLN(50) < EUR(50)  # type: ignore
		except TypeError:
			pass
		else:
			assert False

	def test_math(self):
		assert_type(+PLN(50), Money[PLN])
		assert +PLN(50) == PLN(50)
		assert +PLN(-50) == PLN(-50)

		assert_type(-PLN(50), Money[PLN])
		assert -PLN(50) == PLN(-50)
		assert -PLN(-50) == PLN(50)

		assert_type(abs(PLN(50)), Money[PLN])
		assert abs(PLN(50)) == PLN(50)
		assert abs(PLN(-50)) == PLN(50)

		assert_type(PLN(50) + PLN(100), Money[PLN])
		assert PLN(50) + PLN(100) == PLN(150)

		try:
			PLN(50) + EUR(100)  # type: ignore
		except TypeError:
			pass
		else:
			assert False

		try:
			PLN(50) + 100  # type: ignore
		except TypeError:
			pass
		else:
			assert False

		assert_type(PLN(50) - PLN(100), Money[PLN])
		assert PLN(50) - PLN(100) == PLN(-50)

		try:
			PLN(50) - 100  # type: ignore
		except TypeError:
			pass
		else:
			assert False

		assert_type(PLN(50) * 2, Money[PLN])
		assert PLN(50) * 2 == PLN(100)

		assert_type(2 * PLN(50), Money[PLN])
		assert 2 * PLN(50) == PLN(100)

		try:
			PLN(2) * PLN(50)  # type: ignore
		except TypeError:
			pass
		else:
			assert False

		try:
			EUR(2) * PLN(50)  # type: ignore
		except TypeError:
			pass
		else:
			assert False

		assert_type(PLN(50) / 2, Money[PLN])
		assert PLN(50) / 2 == PLN(25)

		assert_type(PLN(50) / PLN(2), decimal)
		assert PLN(50) / PLN(2) == decimal(25)

		try:
			PLN(50) / EUR(2)  # type: ignore
		except TypeError:
			pass
		else:
			assert False

		assert_type(round(PLN('50.123')), Money[PLN])
		assert round(PLN('50.123')) == PLN(50)

		assert_type(round(PLN('50.5')), Money[PLN])
		assert round(PLN('50.5')) == PLN(50)

		assert_type(round(PLN('-50.5')), Money[PLN])
		assert round(PLN('-50.5')) == PLN(-50)

		assert_type(round(PLN('50.123'), 2), Money[PLN])
		assert round(PLN('50.123'), 2) == PLN('50.12')

		assert_type(math.trunc(PLN('50.123')), Money[PLN])
		assert math.trunc(PLN('50.123')) == PLN(50)

		assert_type(math.trunc(PLN('-50.123')), Money[PLN])
		assert math.trunc(PLN('-50.123')) == PLN(-50)

		assert_type(math.floor(PLN('50.123')), Money[PLN])
		assert math.floor(PLN('50.123')) == PLN(50)

		assert_type(math.floor(PLN('-50.123')), Money[PLN])
		assert math.floor(PLN('-50.123')) == PLN(-51)

		assert_type(math.ceil(PLN('50.123')), Money[PLN])
		assert math.ceil(PLN('50.123')) == PLN(51)

		assert_type(math.ceil(PLN('50.123')), Money[PLN])
		assert math.ceil(PLN('-50.123')) == PLN(-50)

	def test_generic_type(self):
		val = PLN(50) if random.randrange(0, 2) else EUR(100)
		assert_type(val, Money[PLN] | Money[EUR])

		def take_money(money: Money):
			assert_type(money.currency, Currency)
			assert money.currency in {'PLN', 'EUR'}

		take_money(val)
