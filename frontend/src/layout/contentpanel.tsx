import { useModel } from "@/context/ModelContext";
import { useState } from "react";
import { AiOutlineSend } from "react-icons/ai";
import ReactLoading from "react-loading";
import { AiFillLike } from "react-icons/ai";

function ContentPanel() {
  const [isGenerating, setIsGenerating] = useState(false);
  const { prompt, selectedModel } = useModel();
  const [query, setQuery] = useState("");
  const {conversationResults, setConversationResults} = useModel();

  const handleSearch = async () => {
    try {
      const response = await fetch(
        `${
          import.meta.env.VITE_BACKEND_URL
        }/search/search?query=${encodeURIComponent(query)}`
      );
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      return data.google_results;
    } catch (error) {
      console.error("Error fetching search results:", error);
      return error;
    }
  };
  const handleConversation = async (search_content: string) => {
    try {
      const results = [];
      for (const modelID of selectedModel) {
        const response = await fetch(
          `${import.meta.env.VITE_BACKEND_URL}/llm/conversation`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              llm_id: modelID,
              prompt: `${prompt}${search_content}`,
            }),
          }
        );

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        let content = "";
        if (data.choices && data.choices.length > 0) {
          content = data.choices[0].message.content;
        } else {
          console.error("Unexpected response structure:", data);
          content = "No content available";
        }
        const vote = false;
        const result = { modelID, content, vote, query, search_content };
        results.push(result);
        setConversationResults((prevResults) => [...prevResults, result]);
      }
      return results;
    } catch (error) {
      console.error("Error fetching conversation data:", error);
      return error;
    }finally{
      setQuery("");
    }

  };

  const handleGenerating = async () => {
    setIsGenerating(true);
    const search_content = await handleSearch();
    await handleConversation(search_content);
    setIsGenerating(false);
  };
  return (
    <div className="w-full h-full bg-[#ffffff] rounded-t-lg shadow-lg relative">
      <div className="w-full h-[800px] flex  justify-around  ">
        {conversationResults.length > 0 &&
          conversationResults.map((result,index) => (
            <div className="w-[32%] flex flex-col overflow-y-auto border rounded-md border-gray-400 shadow-md overflow-hidden hover:cursor-pointer hover:bg-gray-100"
            key={index}
            onClick={() => {
              setConversationResults((prevResults) =>
                prevResults.map((r) =>
                  r.modelID === result.modelID
                    ? { ...r, vote: !r.vote }
                    : r
                )
              );
            }}
            >
              <div className="bg-gray-800 text-white py-2 text-center px-4">
                <p className="text-left"><span className="font-bold">Model:</span> {result.modelID}</p>
                <p className="text-left"><span className="font-bold">Query:</span> {result.query}</p>
              </div>
              {result.vote &&<div className="flex justify-center p-2">
                <AiFillLike size={20} className="text-gray-600 hover:text-gray-800 cursor-pointer" />
              </div>}
              <p className="p-2 whitespace-pre-wrap">
                {result.content}
              </p>
              
            </div>
          ))}
      </div>
      <div className="  py-2 pl-6 pr-2 absolute bottom-3 left-1/2 transform -translate-x-1/2 mb-4 w-8/12 flex items-center border rounded-full shadow-sm ">
        <input
          type="text"
          className="w-full  border-none  focus:border-none focus:outline-none hover:border-none px-2 text-[18px]"
          placeholder="Type your message..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button
          onClick={() => handleGenerating()}
          className="w-[50px] h-[50px] bg-black justify-center items-center flex rounded-full hover:bg-black/80 disabled:bg-gray-500"
          disabled={!(prompt && selectedModel.length > 0 && query)}
        >
          {!isGenerating ? (
            <AiOutlineSend size={20} className="text-white" />
          ) : (
            <ReactLoading type="bars" color="#ffffff" height={25} width={25} />
          )}
        </button>
      </div>
    </div>
  );
}

export default ContentPanel;
