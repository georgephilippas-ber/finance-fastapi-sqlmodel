import CompanyDetails from "@/components/client/company/company-details";
import {BackButton} from "@/components/server/navigation/back-button";
import {SingleSeriesChart} from "@/components/highcharts/highcharts";
import {retrieveFundamentalTimeSeries} from "@/actions/financial/company";
import {adapt} from "@/schema/fundamental-time-series";

export default async function ({searchParams}: { searchParams?: any })
{
    const company_id = parseInt((await searchParams).company_id || "");

    return (
        <div className={"p-2"}>
            <div className={"mb-2"}>
                <BackButton href={"/members/company/search"}/>
            </div>
            {!isNaN(company_id) ? <CompanyDetails company_id={parseInt((await searchParams).company_id || "")}/> : null}

            {!isNaN(company_id) ?
                <>
                    <div className={"text-xl font-semibold text-center p-4 mb-2"}>
                        Time Series
                    </div>
                    <div
                        className={"border border-white p-2 my-2 rounded-lg grid sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3"}>
                        {
                            adapt((await retrieveFundamentalTimeSeries(company_id)) as any).map((value, index) =>
                            {
                                return (
                                    <SingleSeriesChart key={index} index={index} chart_data={value.chart_data}
                                                       tooltip_point_format={value.tooltip_point_format}/>
                                )
                            })
                        }
                    </div>
                </> : null}
        </div>
    );
}
