import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AgentsList() {
  const [agents, setAgents] = useState([]);

  useEffect(() => {
    // Adjust the URL if your API endpoint differs
    axios.get('/api/agents')
      .then(response => {
        setAgents(response.data);
      })
      .catch(error => console.error("There was an error fetching the agents:", error));
  }, []);

  const handleDelete = (agentId) => {
    axios.post(`/api/agents/${agentId}/delete`)
      .then(() => {
        // Remove the deleted agent from the state to update the UI
        setAgents(agents.filter(agent => agent.id !== agentId));
      })
      .catch(error => console.error("There was an error deleting the agent:", error));
  };

  return (
    <div>
      <h1>List of GenAI Agents</h1>
      <ul>
        {agents.length > 0 ? (
          agents.map(agent => (
            <li key={agent.id}>
              {agent.name}
              <button onClick={() => handleDelete(agent.id)} style={{ marginLeft: '10px' }}>Delete</button>
            </li>
          ))
        ) : (
          <li>No agents found.</li>
        )}
      </ul>
      {/* You'll need to adjust the navigation to use React Router or similar for SPA navigation */}
      <a href="/deleted-agents">View Deleted Agents</a>
    </div>
  );
}

export default AgentsList;
