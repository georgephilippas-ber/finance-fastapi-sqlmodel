import {NextResponse} from 'next/server';
import {FASTAPI_SERVER_BASE_URL, IN_DOCKER} from "@/configuration/configuration";

export async function GET()
{
    return NextResponse.json(
        {
            message: 'Hello, World!',
            docker: IN_DOCKER,
            backend: FASTAPI_SERVER_BASE_URL
        }
    );
}
