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

export async function companyOverview(company_ids: number[]): Promise<company_overview_type[]>
{
    try
    {

        const response_ = await fastApiClient.get<company_overview_type[]>("/company/overview", {
            params:
                {
                    company_ids: company_ids.join(',')
                }
        });

        return response_.data;
    }
    catch (err)
    {
        console.log(err);

        return [];
    }
}

export async function companyOverviewSingle(company_id: number): Promise<company_overview_type | undefined>
{
    const array_ = await companyOverview([company_id]);

    if (array_.length)
    {
        return array_[0];
    }
    else
        return undefined;
}
