'use client'

import {useRouter} from "next/navigation";
import {fastApiClient} from "@/instance/axios-instance";
import {TbLogout2} from "react-icons/tb";

export function Logout()
{
    const router = useRouter();

    async function handleClick()
    {
        await fastApiClient.post('/authentication/logout');

        router.push('/authentication/login');
    }

    return (
        <button onClick={handleClick} className={"btn"}>
            <TbLogout2/>
        </button>
    );
}
