'use client'

import {Dropdown} from "flowbite-react";

import {SUPPORTED_LOCALES} from "@/configuration/configuration";

import i18n from "../../../i18n/i18n";
import {useTranslation} from "react-i18next";
import {useState} from "react";

function localeToFlag(locale: string)
{
    return locale != 'en' ? locale.toUpperCase() : 'GB';
}

export function LanguageSelector()
{
    const {t} = useTranslation('locales');

    const [selection, setSelection] = useState<string>("en");

    return (
        <Dropdown label={t(selection).toUpperCase()} size={"xs"} dismissOnClick={true}>
            {SUPPORTED_LOCALES.map(value =>
            {
                return (
                    <Dropdown.Item onClick={() =>
                    {
                        i18n.changeLanguage(value).then(value1 =>
                        {
                            console.log(value1);
                        });

                        setSelection(value)
                    }} key={value}>
                        <div className={"flex gap-2 items-center"}>
                            <img className={"w-5"} src={`https://flagsapi.com/${localeToFlag(value)}/flat/64.png`}
                                 alt={value.toUpperCase()}/>
                            <div>
                                {t(value).toUpperCase()}
                            </div>
                        </div>
                    </Dropdown.Item>)
            })}
        </Dropdown>
    );
}
