import {fastApiClient} from "@/instance/axios-instance";
import {company_details_type, company_overview_type} from "@/schema/schema";
import {criterion_type} from "@/schema/criterion-schema";

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

export async function retrieveCompanyOverview(company_ids: number[]): Promise<company_overview_type[]>
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

export async function retrieveCompanyOverviewSingle(company_id: number): Promise<company_overview_type | undefined>
{
    const array_ = await retrieveCompanyOverview([company_id]);

    if (array_.length)
    {
        return array_[0];
    }
    else
        return undefined;
}

export async function retrieveCompanyDetails(company_id: number): Promise<company_details_type | undefined>
{
    try
    {
        const response_ = await fastApiClient.get<company_details_type>("/company/details", {
            params:
                {
                    company_id,
                }
        });

        return response_.data;
    }
    catch (err)
    {
        console.log(err);

        return undefined;
    }

}
