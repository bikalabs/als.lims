from bika.lims.interfaces import IATWidgetVisibility
from zope.interface import implements


class HideSamplingDate(object):
    """Hide sampling date if SWE is enabled.
    """
    implements(IATWidgetVisibility)

    def __init__(self, context):
        self.context = context
        self.sort = 100

    def __call__(self, context, mode, field, default):
        swe = context.bika_setup.getSamplingWorkflowEnabled()
        state = default if default else 'invisible'
        fieldname = field.getName()
        if fieldname == 'SamplingDate' and swe:
            state = 'invisible'
        return state
