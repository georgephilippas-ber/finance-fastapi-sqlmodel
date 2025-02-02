// import {useState} from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css';

// function App() {
//   const [count, setCount] = useState(0)
//
//   return (
//     <>
//       <div>
//         <a href="https://vite.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.tsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }
import Highcharts from 'highcharts';
import {DateTime, Duration} from "luxon";
import {useEffect} from "react";

import {faker} from "@faker-js/faker";



function App()
{
    return (
        <div style={{
            margin: "0 auto",
            maxWidth: "80svw",
            border: "1px solid white",
            borderRadius: "1em",
            padding: "1em"
        }}>
            <SingleSeriesChart chart_data={
                {
                    title: "Return on Investment",
                    subtitle: "Net Income / Assets",
                    dependent_axis_title: "return on investment: %",
                    series_name: "ROI",
                    data: Array(100).fill(0).map((_value, index) =>
                    {
                        return {
                            date: DateTime.now().plus(Duration.fromObject({years: index})).toISODate(),
                            value: faker.number.float({min: 23, max: 100})
                        }
                    })
                }
            }/>
        </div>
    );
}

export default App
