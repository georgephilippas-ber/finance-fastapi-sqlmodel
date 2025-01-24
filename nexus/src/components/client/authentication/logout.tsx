'use client'

import {useRouter} from "next/navigation";
import {fastApiClient} from "@/instance/axios-instance";
import {TbLogout2} from "react-icons/tb";

export function LogoutButton()
{
    const router = useRouter();

    async function handleClick()
    {
        await fastApiClient.post('/authentication/logout');

        router.push('/authentication/login');
    }

    return (
        <button onClick={handleClick} className={"btn btn-primary"}>
            <TbLogout2/>
        </button>
    );
}
