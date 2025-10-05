
export default function Header() {
    return (
        <header className="text-white bg-black flex justify-between p-6">

            <div className="left text-3xl font-bold">
                LLM EVALUATOR
            </div>

            <div className="right flex text-xl space-x-4">
                <div>
                    Home
                </div>
                <div>
                    Manage Prompts
                </div>
            </div>
            
        </header>
    )
}