-- NoticeRedundancyScale SDK exists test

local sdk = require("notice-redundancy-scale_sdk")

describe("NoticeRedundancyScaleSDK", function()
  it("should create test SDK", function()
    local testsdk = sdk.test(nil, nil)
    assert.is_not_nil(testsdk)
  end)
end)
