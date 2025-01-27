'use client'

import {TbSettings} from "react-icons/tb";
import {useRouter} from "next/navigation";

export function SettingsButton({className}: { className?: string })
{
    const router = useRouter();

    function handleClick()
    {
        router.push('/members/settings');
    }

    return (
        <button onClick={handleClick} className={["btn btn-primary", className || ""].join(" ").trim()}>
            <TbSettings className={"text-xl"}/>
        </button>
    );
}
