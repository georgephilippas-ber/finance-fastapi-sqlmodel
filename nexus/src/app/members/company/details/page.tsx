import Link from "next/link";
import {BiArrowBack} from "react-icons/bi";
import {EndOfDayChangeOverview} from "@/components/server/end-of-day-change-overview/end-of-day-change-overview";
import {fake_endOfDayChangeOverview} from "@/core/fake/end-of-day-change-overview";

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

            <EndOfDayChangeOverview currencySymbol={"$"} fake endOfDayChangeOverview={fake_endOfDayChangeOverview()}/>
        </div>
    );
}
