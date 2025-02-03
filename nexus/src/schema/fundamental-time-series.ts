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

function fundamentalTimeSeriesChartData(t: (key: string) => string): fundamental_time_series_chart_data_type
{
    return {
        assets:
            {
                chart_data: {
                    data: [],
                    series_name: t("assets.y_axis"),
                    dependent_axis_title: t("assets.y_axis"),
                    title: t("assets.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        liabilities:
            {
                chart_data: {
                    data: [],
                    series_name: t("liabilities.y_axis"),
                    dependent_axis_title: t("liabilities.y_axis"),
                    title: t("liabilities.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        cash:
            {
                chart_data: {
                    data: [],
                    series_name: t("cash.y_axis"),
                    dependent_axis_title: t("cash.y_axis"),
                    title: t("cash.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        net_debt:
            {
                chart_data: {
                    data: [],
                    series_name: t("net_debt.y_axis"),
                    dependent_axis_title: t("net_debt.y_axis"),
                    title: t("net_debt.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        net_working_capital:
            {
                chart_data: {
                    data: [],
                    series_name: t("net_working_capital.y_axis"),
                    dependent_axis_title: t("net_working_capital.y_axis"),
                    title: t("net_working_capital.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        capital_expenditure:
            {
                chart_data: {
                    data: [],
                    series_name: t("capital_expenditure.y_axis"),
                    dependent_axis_title: t("capital_expenditure.y_axis"),
                    title: t("capital_expenditure.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        net_invested_capital:
            {
                chart_data: {
                    data: [],
                    series_name: t("net_invested_capital.y_axis"),
                    dependent_axis_title: t("net_invested_capital.y_axis"),
                    title: t("net_invested_capital.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        free_cash_flow:
            {
                chart_data: {
                    data: [],
                    series_name: t("free_cash_flow.y_axis"),
                    dependent_axis_title: t("free_cash_flow.y_axis"),
                    title: t("free_cash_flow.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        net_income:
            {
                chart_data: {
                    data: [],
                    series_name: t("net_income.y_axis"),
                    dependent_axis_title: t("net_income.y_axis"),
                    title: t("net_income.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        equity:
            {
                chart_data: {
                    data: [],
                    series_name: t("equity.y_axis"),
                    dependent_axis_title: t("equity.y_axis"),
                    title: t("equity.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        return_on_equity:
            {
                chart_data: {
                    data: [],
                    series_name: t("return_on_equity.y_axis"),
                    dependent_axis_title: t("return_on_equity.y_axis"),
                    title: t("return_on_equity.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        free_cash_flow_return_on_assets:
            {
                chart_data: {
                    data: [],
                    series_name: t("free_cash_flow_return_on_assets.y_axis"),
                    dependent_axis_title: t("free_cash_flow_return_on_assets.y_axis"),
                    title: t("free_cash_flow_return_on_assets.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            },
        debt_to_equity_ratio:
            {
                chart_data: {
                    data: [],
                    series_name: t("debt_to_equity_ratio.y_axis"),
                    dependent_axis_title: t("debt_to_equity_ratio.y_axis"),
                    title: t("debt_to_equity_ratio.title"),
                },
                tooltip_point_format: '{series.name}: <b>{point.y:.2f}</b>'
            }
    };
}

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


export function adapt(fundamental_time_series: any[], t: (key: string) => string): {
    chart_data: chart_data_type;
    tooltip_point_format: string
}[]
{
    return fundamentalTimeSeriesKeys.map(value =>
    {
        const chart_ = fundamentalTimeSeriesChartData(t)[value];

        chart_.chart_data.data = adapt_fundamental_time_series_single(value, fundamental_time_series);

        return chart_;
    });
}
