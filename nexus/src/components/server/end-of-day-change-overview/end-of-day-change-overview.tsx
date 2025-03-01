import {end_of_day_change_overview_type} from "@/schema/schema";
import {DateTime} from "luxon";
import {fake_endOfDayChangeOverview} from "@/core/fake/end-of-day-change-overview";

function date(date_string: string | undefined | null, fake: boolean)
{
    if (fake)
    {
        return "fake data".toUpperCase();
    }
    else
    {
        if (date_string)
        {
            return ["latest update", DateTime.fromISO(date_string).toLocaleString(DateTime.DATE_SHORT)].join(": ");
        }
        else
            return "latest update: unknown";
    }
}

function assetReturn(end: number | undefined | null, start: number | undefined | null): number
{
    if (end && start)
        return (end - start) / start
    else
        return NaN;
}

function getClass(value: number | undefined | null)
{
    if (value === undefined || value === null)
        return "text-gray-400";
    else
    {
        if (value > 0)
            return "text-green-400";
        else
            return "text-red-400";
    }
}

export function EndOfDayChangeOverview({endOfDayChangeOverview, currencySymbol, className}: {
    endOfDayChangeOverview?: end_of_day_change_overview_type;
    currencySymbol?: string;
    className?: string;
})
{
    const fake = !endOfDayChangeOverview;

    const overview_ = endOfDayChangeOverview || fake_endOfDayChangeOverview();

    const month_to_date_ = assetReturn(overview_.latest_adjusted, overview_.beginning_of_month_adjusted);
    const year_to_date_ = assetReturn(overview_.latest_adjusted, overview_.beginning_of_year_adjusted);

    return (
        <div className={["w-fit p-2 border-white border rounded-lg", className].join(" ").trim()}>
            <div className={"w-fit flex flex-row gap-3"}>
                <div className={"grid grid-cols-[auto_4em] gap-2 w-fit text-xl"}>
                    <div>
                        {currencySymbol}
                    </div>
                    <div className={"overflow-x-hidden text-nowrap"}>
                        {overview_.latest?.toFixed(2)}
                    </div>
                </div>
                <div
                    className={["grid grid-cols-[auto_4em] gap-1 w-fit text-lg", getClass(month_to_date_)].join(" ")}>
                    <div className={"font-semibold text-sm"}>
                        MTD
                    </div>
                    <div className={"overflow-x-hidden text-nowrap"}>
                        {(month_to_date_ * 1.e2).toFixed(2)} %
                    </div>
                </div>
                <div
                    className={["grid grid-cols-[auto_4em] gap-2 w-fit text-lg", getClass(year_to_date_)].join(" ")}>
                    <div className={"font-semibold text-sm"}>
                        YTD
                    </div>
                    <div className={"overflow-x-hidden text-nowrap"}>
                        {(year_to_date_ * 1.e2).toFixed(2)} %
                    </div>
                </div>
            </div>
            <div className={"text-xs mt-1"}>
                {date(overview_.latest_date, fake)}
            </div>
        </div>);
}
