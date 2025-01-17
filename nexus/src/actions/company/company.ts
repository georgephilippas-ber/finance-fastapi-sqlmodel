import {company_overview_type} from "@/schema/schema";
import {fastApiClient} from "@/instance/axios-instance";

export async function getCompanyOverview(ids: number[]): Promise<company_overview_type[]>
{
    try
    {
        const response_ = await fastApiClient.get<company_overview_type[]>("/company/overview", {
            params:
                {
                    ids
                },
        });

        return response_.data;
    }
    catch (err)
    {
        return [];
    }
}
