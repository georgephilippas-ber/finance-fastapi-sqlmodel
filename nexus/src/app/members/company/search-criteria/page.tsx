'use client'

import Link from "next/link";
import {BiArrowBack} from "react-icons/bi";
import {GroupOptions, MetricOptions} from "@/schema/criterion-schema";

export default function ()
{
    return (
        <div className={"p-2"}>
            <div className={"mb-2"}>
                <Link href={"/members/company/search"}>
                    <button className={"btn btn-primary"}>
                        <BiArrowBack className={"text-xl"}/>
                    </button>
                </Link>
                <p className={"text-2xl font-semibold text-center"}>
                    Search Criteria
                </p>
                <GroupOptions onSelect={console.log}/>
                <MetricOptions onSelect={console.log}/>
            </div>
        </div>
    );
}