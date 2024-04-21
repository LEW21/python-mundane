class Currency(type):

	@classmethod
	def __prepare__(cls, name: str, bases: tuple[type, ...], /, **kwds: object):
		namespace = super().__prepare__(name, bases, **kwds)
		namespace['__slots__'] = ()
		return namespace
