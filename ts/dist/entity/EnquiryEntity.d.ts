import { NoticeRedundancyScaleEntityBase } from '../NoticeRedundancyScaleEntityBase';
import type { NoticeRedundancyScaleSDK } from '../NoticeRedundancyScaleSDK';
import type { Control } from '../types';
import type { Enquiry, EnquiryCreateData } from '../NoticeRedundancyScaleTypes';
declare class EnquiryEntity extends NoticeRedundancyScaleEntityBase<Enquiry> {
    constructor(client: NoticeRedundancyScaleSDK, entopts: any);
    make(this: EnquiryEntity): EnquiryEntity;
    create(this: any, reqdata?: EnquiryCreateData, ctrl?: Control): Promise<EnquiryEntity>;
}
export { EnquiryEntity };
