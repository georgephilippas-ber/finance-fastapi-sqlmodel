import {end_of_day_change_overview_type} from "@/schema/schema";

export function EndOfDayChangeOverview({endOfDayChangeOverview, currencySymbol, isFake = false}: {
    endOfDayChangeOverview: end_of_day_change_overview_type;
    currencySymbol: string;
    isFake?: boolean;
})
{
    return (
        <div>
            {currencySymbol}
            {JSON.stringify(endOfDayChangeOverview, null, 2)}
            {isFake && <div>fake data</div>}
        </div>
    )
}
