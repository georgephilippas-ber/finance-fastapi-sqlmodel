import Link from "next/link";
import {BiArrowBack} from "react-icons/bi";

export default async function ({searchParams}: { searchParams?: { company_id?: string; ticker_id?: string; } })
{
    return (
        <div className={"p-2"}>
            <div className={"mb-6"}>
                <Link href={"/members/company/search"}>
                    <button className={"btn btn-primary"}>
                        <BiArrowBack className={"text-xl"}/>
                    </button>
                </Link>
            </div>

            COMPANY DETAILS {searchParams?.company_id} - {searchParams?.ticker_id}
        </div>
    );
}
