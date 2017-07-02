from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.lims.interfaces import ISample
from bika.lims.fields import ExtStringField
from Products.Archetypes.public import *
from bika.lims import bikaMessageFactory as _
from zope.component import adapts
from zope.interface import implements

SampleConditionText =  ExtStringField(
        'SampleConditionText',
        widget=StringWidget(
            label=_("Sample Condition"),
            description= "",
            visible={'view': 'visible',
                     'edit': 'visible',
                     'add': 'edit'},
            render_own_label=True,
            size=20
        )
    )

class SampleSchemaExtender(object):
    adapts(ISample)
    implements(IOrderableSchemaExtender)

    fields = [
        SampleConditionText,
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        index = schematas["default"].index("SamplePoint") + 1
        schematas["default"].insert(index, "SampleConditionText")
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
            schema['SamplingDate'].widget.visible = False
            schema['SamplingDate'].required = False

        schema.moveField("SampleConditionText", after="SamplePoint")

        return schema
