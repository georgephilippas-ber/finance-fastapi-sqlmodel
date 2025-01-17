import axios from "axios";
import {FASTAPI_SERVER_BASE_URL} from "@/configuration/configuration";

export const fastApiClient = axios.create({
    baseURL: FASTAPI_SERVER_BASE_URL,
    timeout: 5_000,
    withCredentials: true,
});

export function setAuthorizationHeader(token: string)
{
    fastApiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

export function clearAuthorizationHeader(client: any)
{
    delete fastApiClient.defaults.headers.common['Authorization'];
}
