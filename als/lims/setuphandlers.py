from Products.CMFPlone.interfaces import INonInstallable
from zope.component.hooks import getSite
from zope.interface import implementer

from als.lims.permissions import setup_default_permissions


def setupVarious(context):
    if context.readDataFile('alslims_default.txt') is None:
        return

    portal = getSite()
    setup_default_permissions(portal)


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('alslims_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
    pass
