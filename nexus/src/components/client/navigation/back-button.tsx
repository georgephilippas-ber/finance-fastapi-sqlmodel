'use client'

import {BiArrowBack} from "react-icons/bi";
import {useRouter} from "next/navigation";

export function BackButton()
{
    const router = useRouter();

    return (
        <button onClick={event => router.back()} className={"btn btn-primary"}>
            <BiArrowBack className={"text-xl"}/>
        </button>
    );
}
