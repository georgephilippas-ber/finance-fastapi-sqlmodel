'use client'

import {MouseEventHandler, useEffect, useMemo, useState} from "react";
import {createLoginValidationSchema} from "@/core/validation/login";
import {ZodError} from "zod";
import {login} from "@/actions/authentication/login";
import {useRouter} from "next/navigation";
import {Modal} from "flowbite-react";

import "../../../i18n/i18n";
import {useTranslation} from "react-i18next";
import {FASTAPI_SERVER_BASE_URL, IN_DOCKER} from "@/configuration/configuration";

export function LoginServerErrorModal({open, onClose}: { open: boolean, onClose?: () => void })
{
    const {t} = useTranslation('authentication');

    return (
        <Modal show={open} onClose={onClose}>
            <Modal.Header>
                <div>
                    {t("forms.login.validation.modal.header")}
                </div>
            </Modal.Header>
            <Modal.Body>
                <p>
                    {t("forms.login.validation.modal.content")}
                </p>
            </Modal.Body>
            <Modal.Footer>
                <button onClick={onClose} className="btn btn-primary">Close</button>
            </Modal.Footer>
        </Modal>
    );
}

export function Login({success_url}: { success_url: string })
{
    const [identifier, setIdentifier] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const {t} = useTranslation('authentication');

    const [errors, setErrors] = useState<{ identifier?: string; password?: string }>({});

    const validationSchema = useMemo(() => createLoginValidationSchema(t), [t]);

    const router = useRouter();

    const [loginServerErrorModalOpen, setLoginServerErrorModalOpen] = useState<boolean>(false);

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

    const handler: MouseEventHandler<HTMLButtonElement> = async (event) =>
    {
        try
        {
            validationSchema.parse({identifier, password});

            const success_ = await login(identifier, password);
            console.log(IN_DOCKER, FASTAPI_SERVER_BASE_URL);

            if (success_)
                router.push(success_url);
            else
            {
                setLoginServerErrorModalOpen(true);
            }
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
        <>
            <div
                className="w-full bg-white rounded-lg shadow dark:border dark:bg-gray-800 dark:border-gray-700 p-4">
                <div className="p-6 space-y-4">
                    <h1 className="mx-auto w-fit text-xl font-bold leading-tight tracking-tight text-gray-900 dark:text-white">
                        {t("forms.login.title")}
                    </h1>
                    <div className="space-y-4 flex flex-col items-center w-full">
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
                            <input value={password} onChange={event => setPassword(event.target.value)}
                                   id={"password"}
                                   name={"password"} autoComplete={"new-password"} type="password"
                                   placeholder={t("forms.login.placeholder.password")} className="input w-full"
                                   required/>
                        </div>
                        <button onClick={handler} className={"btn btn-primary w-fit mx-auto"}>Sign in</button>
                        <div className="text-sm font-light text-gray-500 dark:text-gray-400">
                            <span className={"mr-1"}>{t("forms.login.create_account_prompt")}</span>
                            <a href="#"
                               className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                                {t("forms.login.create_account_sign_up_link")}
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <LoginServerErrorModal onClose={() => setLoginServerErrorModalOpen(false)}
                                   open={loginServerErrorModalOpen}/>
        </>
    );
}
