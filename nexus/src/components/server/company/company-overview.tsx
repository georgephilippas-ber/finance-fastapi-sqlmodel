import {company_overview_type} from "@/schema/schema";

export function CompanyOverview({company_overview}: { company_overview: company_overview_type })
{
    return (
        <div
            className={"p-2 min-w-[20em] mx-auto w-4/5 cursor-pointer shadow-md shadow-gray-800 rounded-lg flex flex-row gap-2 "}>
            <div className={"w-full flex sm:hidden items-center justify-between gap-3"}>
                <img src={company_overview.company_logo_url} alt={company_overview.company_name}
                     className={"h-8 text-xs"}/>
                <div className={"text-sm"}>
                    {company_overview.ticker_code}.{company_overview.exchange_code}
                </div>
            </div>
            <div className={"w-full hidden sm:flex"}>
                {company_overview.company_name} {company_overview.ticker_code}.{company_overview.exchange_code}
            </div>
        </div>
    );
}
