from zope.interface import Interface, Attribute
class IModel(Interface):
    """Just marker interface, to mark models
    """

class IModuleModel(IModel):
    """Module model """
