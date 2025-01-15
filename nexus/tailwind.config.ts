import type {Config} from "tailwindcss";

const flowbite = require("flowbite-react/tailwind");

export default {
    darkMode: "class",
    content: [
        "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
        "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
        "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
        flowbite.content(),
    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ["Lato", "sans-serif"],
            },
            colors: {
                background: "var(--background)",
                foreground: "var(--foreground)"
            },
        },
    },
    plugins: [
        require("daisyui"),
        flowbite.plugin(),
    ],
} satisfies Config;
