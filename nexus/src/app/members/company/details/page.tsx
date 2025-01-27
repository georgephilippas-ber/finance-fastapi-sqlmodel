import Link from "next/link";
import {BiArrowBack} from "react-icons/bi";
import CompanyDetails from "@/components/client/company/company-details";

export default async function ({searchParams}: { searchParams?: { company_id?: string; ticker_id?: string; } })
{
    return (
        <div className={"p-2"}>
            <div className={"mb-2"}>
                <Link href={"/members/company/search"}>
                    <button className={"btn btn-primary"}>
                        <BiArrowBack className={"text-xl"}/>
                    </button>
                </Link>
            </div>
            {searchParams?.company_id && !isNaN(parseInt((await searchParams).company_id || "")) ?
                <CompanyDetails company_id={parseInt((await searchParams).company_id || "")}/> : null}
        </div>
    );
}
