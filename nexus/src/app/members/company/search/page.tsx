'use client'

import {CompanyOverview} from "@/components/server/company/company-overview";
import {search} from "@/actions/financial/company";
import {useEffect, useState} from "react";
import {company_overview_type} from "@/schema/schema";
import {AiFillSetting} from "react-icons/ai";

export default function ()
{
    const [queryResults, setQueryResults] = useState<company_overview_type[]>([]);

    const [query, setQuery] = useState<string>("");

    useEffect(() =>
        {
            if (query)
                search(query).then(value => setQueryResults(value));
            else
                setQueryResults([]);
        },
        [query]);

    function handleClick(company_id: number)
    {
        console.log(company_id);
    }

    return (
        <div className={"w-full flex flex-col h-full pt-12 px-4"}>
            <div className={"sm:w-4/5 sm:mx-auto flex flex-row gap-4 w-full"}>
                <input value={query} onChange={event => setQuery(event.target.value)} className={"input w-full"}
                       type={"text"} placeholder={"search"}/>
                <button className={"btn btn-primary"}>
                    <AiFillSetting className={"text-xl"}/>
                </button>
            </div>
            <div className={"w-4/5 p-4 flex-grow overflow-auto flex flex-col gap-4 mx-auto my-10"}>
                {queryResults.map((value, index) => <CompanyOverview onClick={handleClick} key={index}
                                                                     company_overview={value}/>)}
            </div>
        </div>
    );
}
