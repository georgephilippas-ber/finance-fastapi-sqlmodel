import {Dropdown, RangeSlider} from "flowbite-react";
import {useEffect, useState} from "react";
import {BsBuildingAdd} from "react-icons/bs";
import {event} from "next/dist/build/output/log";
import {AiOutlineUsergroupAdd} from "react-icons/ai";
import {IoIosAddCircleOutline} from "react-icons/io";

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

export function MetricOptions({onSelect, defaultValue, color = "gray"}: {
    defaultValue: metric_type;
    onSelect?: (metric: metric_type) => void;
    color?: string;
})
{
    const [selection, setSelection] = useState<metric_type>(defaultValue);

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

export function GroupOptions({onSelect, defaultValue, color = "gray", visible}: {
    defaultValue: group_type;
    onSelect?: (group: group_type) => void;
    color?: string;
    visible?: boolean;
})
{
    const [selection, setSelection] = useState<group_type>(defaultValue);

    return (
        <div className={visible ? "block" : "invisible"}>
            <Dropdown size={"xs"} color={color} label={groups[selection].toUpperCase()}
                      dismissOnClick={true}>
                {Object.entries(groups).map(([key, value]) => <Dropdown.Item onClick={() =>
                {
                    setSelection(key as group_type);

                    onSelect?.(key as group_type);
                }} className={"text-xs"}
                                                                             key={key}>{value.toUpperCase()}</Dropdown.Item>)}
            </Dropdown>
        </div>
    );
}

const metric_defaultValue: metric_type = 'market_capitalization';
const group_defaultValue: group_type = 'GICSIndustry';

export function Criterion({onChange, className}: {
    onChange?: (criterion: criterion_type) => void;
    className?: string
})
{
    const [sliderValue, setSliderValue] = useState<number>(10);
    const [currentGroup, setCurrentGroup] = useState<group_type>(group_defaultValue);
    const [groupEnabled, setGroupEnabled] = useState<boolean>(false);
    const [metric, setMetric] = useState<metric_type>(metric_defaultValue);

    const [metricDirection, setMetricDirection] = useState<metric_direction_type>('DESC');

    function onAdd()
    {
        const criterion: criterion_type = {
            metric,
            metric_direction: metricDirection,
            groups: [[groupEnabled ? currentGroup : null, sliderValue]]
        };

        onChange?.(criterion);

        console.table(criterion);
    }

    return (
        <div className={["flex items-center gap-4 w-fit", className || ""].join(" ").trim()}>
            <div className={"flex flex-row gap-3 items-center"}>
                <div className={"flex flex-col items-center border border-white rounded-lg p-2"}
                     onClick={v => setMetricDirection(metricDirection === "DESC" ? "ASC" : "DESC")}>
                    <div className={"w-full flex justify-between items-center text-xs"}>
                        <div className={"font-semibold"}>
                            LOW
                        </div>
                        <div className={"text-xs"}>
                            {sliderValue} %
                        </div>
                        <div className={"font-semibold"}>
                            HIGH
                        </div>
                    </div>
                    <RangeSlider dir={metricDirection == "DESC" ? "rtl" : "ltr"} value={sliderValue}
                                 onChange={event => setSliderValue(parseInt(event.target.value))}
                                 color={"red"}
                                 id="default-range"/>
                </div>
                <div className={"flex flex-col items-start gap-2 p-2"}>
                    <MetricOptions onSelect={metric1 => setMetric(metric1)} defaultValue={metric_defaultValue}/>
                    <div className={"w-full flex flex-row gap-2 justify-between items-center"}>
                        <input type="checkbox" className="toggle" value={groupEnabled ? "1" : "0"}
                               onChange={event => setGroupEnabled(event.target.checked)}/>
                        <GroupOptions onSelect={group => setCurrentGroup(group)} visible={groupEnabled}
                                      defaultValue={group_defaultValue}/>
                    </div>
                </div>
            </div>
            <IoIosAddCircleOutline onClick={event1 => onAdd()} className={"text-2xl cursor-pointer"}/>
        </div>
    )
}
