export const fundamentalTimeSeriesKeys = [
    "assets",
    "liabilities",
    "cash",
    "net_debt",
    "net_working_capital",
    "capital_expenditure",
    "net_invested_capital",
    "free_cash_flow",
    "net_income",
    "equity",
    "return_on_equity",
    "free_cash_flow_return_on_assets",
    "debt_to_equity_ratio"
] as const;

export type fundamental_time_series_key_type = (typeof fundamentalTimeSeriesKeys)[number];

export type entry_type =
    {
        date: string;
        value: number;
    }
export type chart_data_type =
    {
        title: string;
        subtitle?: string;
        series_name: string;
        dependent_axis_title: string;
        data: entry_type[];
    }

export type fundamental_time_series_chart_data_type = {
    [key in fundamental_time_series_key_type]:
    {
        chart_data: chart_data_type;
        tooltip_point_format: string
    }
}

export const fundamentalTimeSeriesChartData: fundamental_time_series_chart_data_type =
    {
        assets:
            {
                chart_data: {
                    data: [],
                    series_name: "assets (million)",
                    dependent_axis_title: "assets (million)",
                    title: "Assets"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        liabilities:
            {
                chart_data: {
                    data: [],
                    series_name: "liabilities (million)",
                    dependent_axis_title: "liabilities (million)",
                    title: "Liabilities"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        cash:
            {
                chart_data: {
                    data: [],
                    series_name: "cash (million)",
                    dependent_axis_title: "cash (million)",
                    title: "Cash"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        net_debt:
            {
                chart_data: {
                    data: [],
                    series_name: "net debt (million)",
                    dependent_axis_title: "net debt (million)",
                    title: "Net Debt"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        net_working_capital:
            {
                chart_data: {
                    data: [],
                    series_name: "net working capital (million)",
                    dependent_axis_title: "net working capital (million)",
                    title: "Net Working Capital"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        capital_expenditure:
            {
                chart_data: {
                    data: [],
                    series_name: "capital expenditure (million)",
                    dependent_axis_title: "capital expenditure (million)",
                    title: "Capital Expenditure"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        net_invested_capital:
            {
                chart_data: {
                    data: [],
                    series_name: "net invested capital (million)",
                    dependent_axis_title: "net invested capital (million)",
                    title: "Net Invested Capital"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        free_cash_flow:
            {
                chart_data: {
                    data: [],
                    series_name: "free cash flow (million)",
                    dependent_axis_title: "free cash flow (million)",
                    title: "Free Cash Flow"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        net_income:
            {
                chart_data: {
                    data: [],
                    series_name: "net income (million)",
                    dependent_axis_title: "net income (million)",
                    title: "Net Income"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        equity:
            {
                chart_data: {
                    data: [],
                    series_name: "equity (million)",
                    dependent_axis_title: "equity (million)",
                    title: "Equity"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        return_on_equity:
            {
                chart_data: {
                    data: [],
                    series_name: "return on equity",
                    dependent_axis_title: "return on equity",
                    title: "Return on Equity"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        free_cash_flow_return_on_assets:
            {
                chart_data: {
                    data: [],
                    series_name: "free cash flow return on assets",
                    dependent_axis_title: "free cash flow return on assets",
                    title: "Free Cash Flow Return on Assets"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        debt_to_equity_ratio:
            {
                chart_data: {
                    data: [],
                    series_name: "debt to equity ratio",
                    dependent_axis_title: "debt to equity ratio",
                    title: "Debt to Equity Ratio"
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            }
    };


export function adapt_fundamental_time_series_single(key: fundamental_time_series_key_type, fundamental_time_series: any[]): entry_type[]
{
    return fundamental_time_series.map(value =>
    {
        return {
            date: value["record_date"],
            value: value[key]
        };
    })
}


export function adapt(fundamental_time_series: any[]): { chart_data: chart_data_type; tooltip_point_format: string }[]
{
    return fundamentalTimeSeriesKeys.map(value =>
    {
        const chart_ = fundamentalTimeSeriesChartData[value];

        chart_.chart_data.data = adapt_fundamental_time_series_single(value, fundamental_time_series);

        return chart_;
    });
}
