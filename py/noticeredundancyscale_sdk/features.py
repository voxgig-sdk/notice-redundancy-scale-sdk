# NoticeRedundancyScale SDK feature factory

from noticeredundancyscale_sdk.feature.base_feature import NoticeRedundancyScaleBaseFeature
from noticeredundancyscale_sdk.feature.ratelimit_feature import NoticeRedundancyScaleRatelimitFeature
from noticeredundancyscale_sdk.feature.retry_feature import NoticeRedundancyScaleRetryFeature
from noticeredundancyscale_sdk.feature.test_feature import NoticeRedundancyScaleTestFeature
from noticeredundancyscale_sdk.feature.timeout_feature import NoticeRedundancyScaleTimeoutFeature


_FEATURES = {
    "base": lambda: NoticeRedundancyScaleBaseFeature(),
    "ratelimit": lambda: NoticeRedundancyScaleRatelimitFeature(),
    "retry": lambda: NoticeRedundancyScaleRetryFeature(),
    "test": lambda: NoticeRedundancyScaleTestFeature(),
    "timeout": lambda: NoticeRedundancyScaleTimeoutFeature(),
}


def _make_feature(name):
    factory = _FEATURES.get(name)
    if factory is not None:
        return factory()
    return _FEATURES["base"]()


# True when this SDK was generated with the named feature class - the
# constructor's tolerance for extend-carried features reads this (an
# active name with no generated class must not become a BaseFeature
# stray when an extend instance carries it).
def _has_feature(name):
    return name in _FEATURES
