import CompanyDetails from "@/components/client/company/company-details";
import {BackButton} from "@/components/server/navigation/back-button";

export default async function ({searchParams}: { searchParams?: any })
{
    return (
        <div className={"p-2"}>
            <div className={"mb-2"}>
                <BackButton href={"/members/company/search"}/>
            </div>
            {searchParams?.company_id && !isNaN(parseInt((await searchParams).company_id || "")) ?
                <CompanyDetails company_id={parseInt((await searchParams).company_id || "")}/> : null}
        </div>
    );
}
