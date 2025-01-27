export type metric_direction_type = 'DESC' | 'ASC';

export type metric_type =
    | 'market_capitalization'
    | 'enterprise_value'
    | 'revenue'
    | 'return_on_assets'
    | 'return_on_invested_capital'
    | 'free_cash_flow_return_on_invested_capital'
    | 'return_on_equity'
    | 'net_profit_margin'
    | 'price_earnings_ratio'
    | 'price_to_book_ratio'
    | 'beta'
    | 'debt_to_equity_ratio'
    | 'operating_profit_margin'


export type group_type = 'GICSSector' | 'GICSIndustryGroup' | 'GICSIndustry' | 'GICSSubIndustry' | 'country';

type metric_display_type = {
    [key in metric_type]: string
}

type group_display_type = {
    [key in group_type]: string
}

export const metrics_dictionary: metric_display_type = {
    market_capitalization: 'market capitalization',
    return_on_assets: 'return on assets',
    operating_profit_margin: 'operating profit margin',
    beta: 'beta',
    debt_to_equity_ratio: 'debt-to-equity ratio',
    enterprise_value: 'enterprise value',
    free_cash_flow_return_on_invested_capital: 'FCF return on invested capital',
    net_profit_margin: 'net profit margin',
    price_earnings_ratio: 'price-earnings ratio',
    price_to_book_ratio: 'price-to-book ratio',
    revenue: 'revenue',
    return_on_equity: 'return on equity',
    return_on_invested_capital: 'return on invested capital'
};

export const groups_dictionary: group_display_type = {
    country: 'country',
    GICSSector: 'sector',
    GICSIndustryGroup: 'industry group',
    GICSIndustry: 'industry',
    GICSSubIndustry: 'sub-industry',
};

export type criterion_type = {
    id?: string;
    metric: metric_type;
    metric_direction: metric_direction_type;
    groups: Array<[group_type | null, number]>;
};
