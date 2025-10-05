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

export default function ManagePrompts() {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL;
  const [systemPrompt, setSystemPrompt] = useState<SystemPromptOut>({
    title: "",
    body: "",
  });
  const [testPrompt, setTestPrompt] = useState<TestPromptOut>({ body: "" });

  const [systemPrompts, setSystemPrompts] = useState<SystemPrompt[]>([]);
  const [selectedSystemPrompt, setSelectedSystemPrompt] = useState("");

  
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
      </div>
    </div>
  );
}
