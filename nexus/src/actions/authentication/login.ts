import {fastApiClient} from "@/instance/axios-instance";

export async function login(identifier: string, password: string): Promise<boolean>
{
    try
    {
        await fastApiClient.post('/authentication/login', {
            identifier,
            password,
        });

        return true;
    }
    catch (e)
    {
        console.log(e);

        return false;
    }
}
