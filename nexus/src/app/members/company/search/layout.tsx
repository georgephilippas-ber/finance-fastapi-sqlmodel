import {APPLICATION_NAVBAR_LOGO_URL} from "@/configuration/configuration";

export default function Layout({children}: { children: React.ReactNode; })
{
    return (
        <div className={"h-screen flex flex-col w-full"}>
            <header>
                <nav className="bg-white border-gray-200 dark:bg-gray-900 font-sans">
                    <div className="flex flex-wrap items-center justify-between mx-auto p-2">
                        <a href="/nexus/public" className="flex items-center space-x-3 rtl:space-x-reverse">
                            <img src={APPLICATION_NAVBAR_LOGO_URL} className="h-8" alt="logo"/>
                            <span className="self-center text-xl font-semibold whitespace-nowrap dark:text-white">
                                Fluent Investor
                            </span>
                        </a>
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
