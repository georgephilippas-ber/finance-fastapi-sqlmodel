export default function ({searchParams}: { searchParams?: { company_id?: string } })
{
    return (
        <div>
            COMPANY DETAILS {searchParams?.company_id}
        </div>
    );
}
