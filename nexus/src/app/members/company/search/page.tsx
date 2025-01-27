'use client'

import {CompanyOverviewListElement} from "@/components/client/company/company-overview-list-element";
import {search} from "@/actions/financial/company";
import {useEffect, useState} from "react";
import {company_overview_type} from "@/schema/schema";
import {AiFillSetting} from "react-icons/ai";
import {sessionAdd, sessionGet} from "@/actions/authentication/session";
import {useRouter} from "next/navigation";
import {criterion_type} from "@/schema/criterion-schema";

import "../../../../i18n/i18n";
import {useTranslation} from "react-i18next";

export default function ()
{
    const [queryResults, setQueryResults] = useState<company_overview_type[]>([]);

    const [query, setQuery] = useState<string | null>(null);
    const [criteria, setCriteria] = useState<criterion_type[]>([]);

    const router = useRouter();

    useEffect(() =>
    {
        sessionGet("company.search").then(value =>
        {
            console.log(value);

            if (value)
                setQuery(value["query"]);
        });

        sessionGet("company.search.criteria").then(value =>
        {
            console.log(value);

            if (value)
                setCriteria(value);
        });
    }, []);

    useEffect(() =>
        {
            if (query || criteria.length)
                search(query, criteria.length ? criteria : undefined).then(value => setQueryResults(value));
            else
                setQueryResults([]);

            if (query != null)
                sessionAdd("company.search", {query: query}).then(value =>
                {
                    console.log(value);
                });
        },
        [query, criteria]);

    function handleClick(company_id: number, ticker_id: number)
    {
        router.push("/members/company/details?company_id=" + company_id + "&ticker_id=" + ticker_id);
    }

    const {t} = useTranslation("company_search");

    return (
        <div className={"w-full flex flex-col h-full pt-12 px-4"}>
            <div className={"sm:w-4/5 sm:mx-auto flex flex-row gap-4 w-full"}>
                <input value={query || ""} onChange={event => setQuery(event.target.value)} className={"input w-full"}
                       type={"text"} placeholder={"search"}/>
                <button className={"btn btn-primary"}
                        onClick={event => router.push("/members/company/search-criteria")}>
                    <AiFillSetting className={"text-xl"}/>
                </button>
            </div>
            <div className={"w-fit mx-auto text-2xl font-semibold my-4"}>
                {queryResults.length === 0 ? t("no-results") : t("result-count", {count: queryResults.length})}
            </div>
            <div className={"w-4/5 p-4 flex-grow overflow-auto flex flex-col gap-4 mx-auto my-10"}>
                {queryResults.map((value, index) =>
                    <CompanyOverviewListElement onClick={handleClick} key={index} company_overview={value}/>
                )}
            </div>
        </div>
    );
}
