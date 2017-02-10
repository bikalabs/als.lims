from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.lims.interfaces import IAnalysisRequest
from zope.component import adapts
from zope.interface import implements


class AnalysisRequestSchemaExtender(object):
    adapts(IAnalysisRequest)
    implements(IOrderableSchemaExtender)

    fields = [
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
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
        for fn in fieldnames:
            if fn in schema:
                schema[fn].widget.visible = {'view': 'invisible',
                                             'edit': 'invisible'}

    def fiddle(self, schema):
        """
        """

        self.hide_fields(schema, ['SubGroup',
                                  'StorageLocation',
                                  'ClientOrderNumber',
                                  'ClientReference',
                                  'ReportDryMatter',
                                  'Composite',
                                  'SamplingDate',
                                  'DefaultContainerType',
                                  # ALS uses only DateSampled and Sampler fields
                                  # SamplingDate is just confusing them and us.
                                  'SamplingDate',
                                  ])

        # SamplingDate is not a required field!
        schema['SamplingDate'].required = False

        return schema
