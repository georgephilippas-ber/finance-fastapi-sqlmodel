export type metric_direction_type = 'DESC' | 'ASC';

export type metric_type =
    | 'market_capitalization'
    | 'return_on_assets'
    | 'operating_profit_margin';

export type group_type = 'GICSIndustry' | 'GICSSector' | 'country';

type metric_display_type = {
    [key in metric_type]: string
}

type group_display_type = {
    [key in group_type]: string
}

export const metrics_array: metric_display_type = {
    'market_capitalization': 'market capitalization',
    'return_on_assets': 'return on assets',
    'operating_profit_margin': 'operating profit margin'
};

export const groups_array: group_display_type = {
    'GICSIndustry': 'industry',
    'GICSSector': 'sector',
    'country': 'country'
};

export type criterion_type = {
    id?: string;
    metric: metric_type;
    metric_direction: metric_direction_type;
    groups: Array<[group_type | null, number]>;
};
