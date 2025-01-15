import {z} from 'zod';

export function createLoginValidationSchema(t: (key: string) => string)
{
    return z.object({
        identifier: z.string().min(3, t("forms.login.validation.identifier_too_short")),
        password: z.string().nonempty(t("forms.login.validation.password_empty"))
    });
}
