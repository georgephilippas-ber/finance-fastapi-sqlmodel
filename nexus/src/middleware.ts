import {NextRequest, NextResponse} from "next/server";
import {
    APPLICATION_HOME_URL,
    APPLICATION_PROTECTED_HOME_URL,
    JSON_WEB_TOKEN_SECRET_KEY_ENCODED,
    PROTECTED_ROUTES
} from "@/configuration/configuration";

import {jwtVerify} from 'jose'

export async function middleware(req: NextRequest)
{
    const header_ = req.headers.get("Authorization")?.split(" ")?.[1] || req.cookies.get("Authorization")?.value;
    const request_url_ = req.nextUrl.pathname;

    if (request_url_.includes("login"))
    {
        if (header_)
        {
            try
            {
                await jwtVerify(header_, JSON_WEB_TOKEN_SECRET_KEY_ENCODED);

                return NextResponse.redirect(APPLICATION_PROTECTED_HOME_URL);
            }
            catch (e)
            {
            }
        }
    }

    if (PROTECTED_ROUTES.some(value => request_url_.startsWith(value)))
    {
        if (!header_)
            return NextResponse.redirect("http://localhost:3000/authentication/login");
        else
        {
            try
            {
                await jwtVerify(header_, JSON_WEB_TOKEN_SECRET_KEY_ENCODED);
            }
            catch (e)
            {

            }
        }
    }

    const headers = new Headers(req.headers);

    headers.set("x-pathname", req.nextUrl.pathname);
    return NextResponse.next({
        headers
    });
}

export const config = {
    matcher: [...PROTECTED_ROUTES.map(value => value + '/:path*'), "/authentication/login"],
};
