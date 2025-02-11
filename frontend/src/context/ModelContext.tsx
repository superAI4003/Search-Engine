import React, { createContext, useContext, useState, ReactNode } from 'react';

interface ModelContextType {
  selectedModel: string[];
  setSelectedModel: React.Dispatch<React.SetStateAction<string[]>>;
  prompt: string;
  setPrompt: React.Dispatch<React.SetStateAction<string>>;
}

const ModelContext = createContext<ModelContextType | undefined>(undefined);

export const ModelProvider = ({ children }: { children: ReactNode }) => {
    const [selectedModel, setSelectedModel] = useState<string[]>([]);
    const [prompt, setPrompt] = useState<string>(''); // Initialize with an empty string
    return (
      <ModelContext.Provider value={{ selectedModel, setSelectedModel, prompt, setPrompt }}>
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