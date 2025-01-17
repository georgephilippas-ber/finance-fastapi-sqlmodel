import {getCompanyOverview} from "@/actions/financial/company";
import {CompanyOverview} from "@/components/server/company/company-overview";

export default async function ()
{
    const co = await getCompanyOverview([1, 2, 3]);

    return (
        <div>
            Hi
            {co.map((value, index) => <CompanyOverview key={index} company_overview={value}/>)}
        </div>
    );
}
