'use client'

import {Login} from "@/components/client/authentication/login";

export default function ()
{
    return (
        <section className={"font-sans"}>
            <Login success_url={"/"}/>
        </section>
    );
}
