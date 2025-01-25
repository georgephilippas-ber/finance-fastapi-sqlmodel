'use client'

import {useEffect, useState} from "react";
import {company_details_type} from "@/schema/schema";
import {retrieveCompanyDetails} from "@/actions/financial/company";
import {CompanyOverview} from "@/components/server/company/company-overview";
import {EndOfDayChangeOverview} from "@/components/server/end-of-day-change-overview/end-of-day-change-overview";
import {ClipLoader} from "react-spinners";
import {CompanySnapshotMetrics} from "@/components/server/company/company-snapshot-metrics";

export default function CompanyDetails({company_id}: { company_id: number })
{
    const [companyDetails, setCompanyDetails] = useState<company_details_type | undefined>(undefined);
    const [isLoading, set_isLoading] = useState<boolean>(true);

    useEffect(() =>
    {
        retrieveCompanyDetails(company_id).then(value =>
        {
            setCompanyDetails(value);

            set_isLoading(false);
        });
    }, []);

    return (
        <>
            {isLoading || !companyDetails ?
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
                        <div className={"hidden lg:block lg:rounded-xl"}>
                            <img className={"w-12"} src={companyDetails.company_overview.country_flag_url}
                                 alt={companyDetails.company_overview.country_cca3}/>
                        </div>
                        <div className={"text-xl"}>
                            {companyDetails.company_overview.company_name}
                        </div>
                        <EndOfDayChangeOverview
                            endOfDayChangeOverview={companyDetails?.end_of_day_change_overview}
                            currencySymbol={companyDetails.company_overview.currency_symbol}/>
                    </div>

                    {companyDetails?.company_overview ?
                        <CompanyOverview company_overview={companyDetails.company_overview}/> : null}

                    {companyDetails?.company_snapshot_metrics ?
                        <CompanySnapshotMetrics currency_code={companyDetails.company_overview.currency_code}
                                                company_snapshot_metrics={companyDetails.company_snapshot_metrics}/> : null}
                </div>}
        </>
    )
}
