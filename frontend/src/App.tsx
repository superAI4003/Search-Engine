import ContentPanel from "./layout/contentpanel";
import ControlPanel from "./layout/controlpanel";
import { ModelProvider } from "./context/ModelContext";

function App() {
  return (
    <ModelProvider>
      <div className="bg-[#ffffff] w-full min-h-screen flex">
        <div className="w-[500px] flex flex-col ">
          <ControlPanel />
        </div>
        <div className="flex-1 pt-[10px] pr-[10px] flex flex-col ">
          <ContentPanel />
        </div>
      </div>
    </ModelProvider>
  );
}

export default App;
