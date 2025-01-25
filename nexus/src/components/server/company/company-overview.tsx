'use client'

import {company_overview_type} from "@/schema/schema";

export default function CompanyOverview({company_overview}: { company_overview: company_overview_type })
{
    return (
        <div className={"font-sans w-fit"}>
            <details>
                <summary className={"text-lg"}>Description</summary>
                <p className={"text-sm"}>
                    {company_overview.description}
                </p>
            </details>
        </div>
    );
}
