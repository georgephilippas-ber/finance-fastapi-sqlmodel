import {company_snapshot_metrics_type} from "@/schema/schema";
import React from "react";

import "../../../i18n/i18n";
import {useTranslation} from "react-i18next";

type metric_entry_type = {
    name: string;
    value: number | null | undefined;
    currency_code?: string;
    format: (value: number | null | undefined, currency_code?: string) => string;
}

type table_type = {
    title: string,
    entry_array: Array<metric_entry_type>
}

function getSizeTable(companySnapshotMetrics: company_snapshot_metrics_type, currency_code: string, t: (key: string) => string): table_type
{
    return {
        title: t("table.company_size"),
        entry_array: [
            {
                name: "MCAP",
                value: companySnapshotMetrics.market_capitalization,
                currency_code: currency_code,
                format: currencyFormat
            },
            {
                name: "EV",
                value: companySnapshotMetrics.enterprise_value,
                currency_code: currency_code,
                format: currencyFormat
            },
            {
                name: "Rev",
                value: companySnapshotMetrics.revenue,
                currency_code: currency_code,
                format: currencyFormat
            }
        ]
    }
}

function getProfitabilityTable(companySnapshotMetrics: company_snapshot_metrics_type, currency_code: string, t: (key: string) => string): table_type
{
    return {
        title: t("table.profitability"),
        entry_array: [
            {
                name: "GPM",
                value: companySnapshotMetrics.gross_profit / companySnapshotMetrics.revenue,
                currency_code: currency_code,
                format: percentageFormat
            },
            {
                name: "OM",
                value: companySnapshotMetrics.operating_profit_margin,
                currency_code: currency_code,
                format: percentageFormat
            },
            {
                name: "NPM",
                value: companySnapshotMetrics.net_profit_margin,
                currency_code: currency_code,
                format: percentageFormat
            }
        ]
    }
}

function getReturnTable(companySnapshotMetrics: company_snapshot_metrics_type, currency_code: string, t: (key: string) => string): table_type
{
    return {
        title: t("table.return"),
        entry_array: [
            {
                name: "ROA",
                value: companySnapshotMetrics.return_on_assets,
                currency_code: currency_code,
                format: percentageFormat
            },
            {
                name: "ROIC",
                value: companySnapshotMetrics.return_on_invested_capital,
                currency_code: currency_code,
                format: percentageFormat
            },
            {
                name: "ROE",
                value: companySnapshotMetrics.return_on_equity,
                currency_code: currency_code,
                format: percentageFormat
            },
        ]
    }
}

function getValuationTable(companySnapshotMetrics: company_snapshot_metrics_type, currency_code: string, t: (key: string) => string): table_type
{
    return {
        title: t("table.valuation"),
        entry_array: [
            {
                name: "P/B",
                value: companySnapshotMetrics.price_to_book_ratio,
                currency_code: currency_code,
                format: ratioFormat
            },
            {
                name: "P/E",
                value: companySnapshotMetrics.price_earnings_ratio,
                currency_code,
                format: ratioFormat
            },
            {
                name: "DEPS",
                value: companySnapshotMetrics.diluted_eps,
                currency_code,
                format: currencyFormat
            },
            {
                name: "BVPS",
                value: companySnapshotMetrics.book_price_per_share,
                currency_code,
                format: currencyFormat
            }
        ]
    }
}

function getTechnicalsTable(companySnapshotMetrics: company_snapshot_metrics_type, currency_code: string, t: (key: string) => string): table_type
{
    return {
        title: t("table.shares_and_technicals"),
        entry_array: [
            {
                name: "β",
                value: companySnapshotMetrics.beta,
                currency_code: currency_code,
                format: decimalFormat
            },
            {
                name: "SO",
                value: companySnapshotMetrics.shares_outstanding,
                currency_code: currency_code,
                format: largeNumberFormat
            },
            {
                name: "Float",
                value: companySnapshotMetrics.shares_float,
                currency_code: currency_code,
                format: largeNumberFormat
            },
        ]
    }
}

function getPriceTable(companySnapshotMetrics: company_snapshot_metrics_type, currency_code: string, t: (key: string) => string): table_type
{
    return {
        title: t("table.price_movement"),
        entry_array: [
            {
                name: "52-HIGH",
                value: companySnapshotMetrics.fifty_two_week_high,
                currency_code: currency_code,
                format: currencyFormat
            },
            {
                name: "52-LOW",
                value: companySnapshotMetrics.fifty_two_week_low,
                currency_code: currency_code,
                format: currencyFormat
            },
        ]
    }
}

function getFundamentalsTable(companySnapshotMetrics: company_snapshot_metrics_type, currency_code: string, t: (key: string) => string): table_type
{
    return {
        title: t("table.fundamentals"),
        entry_array: [
            {
                name: "D/E",
                value: companySnapshotMetrics.debt_to_equity_ratio,
                currency_code: currency_code,
                format: ratioFormat
            },
            {
                name: "FCF-ROIC",
                value: companySnapshotMetrics.free_cash_flow_return_on_invested_capital,
                currency_code: currency_code,
                format: percentageFormat
            }
        ]
    }
}

function Grid({table}: { table: table_type | undefined })
{
    if (table)
        return (
            <div
                className={"min-w-[12em] p-4 border border-white rounded-lg flex flex-col items-stretch w-full justify-start h-full"}>
                <p className={"text-xs mb-4 w-full text-center"}>
                    {table.title.toUpperCase()}
                </p>
                <div className={"grid grid-cols-[auto_auto] gap-2"}>
                    {table.entry_array.map((value, index) =>
                    {
                        return (
                            <React.Fragment key={[table.title, index].join("-")}>
                                <div className={"text-sm font-semibold"}>
                                    {value.name}
                                </div>
                                <div className={"text-sm overflow-x-auto"}>
                                    {value.format(value.value, value.currency_code)}
                                </div>
                            </React.Fragment>
                        )
                    })}
                </div>
            </div>)
    else
        return (
            <div className={"p-2 border border-white rounded-lg"}>
                <p className={"text-sm mb-5 w-full text-center"}>
                    {"DATA ERROR"}
                </p>
            </div>
        );
}

function currencyFormat(value: number | null | undefined, currency_code?: string): string
{
    if (value)
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: currency_code,
            minimumFractionDigits: 2,
            maximumFractionDigits: 2,
        }).format(value);
    else
        return "-";
}

function largeNumberFormat(value: number | null | undefined, currency_code?: string): string
{
    if (value)
        return new Intl.NumberFormat('en-US', {
            style: 'decimal',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0,
        }).format(value);
    else
        return "-";
}

function percentageFormat(value: number | null | undefined, currency_code?: string): string
{
    return value ? (value * 1.e2).toFixed(2) + "%" : "-";
}

function ratioFormat(value: number | null | undefined, currency_code?: string): string
{
    return value ? value.toFixed(2) : "-";
}

function decimalFormat(value: number | null | undefined, currency_code?: string): string
{
    return value ? value.toFixed(2) : "-";
}

export function CompanySnapshotMetrics({company_snapshot_metrics, currency_code}: {
    company_snapshot_metrics: company_snapshot_metrics_type;
    currency_code: string;
})
{
    const {t} = useTranslation("company_details");

    const sizeTable = getSizeTable(company_snapshot_metrics, currency_code, t);
    const profitabilityTable = getProfitabilityTable(company_snapshot_metrics, currency_code, t);
    const returnTable = getReturnTable(company_snapshot_metrics, currency_code, t);
    const valuationTable = getValuationTable(company_snapshot_metrics, currency_code, t);
    const technicalsTable = getTechnicalsTable(company_snapshot_metrics, currency_code, t);
    const priceTable = getPriceTable(company_snapshot_metrics, currency_code, t);
    const fundamentalsTable = getFundamentalsTable(company_snapshot_metrics, currency_code, t);

    return (
        <>
            <p className={"text-xl font-semibold text-center mb-4"}>
                {t("title")}
            </p>
            <div
                className={"font-sans mx-auto w-4/5 m-2 grid justify-items-center xs:grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2"}>
                <Grid table={sizeTable}/>
                <Grid table={profitabilityTable}/>
                <Grid table={returnTable}/>
                <Grid table={valuationTable}/>
                <Grid table={technicalsTable}/>
                <Grid table={priceTable}/>
                <Grid table={fundamentalsTable}/>
            </div>
        </>
    );
}
