import {Dropdown} from "flowbite-react";
import {useState} from "react";

export type metric_direction_type = 'DESC' | 'ASC';

export type metric_type =
    | 'market_capitalization'
    | 'return_on_assets'
    | 'operating_profit_margin';

type metric_display_type = {
    [key in metric_type]: string
}

const metrics: metric_display_type = {
    'market_capitalization': 'market capitalization',
    'return_on_assets': 'return on assets',
    'operating_profit_margin': 'operating profit margin'
};

export function MetricOptions({onSelect}: { onSelect?: (metric: metric_type) => void })
{
    const [selection, setSelection] = useState<metric_type>("market_capitalization");

    return (
        <Dropdown size={"xs"} color={"gray"} label={metrics[selection].toUpperCase()} dismissOnClick={true}>
            {Object.entries(metrics).map(([key, value]) => <Dropdown.Item onClick={() =>
            {
                setSelection(key as metric_type);

                onSelect?.(key as metric_type);
            }} className={"text-xs"}
                                                                          key={key}>{value.toUpperCase()}</Dropdown.Item>)}
        </Dropdown>
    );
}

export type group_type = 'GICSIndustry' | 'GICSSector' | 'country';

export type criterion_type = {
    metric: metric_type;
    metric_direction: metric_direction_type;
    groups: Array<[group_type | null, number]>;
};

type group_display_type = {
    [key in group_type]: string
}

const groups: group_display_type = {
    'GICSIndustry': 'industry',
    'GICSSector': 'sector',
    'country': 'country'
};

export function GroupOptions({onSelect}: { onSelect?: (group: group_type) => void })
{
    const [selection, setSelection] = useState<group_type>("GICSIndustry");

    return (
        <Dropdown size={"xs"} color={"gray"} label={groups[selection].toUpperCase()} dismissOnClick={true}>
            {Object.entries(groups).map(([key, value]) => <Dropdown.Item onClick={() =>
            {
                setSelection(key as group_type);

                onSelect?.(key as group_type);
            }} className={"text-xs"}
                                                                         key={key}>{value.toUpperCase()}</Dropdown.Item>)}
        </Dropdown>
    );
}
