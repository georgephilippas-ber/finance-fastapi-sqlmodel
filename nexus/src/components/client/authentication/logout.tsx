'use client'

import {useRouter} from "next/navigation";
import {fastApiClient} from "@/instance/axios-instance";
import {TbLogout2} from "react-icons/tb";

export function LogoutButton({className}: { className?: string })
{
    const router = useRouter();

    async function handleClick()
    {
        await fastApiClient.post('/authentication/logout');

        router.push('/authentication/login');
    }

    return (
        <button onClick={handleClick} className={["btn btn-primary", className || ""].join(" ").trim()}>
            <TbLogout2/>
        </button>
    );
}
