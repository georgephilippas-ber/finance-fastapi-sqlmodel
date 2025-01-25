'use client'

import {useEffect, useState} from "react";
import {company_details_type} from "@/schema/schema";
import {retrieveCompanyDetails} from "@/actions/financial/company";
import CompanyOverview from "@/components/server/company/company-overview";
import {EndOfDayChangeOverview} from "@/components/server/end-of-day-change-overview/end-of-day-change-overview";
import {ClipLoader} from "react-spinners";

export default function CompanyDetails({company_id}: { company_id: number })
{
    const [companyDetails, setCompanyDetails] = useState<company_details_type | undefined>(undefined);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() =>
    {
        retrieveCompanyDetails(company_id).then(value =>
        {
            setCompanyDetails(value);

            setTimeout(() => setLoading(false), 1000)
            // setLoading(false);
        });
    }, []);

    return (
        <>
            {loading || !companyDetails ?
                <div className={"w-fit mx-auto mt-20"}>
                    <ClipLoader
                        color={"lightgray"}
                        cssOverride={{
                            width: "10em",
                            height: "10em"
                        }}
                        aria-label="Loading Spinner"
                    />
                </div> :
                <div>
                    <div
                        className={"flex flex-col items-center sm:gap-4 md:justify-evenly md:flex-row md:w-full mx-auto"}>
                        <img src={companyDetails.company_overview.company_logo_url}
                             alt={companyDetails.company_overview.company_name}
                             className={"w-20 overflow-x-hidden text-xs text-nowrap rounded-xl"}/>
                        <div className={"text-xl"}>
                            {companyDetails.company_overview.company_name}
                        </div>
                        <EndOfDayChangeOverview
                                                endOfDayChangeOverview={companyDetails?.end_of_day_change_overview as any}
                                                currencySymbol={companyDetails?.company_overview.currency_symbol as any}/>
                    </div>

                    {companyDetails?.company_overview ?
                        <CompanyOverview company_overview={companyDetails.company_overview}/> : null}
                </div>}
        </>
    )
}
