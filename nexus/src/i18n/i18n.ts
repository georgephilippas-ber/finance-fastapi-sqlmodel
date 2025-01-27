import i18n from 'i18next';
import {initReactI18next} from 'react-i18next';

import en_authentication from '../../public/locales/en/authentication.json';
import en_company_search from '../../public/locales/en/company/company-search.json'
import en_company_details from '../../public/locales/en/company/company-details.json'

i18n.use(initReactI18next).init({
    lng: 'en',
    fallbackLng: 'en',
    ns: ['authentication', 'company_search', 'company_details'],
    defaultNS: 'authentication',
    resources: {
        en: {
            authentication: en_authentication,
            company_search: en_company_search,
            company_details: en_company_details,
        }
    }
});

export default i18n;
