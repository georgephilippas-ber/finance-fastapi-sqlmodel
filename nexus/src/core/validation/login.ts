import {z} from 'zod';

function getLoginValidationSchema(t: (key: string) => string)
{
    const loginSchema = z.object({
        username: z.string().min(3, t("forms.login.validation.identifier_too_short")),
    });
}
