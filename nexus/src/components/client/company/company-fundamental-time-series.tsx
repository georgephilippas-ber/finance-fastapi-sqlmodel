'use client'

import {adapt} from "@/schema/fundamental-time-series";
import {retrieveFundamentalTimeSeries} from "@/actions/financial/company";
import {SingleSeriesChart} from "@/components/highcharts/highcharts";
import {useEffect, useState} from "react";
import {useTranslation} from "react-i18next";

export function CompanyFundamentalTimeSeries({company_id}: { company_id: number })
{
    const {t} = useTranslation("company_details_fundamental_time_series");

    const [fundamentalTimeSeries, setFundamentalTimeSeries] = useState<any[] | undefined>(undefined);

    useEffect(() =>
    {
        retrieveFundamentalTimeSeries(company_id).then(value =>
        {
            if (value) setFundamentalTimeSeries(adapt(value, t));
        });
    }, []);

    return (<>
            <div className={"text-xl font-semibold text-center p-4 mb-2"}>
                {t("user_interface.title")}
            </div>
            {fundamentalTimeSeries ?
                <div
                    className={"border border-white p-2 my-2 rounded-lg grid sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3"}>
                    {
                        fundamentalTimeSeries.map((value, index) =>
                        {
                            return (
                                <SingleSeriesChart key={index} index={index} chart_data={value.chart_data}
                                                   tooltip_point_format={value.tooltip_point_format}/>
                            )
                        })
                    }
                </div> : null}
        </>
    );
}
