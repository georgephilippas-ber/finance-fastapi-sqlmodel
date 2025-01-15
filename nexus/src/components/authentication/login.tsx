export function Login()
{
    return (
        <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <div
                className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1 className="mx-auto w-fit text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                        Sign in to your account
                    </h1>
                    <div className="space-y-4 md:space-y-6 flex flex-col items-center w-full">
                        <div className={"w-full"}>
                            {/*<label htmlFor="email"*/}
                            {/*       className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your*/}
                            {/*    email</label>*/}
                            <input id={"identifier"} name={"identifier"} autoComplete={"username"} type="text"
                                   className="input w-full"
                                   placeholder="username or e-mail" required/>
                        </div>
                        <div className={"w-full"}>
                            {/*<label htmlFor="password"*/}
                            {/*       className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>*/}
                            <input id={"password"} name={"password"} autoComplete={"new-password"} type="password"
                                   placeholder="password" className="input w-full" required/>
                        </div>
                        <div className="flex justify-between flex-col items-start gap-3 w-full">
                            <div className="flex items-start">
                                <div className="flex items-center h-5">
                                    <input id="remember" aria-describedby="remember" type="checkbox"
                                           className="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
                                           required/>
                                </div>
                                <div className="ml-3 text-sm">
                                    <label htmlFor="remember" className="text-gray-500 dark:text-gray-300">
                                        Remember me
                                    </label>
                                </div>
                            </div>
                            <a href="#"
                               className="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500 mt-4 hidden">Forgot
                                password?</a>
                        </div>
                        <button className={"btn btn-primary w-fit mx-auto"}>Sign in</button>
                        <p className="text-sm font-light text-gray-500 dark:text-gray-400">
                            Don’t have an account yet? <a href="#"
                                                          className="font-medium text-primary-600 hover:underline dark:text-primary-500">Sign
                            up</a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
}
