# NoticeRedundancyScale SDK utility registration
require_relative '../core/utility_type'
require_relative 'clean'
require_relative 'done'
require_relative 'make_error'
require_relative 'feature_add'
require_relative 'feature_hook'
require_relative 'feature_init'
require_relative 'fetcher'
require_relative 'make_fetch_def'
require_relative 'make_context'
require_relative 'make_options'
require_relative 'make_request'
require_relative 'make_response'
require_relative 'make_result'
require_relative 'make_point'
require_relative 'make_spec'
require_relative 'make_url'
require_relative 'param'
require_relative 'prepare_auth'
require_relative 'prepare_body'
require_relative 'prepare_headers'
require_relative 'prepare_method'
require_relative 'prepare_params'
require_relative 'prepare_path'
require_relative 'prepare_query'
require_relative 'graphql'
require_relative 'result_basic'
require_relative 'result_body'
require_relative 'result_headers'
require_relative 'transform_request'
require_relative 'transform_response'

NoticeRedundancyScaleUtility.registrar = ->(u) {
  u.clean = NoticeRedundancyScaleUtilities::Clean
  u.clean_add = NoticeRedundancyScaleUtilities::CleanAdd
  u.clean_explain = NoticeRedundancyScaleUtilities::CleanExplain
  u.done = NoticeRedundancyScaleUtilities::Done
  u.make_error = NoticeRedundancyScaleUtilities::MakeError
  u.feature_add = NoticeRedundancyScaleUtilities::FeatureAdd
  u.feature_hook = NoticeRedundancyScaleUtilities::FeatureHook
  u.feature_init = NoticeRedundancyScaleUtilities::FeatureInit
  u.fetcher = NoticeRedundancyScaleUtilities::Fetcher
  u.make_fetch_def = NoticeRedundancyScaleUtilities::MakeFetchDef
  u.make_context = NoticeRedundancyScaleUtilities::MakeContext
  u.make_options = NoticeRedundancyScaleUtilities::MakeOptions
  u.make_request = NoticeRedundancyScaleUtilities::MakeRequest
  u.make_response = NoticeRedundancyScaleUtilities::MakeResponse
  u.make_result = NoticeRedundancyScaleUtilities::MakeResult
  u.make_point = NoticeRedundancyScaleUtilities::MakePoint
  u.make_spec = NoticeRedundancyScaleUtilities::MakeSpec
  u.make_url = NoticeRedundancyScaleUtilities::MakeUrl
  u.param = NoticeRedundancyScaleUtilities::Param
  u.prepare_auth = NoticeRedundancyScaleUtilities::PrepareAuth
  u.prepare_body = NoticeRedundancyScaleUtilities::PrepareBody
  u.prepare_headers = NoticeRedundancyScaleUtilities::PrepareHeaders
  u.prepare_method = NoticeRedundancyScaleUtilities::PrepareMethod
  u.prepare_params = NoticeRedundancyScaleUtilities::PrepareParams
  u.prepare_path = NoticeRedundancyScaleUtilities::PreparePath
  u.prepare_query = NoticeRedundancyScaleUtilities::PrepareQuery
  u.graphql_body = NoticeRedundancyScaleUtilities::GraphqlBody
  u.graphql_errors = NoticeRedundancyScaleUtilities::GraphqlErrors
  u.result_basic = NoticeRedundancyScaleUtilities::ResultBasic
  u.result_body = NoticeRedundancyScaleUtilities::ResultBody
  u.result_headers = NoticeRedundancyScaleUtilities::ResultHeaders
  u.transform_request = NoticeRedundancyScaleUtilities::TransformRequest
  u.transform_response = NoticeRedundancyScaleUtilities::TransformResponse
}
