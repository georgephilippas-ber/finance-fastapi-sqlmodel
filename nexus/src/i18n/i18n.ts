import i18n from 'i18next';
import {initReactI18next} from 'react-i18next';

import en_authentication from '../../public/locales/en/authentication.json';
import en_company_search from '../../public/locales/en/company/company-search.json'

i18n.use(initReactI18next).init({
    lng: 'en',
    fallbackLng: 'en',
    ns: ['authentication', 'company_search'],
    defaultNS: 'authentication',
    resources: {
        en: {
            authentication: en_authentication,
            company_search: en_company_search
        }
    }
});

export default i18n;
