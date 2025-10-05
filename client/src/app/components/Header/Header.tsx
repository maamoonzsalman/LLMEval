"use client"

import { useRouter } from "next/navigation";

export default function Header() {
    const router = useRouter();

    return (
        <header className="text-white bg-black flex justify-between p-6">

            <div className="left text-3xl font-bold cursor-pointer" onClick={() => router.push("/")}>
                LLM EVALUATOR
            </div>

            <div className="right flex text-xl space-x-4">
                <div onClick={() => router.push("/")} className="hover:underline cursor-pointer">
                    Home
                </div>
                <div onClick={() => router.push("/prompts")} className="hover:underline cursor-pointer">
                    Manage Prompts
                </div>
            </div>
            
        </header>
    )
}