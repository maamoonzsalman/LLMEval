"use client";

import Header from "../components/Header/Header";
import { useState, useEffect } from "react";
import axios from "axios";
import type { SystemPrompt } from "../components/LandingPage/SelectPrompts";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

type SystemPromptOut = {
  title: string;
  body: string;
};

type TestPromptOut = {
  body: string;
};

type SystemAndTestPrompt = {
    id: number;
    title: string;
    body: string;
    test_prompts: TestPrompt[];
}

type TestPrompt = {
    id: number;
    body: string;
}

export default function ManagePrompts() {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL;
  const [systemPrompt, setSystemPrompt] = useState<SystemPromptOut>({
    title: "",
    body: "",
  });
  const [testPrompt, setTestPrompt] = useState<TestPromptOut>({ body: "" });

  const [systemPrompts, setSystemPrompts] = useState<SystemPrompt[]>([]);
  const [selectedSystemPrompt, setSelectedSystemPrompt] = useState("");

  const [systemAndTestPrompts, setSystemAndTestPrompts] = useState<SystemAndTestPrompt[]>([]);

  
  async function handleAddSystemPrompt() {
    try {
      const data = await axios.post(`${apiUrl}/system_prompt`, {
        title: systemPrompt.title,
        body: systemPrompt.body,
      });
      console.log("Created System Prompt:", data);
      setSystemPrompt({ title: "", body: "" }); // clear after submit
    } catch (err) {
      console.error("Error creating new system prompt: ", err);
    }
  }

  useEffect(() => {
    async function fetchSystemPrompts() {
      try {
        const data = await axios.get(`${apiUrl}/system_prompt/`);
        setSystemPrompts(data.data);
        console.log("Fetched system prompts:", data.data);
      } catch (err) {
        console.error("Error fetching system prompts: ", err);
      }
    }
    fetchSystemPrompts();
  }, [apiUrl]);

  useEffect(() => {
    async function fetchSystemAndTestPrompts() {
        try {
            const data = await axios.get(`${apiUrl}/system_prompt/tests`)
            console.log(data.data)
            setSystemAndTestPrompts(data.data)
        } catch (err) {
            console.error("Error fetching system prompts with test prompts: ", err);
        }
    }
    fetchSystemAndTestPrompts();
  }, [apiUrl])

  async function handleAddTestPrompt() {
    try {
      const data = await axios.post(
        `${apiUrl}/test_prompt/${selectedSystemPrompt}`,
        {
          body: testPrompt.body,
        }
      );
      console.log("Created Test Prompt:", data);
      setTestPrompt({ body: "" }); 
    } catch (err) {
      console.error("Error adding test prompt: ", err);
    }
  }

  async function handleDeleteSystemPrompt(id: number) {
    try {
        const data = await axios.delete(`${apiUrl}/system_prompt/${id}`)
        return data
    } catch (err) {
        console.error("Error deleting system prompt: ", err)
    }
  }

  async function handleDeleteTestPrompt(id: number) {
    try {
        const data = await axios.delete(`${apiUrl}/test_prompt/${id}`)
        return data 
    } catch (err) {
        console.error("Error deleting test prompt: ", err)
    }
  }

  
  return (
    <div>
      <Header />

      <div className="flex flex-col items-center p-10 space-y-12 bg-gray-50 min-h-screen">
        <h1 className="font-bold text-5xl mb-4 text-gray-900">Manage Prompts</h1>

        
        <div className="w-full max-w-4xl bg-white shadow-md rounded-xl border border-gray-200 p-8">
          <h2 className="text-2xl font-bold mb-6 text-gray-800">Add System Prompt</h2>
          <form
            className="flex flex-col space-y-6"
            onSubmit={(e) => {
              e.preventDefault();
              handleAddSystemPrompt();
            }}
          >
            <input
              className="border border-gray-300 rounded-md p-3 text-gray-800 focus:outline-none focus:ring-2 focus:ring-black"
              type="text"
              value={systemPrompt.title}
              onChange={(e) =>
                setSystemPrompt({ ...systemPrompt, title: e.target.value })
              }
              placeholder="Enter new system prompt title"
              required
            />
            <textarea
              className="border border-gray-300 rounded-md p-3 text-gray-800 h-32 resize-none focus:outline-none focus:ring-2 focus:ring-black"
              value={systemPrompt.body}
              onChange={(e) =>
                setSystemPrompt({ ...systemPrompt, body: e.target.value })
              }
              placeholder="Enter new system prompt body"
              required
            />
            <button
              className="bg-black text-white rounded-md py-3 font-semibold hover:bg-gray-800 transition"
              type="submit"
            >
              Add System Prompt
            </button>
          </form>
        </div>

        
        <div className="w-full max-w-4xl bg-white shadow-md rounded-xl border border-gray-200 p-8">
          <h2 className="text-2xl font-bold mb-6 text-gray-800">Add Test Prompt</h2>
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleAddTestPrompt();
            }}
            className="flex flex-col space-y-6"
          >
            <Select onValueChange={setSelectedSystemPrompt}>
              <SelectTrigger className="w-full border border-gray-300 rounded-md p-3 text-gray-800 focus:outline-none focus:ring-2 focus:ring-black">
                <SelectValue placeholder="Select a system prompt" />
              </SelectTrigger>
              <SelectContent>
                {systemPrompts.map((prompt) => (
                  <SelectItem key={prompt.id} value={prompt.id.toString()}>
                    {prompt.title}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>

            <textarea
              className="border border-gray-300 rounded-md p-3 text-gray-800 h-32 resize-none focus:outline-none focus:ring-2 focus:ring-black"
              value={testPrompt.body}
              onChange={(e) =>
                setTestPrompt({ ...testPrompt, body: e.target.value })
              }
              placeholder="Enter new test prompt body"
              required
            />

            <button
              className="bg-black text-white rounded-md py-3 font-semibold hover:bg-gray-800 transition"
              type="submit"
            >
              Add Test Prompt
            </button>
          </form>
        </div>

        <h1 className="font-bold text-5xl mb-4 text-gray-900"> Existing Prompts </h1>
        {systemAndTestPrompts.map((prompt) => (
            <div key={prompt.id}className="items-start space-y-8 flex flex-col w-full max-w-4xl bg-white shadow-md rounded-xl border border-gray-200 p-8" >
                <button onClick={() => handleDeleteSystemPrompt(prompt.id)} className="hover: cursor-pointer bg-red-500/90 hover:bg-red-600 text-white font-semibold px-4 py-2 rounded-md shadow-sm transition-all duration-200 ease-in-out hover:shadow-md active:scale-95 focus:outline-none">
                    Delete
                </button>
                <h1 className="font-bold text-3xl">{prompt.title}</h1>
                <p className="font-bold text-2xl">{prompt.body}</p>
                {prompt.test_prompts.length > 0 && (
                    <div>
                        <h2 className="font-semibold text-xl mb-2 text-gray-800">Test Prompts:</h2>
                        <ul className="list-none text-gray-700 space-y-2">
                            {prompt.test_prompts.map((test_prompt) => (
                                <li
                                    key={test_prompt.id}
                                    className="flex items-center space-x-3 text-lg text-gray-800"
                                >
                                    <button
                                        className="hover:cursor-pointer flex items-center justify-center w-6 h-6 rounded-sm bg-red-500/80 hover:bg-red-600 text-white text-sm font-bold shadow-sm transition-all duration-200 ease-in-out hover:scale-105 focus:outline-none"
                                        title="Delete test prompt"
                                        onClick={() => handleDeleteTestPrompt(test_prompt.id)}
                                    >
                                        ×
                                    </button>

                                    <span>{test_prompt.body}</span>
                                </li>
                            ))}
                            </ul>

                    </div>
                )}
            </div>
        ))}

      </div>

      

    </div>
  );
}
