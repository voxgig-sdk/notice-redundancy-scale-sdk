# NoticeRedundancyScale SDK utility: make_context
require_relative '../core/context'
module NoticeRedundancyScaleUtilities
  MakeContext = ->(ctxmap, basectx) {
    NoticeRedundancyScaleContext.new(ctxmap, basectx)
  }
end
