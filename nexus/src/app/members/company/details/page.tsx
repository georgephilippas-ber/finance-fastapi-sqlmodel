import CompanyDetails from "@/components/client/company/company-details";
import {BackButton} from "@/components/server/navigation/back-button";
import {SingleSeriesChart} from "@/components/highcharts/highcharts";
import {DateTime, Duration} from "luxon";
import {faker} from "@faker-js/faker";

export default async function ({searchParams}: { searchParams?: any })
{
    return (
        <div className={"p-2"}>
            <div className={"mb-2"}>
                <BackButton href={"/members/company/search"}/>
            </div>
            {(await searchParams)?.company_id && !isNaN(parseInt((await searchParams).company_id || "")) ?
                <CompanyDetails company_id={parseInt((await searchParams).company_id || "")}/> : null}

               <SingleSeriesChart chart_data={
                {
                    title: "Return on Investment",
                    subtitle: "Net Income / Assets",
                    dependent_axis_title: "return on investment: %",
                    series_name: "ROI",
                    data: Array(100).fill(0).map((_value, index) =>
                    {
                        return {
                            date: DateTime.now().plus(Duration.fromObject({years: index})).toISODate(),
                            value: faker.number.float({min: 23, max: 100})
                        }
                    })
                }
            }/>
        </div>
    );
}
