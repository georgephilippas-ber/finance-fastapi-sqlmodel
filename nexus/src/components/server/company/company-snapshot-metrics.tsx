import {company_snapshot_metrics_type} from "@/schema/schema";

function currencyFormat(value: number | null | undefined, currency_code: string): string
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

function percentageFormat(value: number | null | undefined): string
{
    return value ? (value * 1.e2).toFixed(2) + "%" : "-";
}

function ratioFormat(value: number | null | undefined): string
{
    return value ? value.toFixed(2) : "-";
}

function SizeMetrics({company_snapshot_metrics, currency_code}: {
    company_snapshot_metrics: company_snapshot_metrics_type,
    currency_code: string
})
{
    return (
        <div>
            <p className={"text-2xl"}>
                Company Size
            </p>
            <table className={"p-2 m-5"}>
                <thead>
                <tr>
                    <th className={"w-[8em]"}>

                    </th>
                    <th className={"w-40"}>

                    </th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <th className={"text-left text-lg font-semibold"}>
                        MCAP
                    </th>
                    <td>
                        {currencyFormat(company_snapshot_metrics.market_capitalization, currency_code)}
                    </td>
                </tr>
                <tr>
                    <th className={"text-left text-lg font-semibold"}>
                        EV
                    </th>
                    <td>
                        {currencyFormat(company_snapshot_metrics.enterprise_value, currency_code)}
                    </td>
                </tr>
                <tr>
                    <th className={"text-left text-lg font-semibold"}>
                        ND
                    </th>
                    <td>
                        {currencyFormat(company_snapshot_metrics.enterprise_value - company_snapshot_metrics.market_capitalization, currency_code)}
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    )
}

function ProfitabilityMetrics({company_snapshot_metrics, currency_code}: {
    company_snapshot_metrics: company_snapshot_metrics_type,
    currency_code: string
})
{
    return (
        <div>
            <p className={"text-2xl"}>
                Profitability
            </p>
            <table className={"p-2 m-5"}>
                <thead>
                <tr>
                    <th className={"w-[8em]"}>

                    </th>
                    <th className={"w-40"}>

                    </th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <th className={"text-left text-lg font-semibold"}>
                        OM
                    </th>
                    <td>
                        {percentageFormat(company_snapshot_metrics.operating_profit_margin)}
                    </td>
                </tr>
                <tr>
                    <th className={"text-left text-lg font-semibold"}>
                        NPM
                    </th>
                    <td>
                        {percentageFormat(company_snapshot_metrics.net_profit_margin)}
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    );
}

function ReturnMetrics({company_snapshot_metrics, currency_code}: {
    company_snapshot_metrics: company_snapshot_metrics_type,
    currency_code: string
})
{
    return (
        <div>
            <p className={"text-2xl"}>
                Return
            </p>
            <table className={"p-2 m-5"}>
                <thead>
                <tr>
                    <th className={"w-[8em]"}>

                    </th>
                    <th className={"w-40"}>

                    </th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <th className={"text-left text-lg font-semibold"}>
                        ROA
                    </th>
                    <td>
                        {percentageFormat(company_snapshot_metrics.return_on_assets)}
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    );
}

function ValuationMetrics({company_snapshot_metrics, currency_code}: {
    company_snapshot_metrics: company_snapshot_metrics_type,
    currency_code: string
})
{
    return (
        <div>
            <p className={"text-2xl"}>
                Valuation
            </p>
            <table className={"p-2 m-5"}>
                <thead>
                <tr>
                    <th className={"w-[8em]"}>

                    </th>
                    <th className={"w-40"}>

                    </th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <th className={"text-left text-lg font-semibold"}>
                        P/E
                    </th>
                    <td>
                        {ratioFormat(company_snapshot_metrics.price_earnings_ratio)}
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    );
}

export function CompanySnapshotMetrics({company_snapshot_metrics, currency_code}: {
    company_snapshot_metrics: company_snapshot_metrics_type;
    currency_code: string;
})
{
    return (
        <div className={"font-sans mx-auto w-4/5 m-2 grid xs:grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4"}>
            <SizeMetrics company_snapshot_metrics={company_snapshot_metrics} currency_code={currency_code}/>
            <ProfitabilityMetrics company_snapshot_metrics={company_snapshot_metrics} currency_code={currency_code}/>
            <ReturnMetrics company_snapshot_metrics={company_snapshot_metrics} currency_code={currency_code}/>
            <ValuationMetrics company_snapshot_metrics={company_snapshot_metrics} currency_code={currency_code}/>
        </div>
    );
}
