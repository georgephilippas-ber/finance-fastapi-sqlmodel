import {APPLICATION_NAVBAR_LOGO_URL} from "@/configuration/configuration";
import {LogoutButton} from "@/components/client/authentication/logout";
import {headers} from "next/headers";

function title(referer: string | null | undefined): string
{
    if (referer)
    {
        const elements_ = referer.split("/");

        if (elements_.some(value => value === "company"))
        {
            if (elements_.some(value => value === "search"))
                return "Company Search";

            if (elements_.some(value => value === "details"))
                return "Company Details";
        }

        return "";
    }
    else
        return "";
}

export default async function Layout({children}: { children: React.ReactNode; })
{
    const headers_ = await headers();

    console.log(headers_.get("Referer"));

    return (
        <div className={"h-screen flex flex-col w-full"}>
            <header>
                <nav className="bg-white border-gray-200 dark:bg-gray-900 font-sans">
                    <div className="flex flex-wrap items-center justify-between mx-auto p-2">
                        <a href="/nexus/public" className="flex items-center space-x-3 rtl:space-x-reverse">
                            <img src={APPLICATION_NAVBAR_LOGO_URL} className="h-8" alt="logo"/>
                        </a>
                        <div className={"text-xl font-semibold"}>
                            {title(headers_.get("Referer"))}
                        </div>
                        <LogoutButton/>
                    </div>
                </nav>
            </header>
            <main className="flex-grow overflow-y-auto">
                {children}
            </main>
            <footer className="h-8">
                <div className="text-center text-gray-500 text-sm">
                    © {new Date().getFullYear()} <strong>Fluent Investor</strong>.
                </div>
            </footer>
        </div>
    );
}
