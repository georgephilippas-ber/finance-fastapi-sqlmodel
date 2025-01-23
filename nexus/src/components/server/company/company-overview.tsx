import {company_overview_type} from "@/schema/schema";

export function CompanyOverview({company_overview}: { company_overview: company_overview_type })
{
    return (
        <div
            className={"p-2 min-w-[20em] mx-auto w-4/5 cursor-pointer shadow-md shadow-gray-800 rounded-lg flex flex-row gap-2 "}>
            <div className={"w-full flex sm:hidden items-center justify-between gap-3"}>
                <img src={company_overview.company_logo_url} alt={company_overview.company_name}
                     className={"h-8 text-xs overflow-hidden w-8"}/>
                <div className={"text-sm"}>
                    <strong>{company_overview.ticker_code}</strong>.<span
                    className={"text-xs"}>{company_overview.exchange_code}</span>
                </div>
            </div>
            <div className={"w-full hidden sm:grid grid-rows-2 grid-cols-[auto,1fr,auto] gap-4 h-full"}>
                <div className="row-span-1  p-4">Top Left</div>
                <div className="row-span-1  p-4">Top Center</div>
                <div className="row-span-1 p-4">Top Right</div>

                <div className="row-span-1  p-4">Bottom Left</div>
                <div className="row-span-1  p-4">Bottom Center</div>
                <div className="row-span-1  p-4">Bottom Right</div>
            </div>
        </div>
    );
}
