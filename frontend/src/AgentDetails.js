import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function AgentDetails() {
  const { agentId } = useParams();
  const [agent, setAgent] = useState(null);

  useEffect(() => {
    axios.get(`/api/agents/${agentId}`)
      .then(response => {
        setAgent(response.data);
      })
      .catch(error => console.error("There was an error fetching the agent details:", error));
  }, [agentId]);

  return (
    <div>
      {agent ? (
        <>
          <h1>Agent Details</h1>
          <p>ID: {agent.id}</p>
          <p>Name: {agent.name}</p>
          <p>Status: {agent.is_active ? 'Active' : 'Inactive'}</p>
        </>
      ) : (
        <p>Loading agent details...</p>
      )}
    </div>
  );
}

export default AgentDetails;
