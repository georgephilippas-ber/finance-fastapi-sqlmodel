import {fastapiClient} from "@/instances/axios-instance";

export async function login(identifier: string, password: string): Promise<boolean>
{
    try
    {
        await fastapiClient.post('/authentication/login', {
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
