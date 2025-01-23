import {fastApiClient} from "@/instance/axios-instance";

export async function add(key: string, value: any): Promise<boolean>
{
    try
    {
        const response_ = await fastApiClient.post<{ status: string }>("authentication/session-set", value, {
            params: {
                key
            }
        });

        return response_.data.status === "success";
    }
    catch (e)
    {
        return false;
    }
}

export async function get(key: string): Promise<any>
{
    try
    {
        const response_ = await fastApiClient.get<{ value: any }>("authentication/session-get", {params: {key}});

        return response_.data;
    }
    catch (e)
    {
        return null;
    }
}
