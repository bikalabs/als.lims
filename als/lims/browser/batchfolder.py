from bika.lims import bikaMessageFactory as _
from bika.lims.browser.batchfolder import BatchFolderContentsView as bfcv
from plone.app.content.browser.interfaces import IFolderContentsView
from zope.interface import implements


class BatchFolderContentsView(bfcv):
    implements(IFolderContentsView)

    def __init__(self, context, request):
        super(BatchFolderContentsView, self).__init__(context, request)

        self.columns = {
            'Title': {'title': _('Title')},
            'BatchDate': {'title': _('Date')},
            'Client': {'title': _('Client')},
            'state_title': {'title': _('State'), 'sortable': False},
        }

        self.review_states = [
            {'id': 'default',
             'contentFilter': {'review_state': 'open'},
             'title': _('Open'),
             'transitions': [{'id': 'close'}, {'id': 'cancel'}],
             'columns': ['Title',
                         'BatchDate',
                         'Client',
                         'state_title', ]
             },
            {'id': 'closed',
             'contentFilter': {'review_state': 'closed'},
             'title': _('Closed'),
             'transitions': [{'id': 'open'}],
             'columns': ['Title',
                         'BatchDate',
                         'Client',
                         'state_title', ]
             },
            {'id': 'cancelled',
             'title': _('Cancelled'),
             'transitions': [{'id': 'reinstate'}],
             'contentFilter': {'cancellation_state': 'cancelled'},
             'columns': ['Title',
                         'BatchDate',
                         'Client',
                         'state_title', ]
             },
            {'id': 'all',
             'title': _('All'),
             'transitions': [],
             'columns': ['Title',
                         'BatchDate',
                         'Client',
                         'state_title', ]
             },
        ]
