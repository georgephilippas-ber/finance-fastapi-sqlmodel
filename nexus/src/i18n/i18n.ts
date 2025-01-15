import i18n from 'i18next';
import {initReactI18next} from 'react-i18next';

import en_authentication from '../../public/locales/en/authentication.json';

i18n.use(initReactI18next).init({
    lng: 'en',
    fallbackLng: 'en',
    ns: ['authentication'],
    defaultNS: 'authentication',
    resources: {
        en: {
            authentication: en_authentication
        }
    }
});

export default i18n;
