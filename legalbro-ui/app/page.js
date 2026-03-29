"use client";

import { useState } from "react";
import ReactMarkdown from "react-markdown";

export default function Home() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const simplify = async () => {
    if (!text.trim()) {
      setResult("Please enter some legal text first.");
      return;
    }

    setLoading(true);
    setResult("");

    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/v1/legal/simplify`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }

      const responseData = await res.json();

      // Support both possible response structures
      const markdownText =
        responseData?.data?.simplified ||
        responseData?.simplified ||
        JSON.stringify(responseData);

      setResult(markdownText);
    } catch (err) {
      console.error("Fetch error:", err);
      setResult(`Error: ${err.message}\n\nIs the backend running?`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white flex items-center justify-center px-4 py-12">
      <div className="w-full max-w-3xl bg-white/5 backdrop-blur-lg p-8 rounded-3xl shadow-2xl border border-white/10">
        {/* Header */}
        <div className="text-center mb-10">
          <h1 className="text-4xl font-bold mb-3 flex items-center justify-center gap-3">
            ⚖️ LegalBro
          </h1>
          <p className="text-gray-400 text-lg">
            Ask legal questions and get answer with reference instantly
          </p>
        </div>

        {/* Input */}
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Paste/write your legal query here..."
          className="w-full h-64 p-5 rounded-2xl bg-black/60 border border-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-200 placeholder-gray-500 resize-y font-mono text-sm"
        />

        {/* Button */}
        <button
          onClick={simplify}
          disabled={loading || !text.trim()}
          className="mt-6 w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed transition-all py-4 rounded-2xl font-semibold text-lg flex items-center justify-center gap-2"
        >
          {loading ? (
            <>
              <span className="animate-spin">⚙️</span>
              Thinking...
            </>
          ) : (
            "Get your answer"
          )}
        </button>

        {/* Result */}
        {result && (
          <div className="mt-10">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-green-400 flex items-center gap-2">
                ✅ Your answer
              </h2>
              <button
                onClick={() => navigator.clipboard.writeText(result)}
                className="text-sm px-4 py-2 bg-white/10 hover:bg-white/20 rounded-xl transition-colors"
              >
                📋 Copy
              </button>
            </div>

            <div className="prose prose-invert prose-sm max-w-none bg-black/40 border border-gray-700 rounded-2xl p-7 leading-relaxed">
              <ReactMarkdown>{result}</ReactMarkdown>
            </div>
          </div>
        )}
      </div>
    </main>
  );
}