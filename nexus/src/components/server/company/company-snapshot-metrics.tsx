import {company_snapshot_metrics_type} from "@/schema/schema";

function currencyFormat(value: number, currency_code: string): string
{
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: currency_code,
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
    }).format(value);
}

export function CompanySnapshotMetrics({company_snapshot_metrics, currency_code}: {
    company_snapshot_metrics: company_snapshot_metrics_type;
    currency_code: string;
})
{
    return (
        <div className={"font-sans w-4/5 m-2"}>
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
        </div>
    );
}
