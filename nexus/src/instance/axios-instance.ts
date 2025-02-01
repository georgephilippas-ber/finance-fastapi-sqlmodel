import axios from "axios";
import {FASTAPI_SERVER_BASE_URL} from "@/configuration/configuration";

export const fastApiClient = axios.create({
    baseURL: FASTAPI_SERVER_BASE_URL,
    timeout: 5_000,
    withCredentials: true,
});
