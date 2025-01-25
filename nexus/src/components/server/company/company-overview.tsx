'use client'

import {company_overview_type} from "@/schema/schema";

export default function CompanyOverview({company_overview}: { company_overview: company_overview_type })
{
    return (
        <div className={"font-sans w-full m-1"}>
            <details open>
                <summary className={"text-lg"}>Description</summary>
                <p className={"text-sm text-justify p-4"}>
                    {company_overview.description}
                </p>
            </details>
        </div>
    );
}
