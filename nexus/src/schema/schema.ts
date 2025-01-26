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

export type end_of_day_change_overview_type = {
    latest?: number;
    latest_date?: string;
    latest_adjusted?: number;
    beginning_of_month_adjusted?: number;
    beginning_of_year_adjusted?: number;
};

export type company_snapshot_metrics_type = {
    updated_at?: string; // using ISO 8601 date string format for dates

    market_capitalization: number;
    enterprise_value: number;

    return_on_assets: number;

    operating_profit_margin: number;
    net_profit_margin: number;

    price_earnings_ratio?: number;
    book_price_per_share: number;

    revenue: number;
    gross_profit: number;

    diluted_eps: number;

    price_to_book_ratio: number;

    shares_outstanding: number;
    shares_float: number;

    beta?: number;

    fifty_two_week_high: number;
    fifty_two_week_low: number;

    return_on_invested_capital?: number;
    debt_to_equity_ratio?: number;
    free_cash_flow_return_on_invested_capital?: number;

    return_on_equity?: number;
};

export type company_details_type = {
    company_overview: company_overview_type;
    company_snapshot_metrics: company_snapshot_metrics_type;
    end_of_day_change_overview?: end_of_day_change_overview_type
};
