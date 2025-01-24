import {end_of_day_change_overview_type} from "@/schema/schema";

export function EndOfDayChangeOverview({end_of_day_change_overview, isFake = false}: {
    end_of_day_change_overview: end_of_day_change_overview_type
    isFake?: boolean;
})
{
    return (
        <div>
            {JSON.stringify(end_of_day_change_overview, null, 2)}
            {isFake && <div>fake data</div>}
        </div>
    )
}
