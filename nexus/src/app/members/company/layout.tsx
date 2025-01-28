import {APPLICATION_HOME_URL} from "@/configuration/configuration";
import {LogoutButton} from "@/components/client/authentication/logout";
import {headers} from "next/headers";
import {faker} from "@faker-js/faker";
import {LanguageSelector} from "@/components/client/internationalization/language-selector";
import {SettingsButton} from "@/components/client/navigation/settings-button";

function title(referer: string | null | undefined): string
{
    if (referer)
    {
        const elements_ = referer.split("/");

        if (elements_.some(value => value === "company"))
            return "Company";

        return "";
    }
    else
        return "";
}

export default async function Layout({children}: { children: React.ReactNode; })
{
    const headers_ = await headers();

    return (
        <div className={"h-screen flex flex-col w-full"}>
            <header>
                <nav className="bg-white border-gray-200 dark:bg-gray-900 font-sans">
                    <div className="flex flex-wrap items-center justify-between mx-auto p-2">
                        <a href={APPLICATION_HOME_URL} className="flex items-center">
                            <span className={"text-2xl font-bold tracking-widest ml-1"}>
                                investi
                            </span>
                            <span className={"text-sm mt-2 font-semibold"}>
                                gator
                            </span>
                        </a>

                        <div className={"text-xl font-semibold"}>
                            {title(headers_.get("x-pathname"))}
                        </div>

                        <div className={"m-0.5 gap-2 flex flex-row items-center"}>
                            <SettingsButton/>
                            <LogoutButton/>
                        </div>
                    </div>
                </nav>
            </header>
            <main className="flex-grow overflow-y-auto">
                {children}
            </main>
            <footer className="h-8">
                <div className="text-center text-gray-500 text-sm">
                    <strong>{faker.finance.ethereumAddress()}</strong>
                </div>
            </footer>
        </div>
    );
}
