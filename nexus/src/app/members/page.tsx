import {CompanyOverview} from "@/components/server/company/company-overview";
import {search} from "@/actions/financial/company";

export default async function ()
{
    const query_result = await search("USD");

    return (
        <div className={"w-full h-full"}>
            <input className={"input w-full"} type={"text"} placeholder={"search"}/>
asdas
            <div className={"w-full flex flex-col gap-4 my-10 mx-auto p-10"}>
                {query_result.map((value, index) => <CompanyOverview key={index} company_overview={value}/>)}
            </div>
        </div>
    );
}
