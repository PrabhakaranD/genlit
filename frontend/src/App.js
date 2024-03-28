import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AgentsList from './AgentsList';
import AgentDetails from './AgentDetails';
// Import other components

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<AgentsList />} index />
        <Route path="/agents/:agentId" element={<AgentDetails />} />
        {/* Define other routes */}
      </Routes>
    </Router>
  );
}

export default App;