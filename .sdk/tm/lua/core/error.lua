-- NoticeRedundancyScale SDK error

local json = require("dkjson")

local NoticeRedundancyScaleError = {}
NoticeRedundancyScaleError.__index = NoticeRedundancyScaleError

-- Reachable for a debugger, absent from the table itself: the context holds
-- the live spec and options, and an error is what gets dumped or encoded.
local CONTEXT = setmetatable({}, { __mode = "k" })


function NoticeRedundancyScaleError.new(code, msg, ctx)
  local self = setmetatable({}, NoticeRedundancyScaleError)
  self.is_sdk_error = true
  self.sdk = "NoticeRedundancyScale"
  self.code = code or ""
  self.msg = msg or ""
  self.result = nil
  self.spec = nil
  self.status = -1
  CONTEXT[self] = ctx
  return self
end


function NoticeRedundancyScaleError:context()
  return CONTEXT[self]
end


function NoticeRedundancyScaleError:error()
  return self.msg
end


function NoticeRedundancyScaleError:not_found()
  return 404 == self.status
end


-- What make_error attached is already cleaned; the context is not part of
-- the record.
function NoticeRedundancyScaleError:to_table()
  return {
    sdk = self.sdk,
    code = self.code,
    msg = self.msg,
    status = self.status,
    result = self.result,
    spec = self.spec,
  }
end


function NoticeRedundancyScaleError:to_json()
  return json.encode(self:to_table())
end


function NoticeRedundancyScaleError:__tostring()
  return self.msg
end


function NoticeRedundancyScaleError.__tojson(self)
  return self:to_json()
end


return NoticeRedundancyScaleError
