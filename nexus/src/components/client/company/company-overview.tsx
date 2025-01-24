'use client'

import {company_overview_type} from "@/schema/schema";

export function CompanyOverview({company_overview, onClick}: {
    company_overview: company_overview_type,
    onClick?: (company_id: number, ticker_id: number) => void
})
{
    return (
        <div onClick={event => onClick?.(company_overview.company_id, company_overview.ticker_id)}
             className={"p-2 min-w-[18em] mx-auto w-full cursor-pointer shadow-md shadow-gray-800 rounded-lg flex flex-row gap-2 "}>
            <div className={"w-full flex sm:hidden items-center justify-between gap-3"}>
                <img src={company_overview.company_logo_url} alt={company_overview.company_name}
                     className={"w-8 h-8 text-xs overflow-hidden"}/>
                <div className={"text-sm"}>
                    <strong>{company_overview.ticker_code}</strong>.<span
                    className={"text-xs"}>{company_overview.exchange_code}</span>
                </div>
            </div>
            <div className={"w-full hidden sm:grid grid-rows-2 grid-cols-[auto,1fr,auto] gap-4 h-full"}>
                <div className="row-span-2 place-content-center p-2">
                    <img src={company_overview.company_logo_url} alt={company_overview.company_name}
                         className={"w-10 h-10 text-xs overflow-hidden"}/>
                </div>
                <div className="row-span-1 text-xl">
                    {company_overview.company_name}
                </div>
                <div className="row-span-1 flex justify-end gap-3">
                    <img src={company_overview.country_flag_url} alt={company_overview.company_name}
                         className={"h-6 text-xs overflow-hidden w-6"}/>
                    <div className={"text-xl"}>
                        {company_overview.currency_symbol}
                    </div>
                </div>
                <div className="row-span-1 text-sm">
                    {company_overview.gics_sector_name} / {company_overview.gics_industry_name}
                </div>
                <div className="row-span-1 min-w-40 flex justify-end">
                    <div className={"text-sm w-fit"}>
                        <strong>{company_overview.ticker_code}</strong>.<span
                        className={"text-xs"}>{company_overview.exchange_code}</span>
                    </div>
                </div>
            </div>
        </div>
    );
}
