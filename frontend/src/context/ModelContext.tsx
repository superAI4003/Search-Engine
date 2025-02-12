import React, { createContext, useContext, useState, ReactNode } from 'react';

interface ModelContextType {
  selectedModel: string[];
  setSelectedModel: React.Dispatch<React.SetStateAction<string[]>>;
  prompt: string;
  setPrompt: React.Dispatch<React.SetStateAction<string>>;
  conversationResults: { modelID: string; content: string; vote: boolean, query:string , search_content:string}[]; // Added this line
  setConversationResults: React.Dispatch<React.SetStateAction<{ modelID: string; content: string; vote: boolean, query:string, search_content:string }[]>>; // Added this line
}

const ModelContext = createContext<ModelContextType | undefined>(undefined);

export const ModelProvider = ({ children }: { children: ReactNode }) => {
    const [selectedModel, setSelectedModel] = useState<string[]>([]);
    const [prompt, setPrompt] = useState<string>(''); // Initialize with an empty string.
    const [conversationResults, setConversationResults] = useState<{ modelID: string; content: string; vote: boolean;query:string, search_content:string }[]>([]); // Added this line
    return (
      <ModelContext.Provider value={{ selectedModel, setSelectedModel, prompt, setPrompt, conversationResults, setConversationResults }}>
        {children}
      </ModelContext.Provider>
    );
  };
export const useModel = () => {
  const context = useContext(ModelContext);
  if (!context) {
    throw new Error('useModel must be used within a ModelProvider');
  }
  return context;
};