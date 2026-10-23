# NoticeRedundancyScale SDK configuration


# The sekreto plugin DEFINITIONS the model selected per feature, imported
# above by name from the modules the catalogue's active `plugin.def`
# entries declare. Handed to each feature (secrets builds its Sekreto
# with them): a provider kind not listed here is unknown to that SDK.
FEATURE_PLUGINS = {
}


_shared_config = None


def shared_config():
    """Return the process-wide config, built once on first use.

    The SDK reads the config on every request and never writes to it, so one
    instance is shared by every client rather than rebuilt per client.

    The returned dict is shared: treat it as read-only. Callers that need to
    mutate should use make_config, which always returns a fresh copy.
    """
    global _shared_config
    if _shared_config is None:
        _shared_config = make_config()
    return _shared_config


def make_config():
    """Build a fresh, fully materialised config dict.

    Every call rebuilds the whole structure, so prefer shared_config unless
    you need a private copy you intend to mutate.
    """
    return {
        "main": {
            "name": "NoticeRedundancyScale",
            "slug": "notice-redundancy-scale",
            "version": "0.0.1",
            "target": "py",
        },
        "feature": {
            "ratelimit": {
        "options": {
          "active": False,
          "burst": 5,
          "rate": 5,
        },
        "optspec": {
          "now": "`$FUNCTION`",
          "sleep": "`$FUNCTION`",
        },
        "strict": False,
        "transport": "wrap",
      },
            "retry": {
        "options": {
          "active": False,
          "factor": 2,
          "maxDelay": 2000,
          "minDelay": 50,
          "retries": 2,
          "statuses": [
            408,
            425,
            429,
            500,
            502,
            503,
            504,
          ],
        },
        "optspec": {
          "jitter": "`$BOOLEAN`",
          "sleep": "`$FUNCTION`",
        },
        "strict": False,
        "transport": "wrap",
      },
            "test": {
        "options": {
          "active": False,
        },
        "optspec": {
          "entity": "`$MAP`",
          "net": "`$MAP`",
        },
        "strict": False,
        "transport": "base",
      },
            "timeout": {
        "options": {
          "active": False,
          "ms": 30000,
        },
        "optspec": {
          "clearTimer": "`$FUNCTION`",
          "now": "`$FUNCTION`",
          "setTimer": "`$FUNCTION`",
        },
        "strict": False,
        "transport": "wrap",
      },
        },
        "options": {
            "base": "https://noticeperiodaustralia.com",
            "auth": {
                "prefix": "Bearer",
            },
            "headers": {
        "content-type": "application/json",
      },
            "entity": {
                "calculator": {},
                "enquiry": {},
                "mcp": {},
            },
        },
        "entity": {
      "calculator": {
        "fields": [
          {
            "name": "instrumentWeeks",
            "title": "Instrument Weeks",
            "type": "`$NUMBER`",
            "short": "Notice in your award, agreement or contract",
          },
          {
            "name": "over45",
            "title": "Over45",
            "type": "`$STRING`",
            "short": "Over 45 on the day notice is given?",
          },
          {
            "name": "reason",
            "title": "Reason",
            "type": "`$STRING`",
            "short": "How is the employment ending?",
          },
          {
            "name": "weeklyPay",
            "title": "Weekly Pay",
            "type": "`$NUMBER`",
            "short": "Weekly pay",
          },
          {
            "name": "years",
            "title": "Years",
            "type": "`$NUMBER`",
            "short": "Completed years of continuous service",
          },
        ],
        "name": "calculator",
        "op": {
          "create": {
            "input": "data",
            "name": "create",
            "points": [
              {
                "kind": "http",
                "method": "POST",
                "orig": "/mcp/tools/calculate",
                "segments": [
                  {
                    "lit": "mcp",
                  },
                  {
                    "lit": "tools",
                  },
                  {
                    "lit": "calculate",
                  },
                ],
                "parts": [
                  "mcp",
                  "tools",
                  "calculate",
                ],
                "rename": {},
                "transform": {
                  "req": {
                    "instrumentWeeks": "`reqdata.instrument_week`",
                    "over45": "`reqdata.over45`",
                    "reason": "`reqdata.reason`",
                    "weeklyPay": "`reqdata.weekly_pay`",
                    "years": "`reqdata.year`",
                  },
                  "res": "`body`",
                },
                "args": {},
                "select": {},
                "response": {
                  "kind": "json",
                  "media": "application/json",
                },
              },
              {
                "kind": "http",
                "method": "POST",
                "orig": "/mcp/tools/calculator_describe",
                "segments": [
                  {
                    "lit": "mcp",
                  },
                  {
                    "lit": "tools",
                  },
                  {
                    "lit": "calculator_describe",
                  },
                ],
                "parts": [
                  "mcp",
                  "tools",
                  "calculator_describe",
                ],
                "rename": {},
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
                "args": {},
                "select": {},
                "response": {
                  "kind": "json",
                  "media": "application/json",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
      "enquiry": {
        "fields": [
          {
            "name": "answers",
            "title": "Answers",
            "type": "`$OBJECT`",
            "req": True,
            "short": "the person's answers, keyed by field key",
          },
          {
            "name": "confirmation",
            "title": "Confirmation",
            "type": "`$STRING`",
            "short": "the confirmation token from step 1, after the person has approved the summary",
          },
          {
            "name": "consent",
            "title": "Consent",
            "type": "`$BOOLEAN`",
            "req": True,
            "short": "true only when the person has agreed to: Send my contact details to up to three payroll and HR service providers, chosen by Notice Period Australia, who'll contact me directly.",
          },
        ],
        "name": "enquiry",
        "op": {
          "create": {
            "input": "data",
            "name": "create",
            "points": [
              {
                "kind": "http",
                "method": "POST",
                "orig": "/mcp/tools/enquiry_describe",
                "segments": [
                  {
                    "lit": "mcp",
                  },
                  {
                    "lit": "tools",
                  },
                  {
                    "lit": "enquiry_describe",
                  },
                ],
                "parts": [
                  "mcp",
                  "tools",
                  "enquiry_describe",
                ],
                "rename": {},
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
                "args": {},
                "select": {},
                "response": {
                  "kind": "json",
                  "media": "application/json",
                },
              },
              {
                "kind": "http",
                "method": "POST",
                "orig": "/mcp/tools/enquiry_fields",
                "segments": [
                  {
                    "lit": "mcp",
                  },
                  {
                    "lit": "tools",
                  },
                  {
                    "lit": "enquiry_fields",
                  },
                ],
                "parts": [
                  "mcp",
                  "tools",
                  "enquiry_fields",
                ],
                "rename": {},
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
                "args": {},
                "select": {},
                "response": {
                  "kind": "json",
                  "media": "application/json",
                },
              },
              {
                "kind": "http",
                "method": "POST",
                "orig": "/mcp/tools/submit_enquiry",
                "segments": [
                  {
                    "lit": "mcp",
                  },
                  {
                    "lit": "tools",
                  },
                  {
                    "lit": "submit_enquiry",
                  },
                ],
                "parts": [
                  "mcp",
                  "tools",
                  "submit_enquiry",
                ],
                "rename": {},
                "transform": {
                  "req": {
                    "answers": "`reqdata.answer`",
                    "confirmation": "`reqdata.confirmation`",
                    "consent": "`reqdata.consent`",
                  },
                  "res": "`body`",
                },
                "args": {},
                "select": {},
                "response": {
                  "kind": "json",
                  "media": "application/json",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
      "mcp": {
        "fields": [
          {
            "name": "id",
            "title": "Id",
            "type": "`$STRING`",
          },
          {
            "name": "jsonrpc",
            "title": "Jsonrpc",
            "type": "`$ANY`",
            "req": True,
          },
          {
            "name": "method",
            "title": "Method",
            "type": "`$STRING`",
            "req": True,
          },
          {
            "name": "params",
            "title": "Params",
            "type": "`$OBJECT`",
          },
        ],
        "id": {
          "field": "id",
          "name": "id",
        },
        "name": "mcp",
        "op": {
          "create": {
            "input": "data",
            "name": "create",
            "points": [
              {
                "kind": "http",
                "method": "POST",
                "orig": "/mcp",
                "segments": [
                  {
                    "lit": "mcp",
                  },
                ],
                "parts": [
                  "mcp",
                ],
                "rename": {},
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
                "args": {},
                "select": {},
                "response": {
                  "kind": "json",
                  "media": "application/json",
                },
              },
            ],
          },
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "kind": "http",
                "method": "GET",
                "orig": "/mcp",
                "segments": [
                  {
                    "lit": "mcp",
                  },
                ],
                "parts": [
                  "mcp",
                ],
                "rename": {},
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
                "args": {},
                "select": {},
                "response": {
                  "kind": "json",
                  "media": "application/json",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
    },
    }
