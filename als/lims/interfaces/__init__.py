from zope.interface import Interface


class IALSLIMS(Interface):

    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "als.lims" product, this interface must be its layer
    """
