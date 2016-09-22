from bika.lims.browser.analysisrequest.analysisrequests import \
    AnalysisRequestsView as ARV
from bika.lims.browser.batch.analysisrequests import \
    AnalysisRequestsView as BARV
from bika.lims.browser.client.views.analysisrequests import \
    AnalysisRequestsView as CARV
from plone.app.content.browser.interfaces import IFolderContentsView
from zope.interface import implements


class AnalysisRequestsView(ARV):
    """Hide SamplingDate from listing views (if SWE is enabled)
    """
    implements(IFolderContentsView)

    def __init__(self, context, request):
        super(AnalysisRequestsView, self).__init__(context, request)
        if context.bika_setup.getSamplingWorkflowEnabled():
            for x in range(len(self.review_states)):
                if 'SamplingDate' in self.review_states[x]['columns']:
                    self.review_states[x]['columns'].remove('SamplingDate')


class ClientAnalysisRequestsView(CARV):
    """Hide SamplingDate from listing views (if SWE is enabled)
    """
    implements(IFolderContentsView)

    def __init__(self, context, request):
        super(ClientAnalysisRequestsView, self).__init__(context, request)
        if context.bika_setup.getSamplingWorkflowEnabled():
            for x in range(len(self.review_states)):
                if 'SamplingDate' in self.review_states[x]['columns']:
                    self.review_states[x]['columns'].remove('SamplingDate')


class BatchAnalysisRequestsView(BARV):
    """Hide SamplingDate from listing views (if SWE is enabled)
    """
    implements(IFolderContentsView)

    def __init__(self, context, request):
        super(BatchAnalysisRequestsView, self).__init__(context, request)
        if context.bika_setup.getSamplingWorkflowEnabled():
            for x in range(len(self.review_states)):
                if 'SamplingDate' in self.review_states[x]['columns']:
                    self.review_states[x]['columns'].remove('SamplingDate')
