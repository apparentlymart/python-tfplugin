# tfplugin.schema exports only symbols that might be used when defining a
# schema, so that callers can optionally import * from it. However, these
# symbols are also available directly under tfplugin for those who would
# rather not pollute their namespace directly.


class StringType(object):
    pass


class NumberType(object):
    pass


class BoolType(object):
    pass


class ListType(object):
    def __init__(self, of):
        self.of = of


class SetType(object):
    def __init__(self, of):
        self.of = of


class MapType(object):
    def __init__(self, of):
        self.of = of


String = StringType()
Number = NumberType()
Bool = BoolType()


class ObjectTypeMeta(type):
    def __new__(cls, name, bases, attrs):
        pass


class Object(object):
    """
    Parent class of all classes that represent Terraform object types.

    Object subclasses should be declared with their attributes defined as fields
    whose values are values returned by tfplugin.Attribute.

    >>> import tfplugin
    >>> class Instance(tfplugin.Object):
    ...     type_ = tfplugin.Attribute("type", tfplugin.String)
    ...     image_ = tfplugin.Attribute("image", tfplugin.String)
    ...

    NestedBlockType fields are not permitted in an Object subclass and will
    generate an error at declaration time if present.
    """
    __metaclass__ = ObjectTypeMeta

    def __new__(cls, atys):
        # Note that this isn't actually inherited by subclasses because our
        # metaclass hides it. This is here only to allow callers to use
        # Object(atys) as a convenient way to construct an anonymous object
        # type.
        pass


def Tuple(etys):
    """
    Generates an anonymous tuple type.
    """
    pass


class BlockTypeMeta(type):
    def __new__(cls, name, bases, attrs):
        pass


class Block(object):
    """
    Parent class of all classes that represent Terraform configuration block schemas.

    Block subclasses should be declared with their attributes and nested
    block types defined as fields whose values are returned either by
    Attribute or NestedBlockType.

    >>> import tfplugin
    >>> class Instance(tfplugin.Block):
    ...     type_ = tfplugin.Attribute("type", tfplugin.String)
    ...     image = tfplugin.Attribute("image", tfplugin.String)
    ...     block_device = tfplugin.NestedBlockType("block_device", tfplugin.Map(BlockDevice))
    ...

    The fields then provide the mapping between live instances and the wire
    representation of each type.
    """
    __metaclass__ = BlockTypeMeta


__all__ = [
    'Block',
    'String',
]
