import {fastApiClient} from "@/instance/axios-instance";

export async function login(identifier: string, password: string): Promise<boolean>
{
    try
    {
        const response_ = await fastApiClient.post('/authentication/login', {
            identifier,
            password,
        });

        fastApiClient.defaults.headers.common['Authorization'] = `Bearer ${response_.data.access_token}`;

        return true;
    }
    catch (e)
    {
        console.log(e);

        return false;
    }
}
