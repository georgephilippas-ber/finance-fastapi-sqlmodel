import {NextResponse} from 'next/server';
import {IN_DOCKER} from "@/configuration/configuration";

export async function GET()
{
    return NextResponse.json(
        {
            message: 'Hello, World!',
            docker: IN_DOCKER
        }
    );
}
