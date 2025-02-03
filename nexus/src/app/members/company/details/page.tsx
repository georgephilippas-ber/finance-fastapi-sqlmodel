import CompanyDetails from "@/components/client/company/company-details";
import {BackButton} from "@/components/server/navigation/back-button";
import {CompanyFundamentalTimeSeries} from "@/components/client/company-fundamental-time-series";

export default async function ({searchParams}: { searchParams?: any })
{
    const company_id = parseInt((await searchParams).company_id || "");

    return (
        <div className={"p-2"}>
            <div className={"mb-2"}>
                <BackButton href={"/members/company/search"}/>
            </div>
            {!isNaN(company_id) ? <CompanyDetails company_id={company_id}/> : null}

            {!isNaN(company_id) ? <CompanyFundamentalTimeSeries company_id={company_id}/> : null}
        </div>
    );
}
