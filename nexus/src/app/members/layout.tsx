import {APPLICATION_NAVBAR_LOGO_URL} from "@/configuration/configuration";

export default function Layout({children}: { children: React.ReactNode; })
{
    return (
        <div className={"h-screen flex flex-col"}>
            <header>
                <nav className="bg-white border-gray-200 dark:bg-gray-900 font-sans">
                    <div className="flex flex-wrap items-center justify-between mx-auto p-2">
                        <a href="/" className="flex items-center space-x-3 rtl:space-x-reverse">
                            <img src={APPLICATION_NAVBAR_LOGO_URL} className="h-8" alt="logo"/>
                            <span className="self-center text-xl font-semibold whitespace-nowrap dark:text-white">
                                Fluent Investor
                            </span>
                        </a>
                        <button data-collapse-toggle="navbar-default" type="button"
                                className="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
                            <span className="sr-only">Open main menu</span>
                            <svg className="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none"
                                 viewBox="0 0 17 14">
                                <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2"
                                      d="M1 1h15M1 7h15M1 13h15"/>
                            </svg>
                        </button>
                        <div className="hidden w-full md:block md:w-auto mr-3">
                            <ul className="font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                                <li>
                                    <a href="/" className="block font-sans text-white rounded  dark:text-white text-sm">
                                        Home
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </header>
            <main className="flex-grow overflow-y-auto">
                {children}
            </main>
            <footer className="h-10">
                <div className="text-center text-gray-500 text-sm">
                    © {new Date().getFullYear()} <strong>Fluent Investor</strong>.
                    <br/>
                    Licensed under the <a href="https://opensource.org/licenses/MIT" target="_blank"
                                          rel="noopener noreferrer" className="text-blue-500 hover:underline">MIT
                    License</a>.
                </div>
            </footer>
        </div>
    );
}
