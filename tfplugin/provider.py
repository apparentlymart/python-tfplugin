

class Provider(object):
    """
    Entry-point type for implementing provider plugins. Instantiate this type
    and then decorate various resource type and data source block type classes
    using its ``resource_type`` and ``data_source`` decorators before eventually
    calling method ``serve`` to start up the plugin "server".
    """

    def __init__(self, config_block_type=None):
        pass

    def resource_type(self, name, schema_version=0):
        """
        Decorator for registering a particular block type as a resource type.

        A block type registered in this way must have methods ``read``, ``create``,
        ``delete`` and optionally ``update``, amongst others, that implement
        the behavior of the resource type.
        """
        def resource_type_register(cls):
            # cls should always be a Block subclass
            pass

    def data_source(self, name):
        """
        Decorator for registering a particular block type as a data source.

        A block type registered in this way must have method ``read`` that
        implements the behavior of the resource type.
        """
        def data_source_register(cls):
            # cls should always be a Block subclass
            pass

    def serve(self):
        """
        Start up the plugin "server" and serve requests until instructed by
        the host Terraform process to exit.
        """
        pass


__all__ = [
    'Provider'
]
