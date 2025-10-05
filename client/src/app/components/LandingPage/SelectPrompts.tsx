"use client"
import axios from "axios"
import { useState, useEffect } from "react"
import {
    Select, 
    SelectContent,
    SelectItem, 
    SelectTrigger,
    SelectValue
} from "@/components/ui/select"

type SystemPrompt = {
    id: number;
    title: string;
    body: string;
}

type TestPrompt = {
    id: number;
    body: string;
}

type LLMOutput = {
    latency_ms: number,
    model: string,
    text: string,
    usage: {
        input_tokens: number,
        output_tokens: number,
        total_tokens: number,
    }   
}

type ScoreMetric = {
  metric: string;
  score_0_to_1: number;
  score_1_to_5: number;
  passed: boolean;
  reason: string;
};

type LLMScore = {
  adherence: ScoreMetric;
  clarity: ScoreMetric;
  completeness: ScoreMetric;
  reasoning: ScoreMetric;
  relevancy: ScoreMetric;
};

export type ModelData = {
    output: {
        claude_output: LLMOutput,
        gemini_output: LLMOutput,
        openai_output: LLMOutput,
    },
    scores: {
        claude_score: LLMScore,
        gemini_score: LLMScore,
        openai_score: LLMScore,
    },
}

export default function SelectPrompts({
    setModelData, setLoading 
}:  { 
    setModelData: React.Dispatch<React.SetStateAction<ModelData | null>>; 
    setLoading: React.Dispatch<React.SetStateAction<boolean>>;
}) {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;

    const [systemPrompts, setSystemPrompts] = useState<SystemPrompt[]>([]);
    const [selectedSystemPrompt, setSelectedSystemPrompt] = useState("");

    const [testPrompts, setTestPrompts] = useState<TestPrompt[]>([]);
    const [selectedTestPrompt, setSelectedTestPrompt] = useState("");


    const isTestPromptDisabled = selectedSystemPrompt === "";
    const isEvaluateDisabled = selectedTestPrompt === "";


    useEffect(() => {
        async function fetchSystemPrompts() {
            try {
                const data = await axios.get(`${apiUrl}/system_prompt/`)
                setSystemPrompts(data.data)
                console.log(data.data)
            } catch (err) {
                console.error("Error fetching system prompts: ", err);
            }
        }

        fetchSystemPrompts();
    }, [apiUrl]);

    useEffect(() => {
        if (!selectedSystemPrompt) return;
        async function fetchTestPrompts() {
            try {
                const data = await axios.get(`${apiUrl}/test_prompt/${selectedSystemPrompt}`)
                setTestPrompts(data.data)
                console.log(data)
            } catch (err) {
                console.error("Error fetching test prompts: ", err);
            }
        }

        fetchTestPrompts();
    }, [apiUrl, selectedSystemPrompt])

    async function handleEvaluateModels() {
        const system = systemPrompts.find(
        (p) => p.id.toString() === selectedSystemPrompt
        );
        const test = testPrompts.find(
        (p) => p.id.toString() === selectedTestPrompt
        );

        console.log("Selected System Prompt:", system);
        console.log("Selected Test Prompt:", test);

        try {
            setLoading(true);
            const data = await axios.post(`${apiUrl}/experiment/run`, {
                system_prompt: system?.body,
                test_prompt: test?.body,
            })
            console.log(data)
            setModelData(data.data)
            setLoading(false)
        } catch(err) {
            console.error("Error fetching model responses and experiment metrics: ", err);
        }
    }

    return (
        <div className="text-black w-fit border-solid border-2 p-10 flex flex-col space-y-6 rounded-lg">
            
            <div className="flex w-full space-x-6 p-2">
                
                <div className="system-prompt w-96">
                    <label className="font-semibold text-black">System Prompt</label>
                    <Select onValueChange={setSelectedSystemPrompt}>
                        <SelectTrigger className="w-full">
                            <SelectValue placeholder="Select a system prompt"/>
                        </SelectTrigger>
                        <SelectContent>
                            {systemPrompts.map((prompt) => (
                                <SelectItem key={prompt.id} value={prompt.id.toString()}>
                                    {prompt.title}
                                </SelectItem>
                            ))}
                        </SelectContent>
                    </Select>
                </div>
                
                <div className="test-prompt w-96">
                    <label className="font-semibold text-black">Test Prompt</label>
                    <Select onValueChange={setSelectedTestPrompt}>
                        <SelectTrigger className={`w-full ${isTestPromptDisabled ? "opacity-50 cursor-not-allowed" : ""}`}>
                            <SelectValue placeholder="Select a test prompt"/>
                        </SelectTrigger>
                        <SelectContent>
                            {testPrompts.map((prompt) => (
                                <SelectItem key={prompt.id} value={prompt.id.toString()}>
                                    {prompt.body}
                                </SelectItem>
                            ))}
                        </SelectContent>
                    </Select>
                </div>
                
            </div>

            <button onClick={handleEvaluateModels} className={`bg-black text-white p-3 font-bold text-lg rounded-2xl  ${isEvaluateDisabled ? "opacity-50 cursor-not-allowed": "hover:cursor-pointer"}`}>
                Evaluate Models
            </button>

        </div>
    )
}

