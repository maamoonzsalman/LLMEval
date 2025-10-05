import { ModelData } from "./SelectPrompts";
import { Loader2 } from "lucide-react";
import React from "react";

export default function Models({
  modelData,
  loading,
}: {
  modelData: ModelData | null;
  loading: boolean;
}) {
  const models = [
    { key: "claude_output", scoreKey: "claude_score", name: "claude-3.5-sonnet" },
    { key: "openai_output", scoreKey: "openai_score", name: "gpt-4o" },
    { key: "gemini_output", scoreKey: "gemini_score", name: "gemini-2.5-pro" },
  ];

  return (
    <div className="flex flex-wrap justify-center gap-8 overflow-y-auto max-h-[90vh] p-6">
      {models.map((model) => {
        const output =
          modelData?.output?.[model.key as keyof typeof modelData.output];
        const scores =
          modelData?.scores?.[model.scoreKey as keyof typeof modelData.scores];
        const text = output?.text || "Waiting for evaluation...";

        return (
          <div
            key={model.key}
            className="flex flex-col border rounded-xl w-96 bg-white shadow-md p-4 text-center"
          >
            {/* Model Header */}
            <div className="bg-black text-white text-sm px-3 py-1 rounded-md mb-3 font-semibold w-fit mx-auto">
              {model.name}
            </div>

            {/* Text Output */}
            <div className="flex-1 overflow-y-auto max-h-[50vh] text-left text-gray-800 whitespace-pre-line border rounded-md p-3">
              {loading ? (
                <div className="flex flex-col items-center justify-center space-y-2 py-12">
                  <Loader2 className="h-6 w-6 animate-spin text-gray-500" />
                  <p className="text-gray-500 text-sm">Evaluating...</p>
                </div>
              ) : (
                text
              )}
            </div>

            {/* Metrics Table */}
            {!loading && scores && (
              <div className="mt-4">
                <table className="w-full border-collapse text-sm">
                  <thead>
                    <tr className="border-b text-gray-700">
                      <th className="py-1 text-left">Metric</th>
                      <th className="py-1 text-right">Score (%)</th>
                    </tr>
                  </thead>
                  <tbody>
                    {Object.entries(scores).map(([metric, value]) => {
                      const v = value as {
                        score_0_to_1: number;
                        reason: string;
                      };
                      const percent = Math.round(v.score_0_to_1 * 100);
                      return (
                        <tr key={metric} className="border-t">
                          <td className="py-1 text-left capitalize">{metric}</td>
                          <td
                            className={`py-1 text-right font-medium ${
                              percent >= 80
                                ? "text-green-600"
                                : percent >= 60
                                ? "text-yellow-600"
                                : "text-red-600"
                            }`}
                          >
                            {percent}%
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
