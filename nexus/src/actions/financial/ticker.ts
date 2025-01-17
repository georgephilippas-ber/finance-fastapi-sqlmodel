import {company_overview_type} from "@/schema/schema";
import {fastApiClient} from "@/instance/axios-instance";

// export async function getEndOfDayChangeOverview(ticker_id: number): Promise<company_overview_type[]>
// {
//     try
//     {
//         const response_ = await fastApiClient.get<company_overview_type[]>("/company/overview", {
//             params:
//                 {
//                     ids: ids.join(','),
//                 },
//         });
//
//         return response_.data;
//     }
//     catch (err)
//     {
//         return [];
//     }
// }
