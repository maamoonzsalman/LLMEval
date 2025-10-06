"use client"
import Header from "./components/Header/Header";
import SelectPrompts from "./components/LandingPage/SelectPrompts";
import Models from "./components/LandingPage/Models";
import type { ModelData } from "./components/LandingPage/SelectPrompts"; 
import { useState } from "react";

export default function Home() {
  const [modelData, setModelData] = useState<ModelData | null>(null);
  const [loading, setLoading] = useState(false);

  return (
    <div className="font-sans min-h-screen bg-white">
      <Header/>
      
      <div className="flex flex-col items-center space-y-12 py-12">
        
        <h1 className="text-black font-bold text-6xl">LLM Evaluation Platform</h1>
        
        <SelectPrompts setModelData={setModelData} setLoading={setLoading}/>
        
        <Models modelData={modelData} loading={loading}/>

      </div>

    </div>
  );
}
