
import { test, describe } from 'node:test'
import { equal } from 'node:assert'


import { NoticeRedundancyScaleSDK } from '..'


describe('exists', async () => {

  test('test-mode', () => {
    const testsdk = NoticeRedundancyScaleSDK.test()
    equal(testsdk instanceof NoticeRedundancyScaleSDK, true,
      'NoticeRedundancyScaleSDK.test() must return a client synchronously')
  })

})
