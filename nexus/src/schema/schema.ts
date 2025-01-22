type company_overview_type = {
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

type MetricDirectionType = 'DESC' | 'ASC';

type MetricType =
    | 'market_capitalization'
    | 'return_on_assets'
    | 'operating_profit_margin';

type GroupType = 'GICSIndustry' | 'GICSSector' | 'country';

type Criterion = {
    metric: MetricType;
    metric_direction: MetricDirectionType;
    groups: Array<[GroupType | null, number]>;
};
