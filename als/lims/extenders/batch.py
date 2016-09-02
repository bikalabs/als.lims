from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.lims.interfaces import IBatch
from zope.component import adapts
from zope.interface import implements


class BatchSchemaExtender(object):
    adapts(IBatch)
    implements(IOrderableSchemaExtender)

    fields = [
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields


class BatchSchemaModifier(object):
    adapts(IBatch)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    def hide_fields(self, schema, fieldnames):
        """Hide fields ALS doesn't care to see
        """
        for fn in fieldnames:
            if fn in schema:
                schema[fn].widget.visible = {"view": "invisible",
                                             "edit": "invisible"}

    def fiddle(self, schema):
        """
        """

        self.hide_fields(schema, ["ClientBatchID",
                                  "description",
                                  "InheritedObjectsUI",
                                  "BatchLabels",
                                  "Remarks"])

        return schema
