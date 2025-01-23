import {fastApiClient} from "@/instance/axios-instance";

export async function sessionAdd(key: string, value: any): Promise<boolean>
{
    try
    {
        const response_ = await fastApiClient.post<{ status: string }>("/authentication/session-set", value, {
            params: {
                key
            }
        });

        return response_.data.status === "SUCCESS";
    }
    catch (e)
    {
        return false;
    }
}

export async function sessionGet(key: string): Promise<any>
{
    try
    {
        const response_ = await fastApiClient.get<{ value: any }>("/authentication/session-get", {params: {key}});

        return response_.data;
    }
    catch (e)
    {
        return null;
    }
}
