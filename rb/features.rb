# NoticeRedundancyScale SDK feature factory

require_relative 'feature/base_feature'
require_relative 'feature/ratelimit_feature'
require_relative 'feature/retry_feature'
require_relative 'feature/test_feature'
require_relative 'feature/timeout_feature'


module NoticeRedundancyScaleFeatures
  def self.make_feature(name)
    case name
    when "base"
      NoticeRedundancyScaleBaseFeature.new
    when "ratelimit"
      NoticeRedundancyScaleRatelimitFeature.new
    when "retry"
      NoticeRedundancyScaleRetryFeature.new
    when "test"
      NoticeRedundancyScaleTestFeature.new
    when "timeout"
      NoticeRedundancyScaleTimeoutFeature.new
    else
      NoticeRedundancyScaleBaseFeature.new
    end
  end
end
