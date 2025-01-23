import {NextRequest, NextResponse} from "next/server";
import {JSON_WEB_TOKEN_SECRET_KEY_ENCODED, PROTECTED_ROUTES} from "@/configuration/configuration";

import {jwtVerify} from 'jose'

export async function middleware(req: NextRequest)
{
    const header_ = req.headers.get("Authorization")?.split(" ")?.[1] || req.cookies.get("Authorization")?.value;
    const request_url_ = req.nextUrl.pathname;

    if (PROTECTED_ROUTES.some(value => request_url_.startsWith(value)))
    {
        if (!header_)
            return NextResponse.redirect("http://localhost:3000/authentication/login");
        else
        {
            try
            {
                await jwtVerify(header_, JSON_WEB_TOKEN_SECRET_KEY_ENCODED)
            }
            catch (e)
            {

            }
        }
    }

    return NextResponse.next();
}

export const config = {
    matcher: PROTECTED_ROUTES.map(value => value + '/:path*'),
};
