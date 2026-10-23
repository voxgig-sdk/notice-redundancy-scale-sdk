import { NoticeRedundancyScaleEntityBase } from '../NoticeRedundancyScaleEntityBase';
import type { NoticeRedundancyScaleSDK } from '../NoticeRedundancyScaleSDK';
import type { Control } from '../types';
import type { Calculator, CalculatorCreateData } from '../NoticeRedundancyScaleTypes';
declare class CalculatorEntity extends NoticeRedundancyScaleEntityBase<Calculator> {
    constructor(client: NoticeRedundancyScaleSDK, entopts: any);
    make(this: CalculatorEntity): CalculatorEntity;
    create(this: any, reqdata?: CalculatorCreateData, ctrl?: Control): Promise<CalculatorEntity>;
}
export { CalculatorEntity };
