import {CompanyOverview} from "@/components/server/company/company-overview";
import {search} from "@/actions/financial/company";

export default async function ()
{
    const query_result = await search("USD");

    console.log(query_result);

    return (
        <div>
            Hi
            {query_result.map((value, index) => <CompanyOverview key={index} company_overview={value}/>)}
        </div>
    );
}
