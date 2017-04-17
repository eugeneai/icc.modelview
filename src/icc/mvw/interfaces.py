from zope.interface import Interface, Attribute

class IModel(Interface):
    """Just marker interface, to mark models in
    various MV* patterns: MVC, MVP, MVMC, etc.
    """


class IView(Interface):
    """Interface representing view in MVC, MVP, etc.
    """
    model = Attribute("Project under exploration. The MVC Model.")
    ui = Attribute("User interface component holder.")


class IController(Interface):
    """Interface representing Controller in MVC
    """


class IPresenter(IController):
    """Interface representing Presenter in MVP
    """

class IViewRegistry(Interface):
    """
    Registers views under names
    """

    def register(view, name):
        """
        Register a view under the name.
        """

    def unregister(name):
        """
        Unregister view under the name.
        """

    def get(name, default):
        """
        Return the view registered under the name.
        """
