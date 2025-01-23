'use client'

import {CompanyOverview} from "@/components/server/company/company-overview";
import {search} from "@/actions/financial/company";

export default async function ()
{
    const query_result = await search("USD");

    function handleClick(company_id: number)
    {
        console.log(company_id);
    }

    return (
        <div className={"w-full flex flex-col h-full pt-12 px-4"}>
            <div className={"w-full flex flex-row gap-4"}>
                <input className={"input w-full"} type={"text"} placeholder={"search"}/>
                <button className={"btn btn-primary"}>Search</button>
            </div>
            <div className={"w-full flex-grow overflow-auto flex flex-col gap-4 my-10 mx-auto p-10"}>
                {query_result.map((value, index) => <CompanyOverview onClick={handleClick} key={index}
                                                                     company_overview={value}/>)}
            </div>
        </div>
    );
}
