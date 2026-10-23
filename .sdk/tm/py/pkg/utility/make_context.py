# NoticeRedundancyScale SDK utility: make_context

from projectname_sdk.core.context import NoticeRedundancyScaleContext


def make_context_util(ctxmap, basectx):
    return NoticeRedundancyScaleContext(ctxmap, basectx)
