import {useTranslation} from "react-i18next";

import i18n from "../../i18n/i18n";
import {MouseEventHandler, useEffect, useMemo, useState} from "react";
import {createLoginValidationSchema} from "@/core/validation/login";
import {ZodError} from "zod";

console.log(i18n);

export function Login()
{
    const [identifier, setIdentifier] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const {t} = useTranslation('authentication');

    const [errors, setErrors] = useState<{ identifier?: string; password?: string }>({});

    const validationSchema = useMemo(() => createLoginValidationSchema(t), [t]);

    useEffect(() =>
    {
        setErrors(prevState =>
        {
            return {...prevState, identifier: undefined};
        });
    }, [identifier])

    useEffect(() =>
    {
        setErrors(prevState =>
        {
            return {...prevState, password: undefined};
        });
    }, [password])

    const handler: MouseEventHandler<HTMLButtonElement> = (event) =>
    {
        try
        {
            validationSchema.parse({identifier, password});
        }
        catch (e)
        {
            const error = e as ZodError;

            for (const fieldError of error.errors)
            {
                if ((fieldError.path.length === 1) && (fieldError.path[0] === "identifier"))
                    setErrors(prevState => ({...prevState, identifier: fieldError.message}));

                if ((fieldError.path.length === 1) && (fieldError.path[0] === "password"))
                    setErrors(prevState => ({...prevState, password: fieldError.message}));

                console.log(errors);
            }
        }
    }

    return (
        <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <div
                className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1 className="mx-auto w-fit text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                        {t("forms.login.title")}
                    </h1>
                    <div className="space-y-4 md:space-y-6 flex flex-col items-center w-full">
                        <div className={"w-full"}>
                            {errors.identifier ?
                                <p className={"w-full text-xs text-red-500 mb-1"}>{errors.identifier}</p> : null}
                            <input value={identifier} onChange={event => setIdentifier(event.target.value)}
                                   id={"identifier"} name={"identifier"} autoComplete={"username"} type="text"
                                   className="input w-full"
                                   placeholder={t("forms.login.placeholder.identifier")} required/>
                        </div>

                        <div className={"w-full"}>
                            {errors.password ?
                                <p className={"w-full text-xs text-red-500 mb-1"}>{errors.password}</p> : null}
                            <input value={password} onChange={event => setPassword(event.target.value)} id={"password"}
                                   name={"password"} autoComplete={"new-password"} type="password"
                                   placeholder={t("forms.login.placeholder.password")} className="input w-full"
                                   required/>
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
                                        {t("forms.login.remember_me")}
                                    </label>
                                </div>
                            </div>
                            <a href="#"
                               className="hidden text-sm font-medium text-primary-600 hover:underline dark:text-primary-500 mt-4">Forgot
                                password?</a>
                        </div>
                        <button onClick={handler} className={"btn btn-primary w-fit mx-auto"}>Sign in</button>
                        <div className="text-sm font-light text-gray-500 dark:text-gray-400">
                            <span className={"mr-1"}>{t("forms.login.create_account_prompt")}</span>
                            <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                                {t("forms.login.create_account_sign_up_link")}
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
