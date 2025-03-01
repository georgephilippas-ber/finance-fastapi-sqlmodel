'use client'

import {company_overview_type} from "@/schema/schema";

import "../../../i18n/i18n";
import {useTranslation} from "react-i18next";

export function CompanyOverview({company_overview}: { company_overview: company_overview_type })
{
    const {t} = useTranslation("company_details");

    return (
        <div className={"font-sans w-full m-1"}>
            <div className={"flex flex-row items-center justify-start gap-4"}>
                <div className={"m-2"}>
                    <span className={"text-2xl"}>
                        {company_overview.ticker_code}
                    </span>.
                    <span className={"font-semibold"}>
                        {company_overview.exchange_code}
                    </span>
                </div>
                <div className={"font-semibold text-lg"}>
                    {company_overview.currency_code}
                </div>
            </div>
            <details open className={"m-2 dropdown"}>
                <summary className={"text-lg cursor-pointer"}>
                    {t("description")}
                </summary>
                <p className={"text-sm text-justify p-4"}>
                    {company_overview.description}
                </p>
            </details>
        </div>
    );
}
