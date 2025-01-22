import {fastApiClient} from "@/instance/axios-instance";
import {company_overview_type, criterion_type} from "@/schema/schema";

export async function search(query: string | undefined = undefined, criteria: criterion_type[] | undefined = undefined): Promise<company_overview_type[]>
{
    try
    {
        const response_ = await fastApiClient.post<company_overview_type[]>("/company/search", criteria, {
            params:
                {
                    query: query,
                },
        });

        return response_.data;
    }
    catch (err)
    {
        return [];
    }
}
