import { useEffect, useState } from "react";
import { MultiSelect } from "@/components/ui/multi-select";
import { Textarea } from "@/components/ui/textarea";
import ReactLoading from "react-loading";
import { useModel } from "@/context/ModelContext";

function ControlPanel() {
  const [models, setModels] = useState<any[]>([]);
  const { selectedModel, setSelectedModel } = useModel();
  const { prompt, setPrompt } = useModel();
  // ... existing code ...
  useEffect(() => {
    const backendUrl = import.meta.env.VITE_BACKEND_URL;

    const fetchData = async () => {
      try {
        const response = await fetch(`${backendUrl}/llm/models`);
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const responseData = await response.json();
        const transformedData = responseData.data.map((item: any) => ({
          value: item.id,
          label: item.name,
        }));
        setModels(transformedData);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData(); // Remove 'await' here
  }, []);

  return (
    <div className="w-full h-full pt-[10px] px-4 space-y-4">
      {models.length > 0 ? (
        <div className="p-4 max-w-xl">
          <h1 className="text-md font-bold py-2">Select Model.</h1>
          <MultiSelect
            options={models}
            onValueChange={setSelectedModel}
            defaultValue={selectedModel}
            placeholder="Select Models"
            variant="inverted"
            animation={2}
            maxCount={3}
          />
          <h1 className="text-md font-bold py-2">Input Prompt.</h1>
          <Textarea
            placeholder="Type your message here."
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            id="message-2"
            rows={4}
          />
        </div>
      ) : (
        <div className="flex items-center justify-center h-full">
          <ReactLoading type="bars" color="#000000" height={50} width={50} />
        </div>
      )}
    </div>
  );
}

export default ControlPanel;
