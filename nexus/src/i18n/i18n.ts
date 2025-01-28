import i18n from 'i18next';
import {initReactI18next} from 'react-i18next';

import en_authentication from '../../public/locales/en/authentication.json';
import en_company_search from '../../public/locales/en/company/company-search.json'
import en_company_details from '../../public/locales/en/company/company-details.json'
import en_locales from "../../public/locales/en/locales.json"

import de_authentication from '../../public/locales/de/authentication.json';
import de_company_search from '../../public/locales/de/company/company-search.json'
import de_company_details from '../../public/locales/de/company/company-details.json'
import de_locales from "../../public/locales/de/locales.json"

import fr_authentication from '../../public/locales/fr/authentication.json';
import fr_company_search from '../../public/locales/fr/company/company-search.json'
import fr_company_details from '../../public/locales/fr/company/company-details.json'
import fr_locales from "../../public/locales/fr/locales.json"


i18n.use(initReactI18next).init({
    lng: 'en',
    fallbackLng: 'en',
    ns: ['authentication', "locales", 'company_search', 'company_details'],
    defaultNS: 'authentication',
    resources:
        {
            en:
                {
                    authentication: en_authentication,
                    company_search: en_company_search,
                    company_details: en_company_details,
                    locales: en_locales,
                },
            de:
                {
                    authentication: de_authentication,
                    company_search: de_company_search,
                    company_details: de_company_details,
                    locales: de_locales,
                },
            fr:
                {
                    authentication: fr_authentication,
                    company_search: fr_company_search,
                    company_details: fr_company_details,
                    locales: fr_locales,
                }
        }
});

export default i18n;
