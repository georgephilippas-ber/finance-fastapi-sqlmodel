import {faker} from "@faker-js/faker";
import {end_of_day_change_overview_type} from "@/schema/schema";
import {DateTime} from "luxon";

export function fake_endOfDayChangeOverview(): end_of_day_change_overview_type
{
    return {
        beginning_of_month_adjusted: faker.number.float({min: 100., max: 110.0}),
        beginning_of_year_adjusted: faker.number.float({min: 100., max: 110.0}),
        latest_adjusted: faker.number.float({min: 100., max: 110.0}),
        latest: faker.number.float({min: 100., max: 110.0}),
        latest_date: DateTime.now().toISODate(),
    }
}
