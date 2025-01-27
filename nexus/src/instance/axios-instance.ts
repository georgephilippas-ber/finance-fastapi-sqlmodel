import axios, {AxiosError, HttpStatusCode} from "axios";
import {FASTAPI_SERVER_BASE_URL} from "@/configuration/configuration";

export const fastApiClient = axios.create({
    baseURL: FASTAPI_SERVER_BASE_URL,
    timeout: 5_000,
    withCredentials: true,
});

fastApiClient.interceptors.response.use(
    (response) =>
    {
        return response;
    },
    (error: AxiosError) =>
    {
        if (error.response?.status === HttpStatusCode.Unauthorized)
            window.location.href = '/authentication/login';

        return Promise.reject(error);
    }
);

export function setAuthorizationHeader(token: string)
{
    fastApiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

export function clearAuthorizationHeader(client: any)
{
    delete fastApiClient.defaults.headers.common['Authorization'];
}
