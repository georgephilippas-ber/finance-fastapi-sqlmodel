import {company_overview_type} from "@/schema/schema";

export function CompanyOverview({company_overview}: { company_overview: company_overview_type })
{
    return (
        <div className={"p-2 min-w-[10em] border border-gray-200 rounded-lg flex flex-row gap-2"}>
            <div>

            </div>
            {/*{JSON.stringify(company_overview)}*/}
        </div>
    );
}
