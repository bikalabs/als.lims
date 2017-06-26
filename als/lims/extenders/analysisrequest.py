from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.lims.interfaces import IAnalysisRequest
from bika.lims.fields import ExtStringField
from Products.Archetypes.public import *
from bika.lims import bikaMessageFactory as _
from zope.component import adapts
from zope.interface import implements





class SampleConditionTextField(ExtStringField):
    """A computed field which sets and gets a value from Sample
    """

    def get(self, instance):
        sample = instance.getSample()
        value = False
        if sample:
            value = sample.Schema()['SampleConditionText'].get(sample)
        if not value:
            value = self.getDefault(instance)
        return value

    def set(self, instance, value):
        sample = instance.getSample()
        if sample and value:
            return sample.Schema()['SampleConditionText'].set(sample, value)

SampleConditionText =  SampleConditionTextField(
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

class AnalysisRequestSchemaExtender(object):
    adapts(IAnalysisRequest)
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


class AnalysisRequestSchemaModifier(object):
    adapts(IAnalysisRequest)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    def hide_fields(self, schema, fieldnames):
        """Hide fields ALS doesn't care to see
        """

    def fiddle(self, schema):
        """
        """
        # hide field from view and edit views
        hidefromviewedit = [
            'SubGroup',
            'StorageLocation',
            'ClientReference',
            'ReportDryMatter',
            'Composite',
            'SamplingDate',
            'DefaultContainerType',
            # ALS uses only DateSampled and Sampler fields
            # SamplingDate is just confusing them and us.
            'SamplingDate',
        ]

        for fn in hidefromviewedit:
            if fn in schema:
                schema[fn].widget.visible = {
                    'view': 'invisible',
                    'edit': 'invisible'}

        # hide field from AR add
        hidefromadd = [
            'Sample',
            'SamplingRound',
            'SamplingDeviation',
            'EnvironmentalConditions',
            'AdHoc',
            'InvoiceExclude',
            'PreparationWorkflow',
            'SampleCondition'
        ]

        for fn in hidefromadd:
            if fn in schema:
                schema[fn].widget.visible = {
                'add': 'invisible',
                'edit': 'invisible',
                'view': 'invisible'}
                schema[fn].required = False
        # hide field from AR add
        hidefromadd = [
            'Sample',
            'SamplingRound',
            'SamplingDeviation',
            'EnvironmentalConditions',
            'AdHoc',
            'InvoiceExclude',
            'PreparationWorkflow',
            'SampleCondition'
        ]

        for fn in hidefromadd:
            if fn in schema:
                schema[fn].widget.visible = {
                'add': 'invisible',
                'edit': 'invisible',
                'view': 'invisible'}


        # Sampler and DateSampled are now visible on AR Add.
        schema['Sampler'].widget.visible['add'] = 'edit'
        schema['DateSampled'].widget.visible['add'] = 'edit'

        schema.moveField("SampleConditionText", after="SamplePoint")

        return schema
