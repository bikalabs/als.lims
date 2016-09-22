from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.lims.interfaces import ISample
from zope.component import adapts
from zope.interface import implements


class SampleSchemaExtender(object):
    adapts(ISample)
    implements(IOrderableSchemaExtender)

    fields = [
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields


class SampleSchemaModifier(object):
    adapts(ISample)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        """
        """

        # SamplingDate is not a required field, if SWE is enabled
        swe = self.context.bika_setup.getSamplingWorkflowEnabled()
        if swe:
            schema['SamplingDate'].required = False

        return schema
