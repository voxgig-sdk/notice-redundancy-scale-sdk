# NoticeRedundancyScale SDK exists test

import pytest
from noticeredundancyscale_sdk import NoticeRedundancyScaleSDK


class TestExists:

    def test_should_create_test_sdk(self):
        testsdk = NoticeRedundancyScaleSDK.test(None, None)
        assert testsdk is not None
