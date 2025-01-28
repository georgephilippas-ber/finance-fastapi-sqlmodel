'use client'

import {Dropdown} from "flowbite-react";
import {useTranslation} from "react-i18next";

export function LanguageSelector()
{
    const {t} = useTranslation('locales');

    return (
        <Dropdown label={"Language"}>
            <Dropdown.Item>
                s
            </Dropdown.Item>
        </Dropdown>
    );
}

