import Link from "next/link";
import {BiArrowBack} from "react-icons/bi";

export function BackButton({href}: { href: string })
{
    return <Link href={href}>
        <button className={"btn btn-primary"}>
            <BiArrowBack className={"text-xl"}/>
        </button>
    </Link>
}
