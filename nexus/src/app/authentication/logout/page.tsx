'use client'

import {fastApiClient} from "@/instance/axios-instance";
import {useRouter} from "next/navigation";
import {useEffect} from "react";

export default function ()
{
    const router = useRouter();

    useEffect(() =>
        {
            fastApiClient.post('/authentication/logout').then(value =>
            {
                fastApiClient.defaults.headers.common['Authorization'] = undefined;

                router.push('/authentication/login');
            });
        }, []
    );

    return null;
}
