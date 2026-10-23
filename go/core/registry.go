package core

var UtilityRegistrar func(u *Utility)

var NewBaseFeatureFunc func() Feature

var NewRatelimitFeatureFunc func() Feature

var NewRetryFeatureFunc func() Feature

var NewTestFeatureFunc func() Feature

var NewTimeoutFeatureFunc func() Feature

var NewCalculatorEntityFunc func(client *NoticeRedundancyScaleSDK, entopts map[string]any) NoticeRedundancyScaleEntity

var NewEnquiryEntityFunc func(client *NoticeRedundancyScaleSDK, entopts map[string]any) NoticeRedundancyScaleEntity

var NewMcpEntityFunc func(client *NoticeRedundancyScaleSDK, entopts map[string]any) NoticeRedundancyScaleEntity

