import Link from "next/link";

export default async function ({searchParams}: { searchParams?: { company_id?: string; ticker_id?: string; } })
{
    return (
        <div>
            <Link href={"/members/company/search"}>
                Search
            </Link>

            COMPANY DETAILS {searchParams?.company_id} - {searchParams?.ticker_id}
        </div>
    );
}
