import {z} from 'zod';

function getLoginValidationSchema(t: (key: string) => string)
{

}

const loginSchema = z.object({
    username: z.string().min(3, "username or e-mail is too short"),
});