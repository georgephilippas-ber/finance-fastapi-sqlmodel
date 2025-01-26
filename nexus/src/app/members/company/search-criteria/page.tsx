'use client'

import Link from "next/link";
import {BiArrowBack} from "react-icons/bi";
import {CriteriaList, criterion_type, CriterionInput} from "@/schema/criterion-schema";
import {useEffect, useState} from "react";
import {sessionAdd, sessionGet} from "@/actions/authentication/session";

export default function ()
{
    const [criteria, setCriteria] = useState<criterion_type[] | null>(null);

    useEffect(() =>
    {
        sessionGet("company.search.criteria").then(value =>
        {
            if (value)
            {
                setCriteria(value);
            }
        })
    }, [])

    useEffect(() =>
    {
        if (criteria !== null)
            sessionAdd("company.search.criteria", criteria).then(value =>
            {
                console.log(value);
            });
    }, [criteria])

    return (
        <div className={"p-2"}>
            <div className={"mb-2"}>
                <Link href={"/members/company/search"}>
                    <button className={"btn btn-primary"}>
                        <BiArrowBack className={"text-xl"}/>
                    </button>
                </Link>
                <p className={"text-2xl font-semibold text-center mb-4"}>
                    Search Criteria
                </p>

                <CriterionInput onChange={criterion =>
                {
                    setCriteria([...(criteria || []), {...criterion, id: crypto.randomUUID()}]);
                }} className={"mx-auto mb-4"}/>

                <CriteriaList className={"w-4/5 mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3"}
                              onDelete={id =>
                              {
                                  setCriteria(prevState =>
                                  {
                                      return (prevState || []).filter(value => value.id !== id)
                                  });
                              }} criteria={criteria || []}/>
            </div>
        </div>
    );
}
