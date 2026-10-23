export interface Calculator {
    instrumentWeeks?: number;
    over45?: string;
    reason?: string;
    weeklyPay?: number;
    years?: number;
}
export interface CalculatorCreateData {
    instrumentWeeks?: number;
    over45?: string;
    reason?: string;
    weeklyPay?: number;
    years?: number;
}
export interface Enquiry {
    answers: Record<string, any>;
    confirmation?: string;
    consent: boolean;
}
export interface EnquiryCreateData {
    answers: Record<string, any>;
    confirmation?: string;
    consent: boolean;
}
export interface Mcp {
    id?: string;
    jsonrpc: any;
    method: string;
    params?: Record<string, any>;
}
export interface McpLoadMatch {
    id: string;
    jsonrpc?: any;
    method?: string;
    params?: Record<string, any>;
}
export interface McpCreateData {
    id?: string;
    jsonrpc: any;
    method: string;
    params?: Record<string, any>;
}
