import Link from "next/link";
import {BiArrowBack} from "react-icons/bi";

export default function ()
{
    return (
        <div className={"p-2"}>
            <div className={"mb-2"}>
                <Link href={"/members/company/search"}>
                    <button className={"btn btn-primary"}>
                        <BiArrowBack className={"text-xl"}/>
                    </button>
                </Link>
                <div>
                    {"Search Criteria"}
                </div>
            </div>
        </div>
    );
}