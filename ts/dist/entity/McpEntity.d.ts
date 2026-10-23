import { NoticeRedundancyScaleEntityBase } from '../NoticeRedundancyScaleEntityBase';
import type { NoticeRedundancyScaleSDK } from '../NoticeRedundancyScaleSDK';
import type { Control } from '../types';
import type { Mcp, McpLoadMatch, McpCreateData } from '../NoticeRedundancyScaleTypes';
declare class McpEntity extends NoticeRedundancyScaleEntityBase<Mcp> {
    constructor(client: NoticeRedundancyScaleSDK, entopts: any);
    make(this: McpEntity): McpEntity;
    load(this: any, reqmatch?: McpLoadMatch, ctrl?: Control): Promise<McpEntity>;
    create(this: any, reqdata?: McpCreateData, ctrl?: Control): Promise<McpEntity>;
}
export { McpEntity };
