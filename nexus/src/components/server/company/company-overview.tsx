import {company_overview_type} from "@/schema/schema";

export function CompanyOverview({company_overview}: { company_overview: company_overview_type })
{
    return (
        <div>
            {JSON.stringify(company_overview)}
        </div>
    );
}
