# NoticeRedundancyScale SDK utility: prepare_body
require_relative 'media'
module NoticeRedundancyScaleUtilities
  PrepareBody = ->(ctx) {
    return nil unless ctx.op.input == "data"
    return NoticeRedundancyScaleUtilities.raw_body(ctx.reqdata) if NoticeRedundancyScaleUtilities.raw_request?(ctx.point)
    ctx.utility.transform_request.call(ctx)
  }
end
