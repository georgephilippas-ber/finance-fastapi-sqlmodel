import {Accordion} from "flowbite-react";
import {company_overview_type} from "@/schema/schema";

export default function CompanyOverview({company_overview}: { company_overview: company_overview_type })
{
    return (
        <div>
            <Accordion>
                <Accordion.Title>
                    {company_overview.company_name}
                </Accordion.Title>
            </Accordion>
        </div>
    );
}
