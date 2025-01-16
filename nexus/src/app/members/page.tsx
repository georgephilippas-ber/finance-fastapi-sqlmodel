export default function ()
{
    return (
        <div>
            {Array(100).fill(0).map((_, i) => <p key={i}>Hello World</p>)}
        </div>
    )
}