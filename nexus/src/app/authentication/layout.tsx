export default function ({children}: { children: React.ReactNode })
{
    return (
        <div className={"min-h-screen flex flex-col items-center justify-center px-6 mx-auto md:h-screen lg:py-0 font-sans"}>
            {children}
        </div>
    )
}
