from xml.etree.ElementTree import Element, parse

currencies = set[str]()

ISO_4217 = parse('./list-one.xml').getroot()
match ISO_4217:
	case Element(tag = 'ISO_4217'):
		for CcyTbl in ISO_4217:
			match CcyTbl:
				case Element(tag = 'CcyTbl'):
					for CcyNtry in CcyTbl:
						match CcyNtry:
							case Element(tag = 'CcyNtry'):
								ccys = list(CcyNtry.iter('Ccy'))
								if len(ccys) == 0:
									continue
								ccy, = ccys
								assert ccy.text
								currencies.add(ccy.text)
							case _:
								pass
				case _:
					pass
	case _:
		assert False

currencies = sorted(currencies)

for currency in currencies:
	assert '\'' not in currency

with open('src/mundane/_currencies.py', 'w') as out:
	out.write(f'''from typing import Literal

from ._currency import Currency

__all__ = [{', '.join(f'\'{currency}\'' for currency in currencies)}]
''')

	for currency in currencies:
		out.write(f'''

class {currency}(Currency):
	__slots__ = []

	@property
	def id(self) -> Literal['{currency}']:
		return '{currency}'
''')

with open('src/mundane/__init__.py', 'w') as out:
	out.write(f'''from ._currencies import *
from ._currency import Currency
from ._money import Money

__all__ = ['Money', 'Currency', {', '.join(f'\'{currency}\'' for currency in currencies)}]
''')
