export type company_overview_type = {
    company_id: number;
    ticker_id: number;
    company_name: string;
    ticker_code: string;
    exchange_code: string;
    currency_symbol: string;
    currency_code: string;
    gics_sector_name: string;
    gics_industry_name: string;
    company_logo_url: string;
    country_flag_url: string;
    description: string;
    country_common_name: string;
    country_official_name: string;
    country_cca2: string;
    country_cca3: string;
    continents: string;
};

export type metric_direction_type = 'DESC' | 'ASC';

export type metric_type =
    | 'market_capitalization'
    | 'return_on_assets'
    | 'operating_profit_margin';

export type group_type = 'GICSIndustry' | 'GICSSector' | 'country';

export type criterion_type = {
    metric: metric_type;
    metric_direction: metric_direction_type;
    groups: Array<[group_type | null, number]>;
};


export type end_of_day_change_overview_type = {
    latest?: number;
    latest_date?: string;
    latest_adjusted?: number;
    beginning_of_month_adjusted?: number;
    beginning_of_year_adjusted?: number;
};
