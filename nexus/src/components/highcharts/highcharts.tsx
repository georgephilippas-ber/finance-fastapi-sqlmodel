import {useEffect} from "react";
import {DateTime} from "luxon";

import Highcharts from "highcharts"

type entry_type =
    {
        date: string;
        value: number;
    }

export type chart_data_type =
    {
        title: string;
        subtitle?: string;
        series_name: string;
        dependent_axis_title: string;
        data: entry_type[];
    }


export function SingleSeriesChart({chart_data, tooltip_point_format = '{series.name}: <b>{point.y:.2f}%</b>'}: {
    chart_data: chart_data_type;
    tooltip_point_format?: string;
})
{
    const element_id = crypto.randomUUID().replace(/-/g, '');

    useEffect(() =>
    {
        Highcharts.chart(element_id,
            {
                chart: {
                    zooming: {
                        type: 'x'
                    },
                    backgroundColor: 'rgba(100, 100, 100, 0.0)',
                },
                title: {
                    text: chart_data.title,
                    style:
                        {
                            color: '#fff',
                        }
                },
                subtitle: {
                    text: chart_data.subtitle,
                    style:
                        {
                            color: '#fff',
                        }
                },
                xAxis: {
                    type: 'datetime',
                    tickInterval: 365 * 24 * 3600 * 1000,
                    labels:
                        {
                            style:
                                {
                                    fontSize: '0.75em',
                                    color: '#fff'
                                },
                            formatter: function ()
                            {
                                return DateTime.fromMillis(this.value as number).toFormat('MM/yyyy');
                            }
                        }
                },
                yAxis: {
                    gridLineWidth: 0,
                    title: {
                        text: chart_data.dependent_axis_title,
                        style:
                            {
                                fontWeight: '600',
                                fontSize: "1.05em",
                                color: '#fff'
                            }
                    },
                    labels:
                        {
                            style:
                                {
                                    color: '#fff'
                                }
                        }

                },
                legend: {
                    enabled: false
                },
                tooltip:
                    {
                        pointFormat: tooltip_point_format,
                    },
                plotOptions: {
                    area: {
                        marker: {
                            radius: 2
                        },
                        lineWidth: 1,
                        color: {
                            linearGradient: {
                                x1: 0,
                                y1: 0,
                                x2: 0,
                                y2: 1
                            },
                            stops: [
                                [0, 'rgb(130, 120, 190)'],
                                [0.7, 'rgb(90, 100, 160)']
                            ]
                        },
                        states: {
                            hover: {
                                lineWidth: 1
                            }
                        },
                        threshold: null
                    }
                },
                series: [{
                    type: 'area',
                    name: chart_data.series_name,
                    data: chart_data.data.map(value => [DateTime.fromISO(value.date).toMillis(), value.value]),
                }]
            });
    }, [])

    return (
        <div style={{width: "100%"}} id={element_id}></div>
    );
}
