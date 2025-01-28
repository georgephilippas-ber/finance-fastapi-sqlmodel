import {LanguageSelector} from "@/components/client/internationalization/language-selector";
import {BackButton} from "@/components/client/navigation/back-button";

export default function ()
{
    return (
        <div className={"min-h-screen"}>
            <div className={"text-2xl font-semibold text-center p-4 mb-4"}>
                Settings
            </div>
            <div className={"m-4"}>
                <BackButton/>
            </div>
            <div className={"m-4"}>
                <LanguageSelector/>
            </div>
        </div>
    )
}
