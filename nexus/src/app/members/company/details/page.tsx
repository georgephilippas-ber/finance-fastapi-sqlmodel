export default async function ({searchParams}: { searchParams?: { company_id?: string } })
{
    return (
        <div>
            COMPANY DETAILS {(await searchParams)?.company_id}
        </div>
    );
}
