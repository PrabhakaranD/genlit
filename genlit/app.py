from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to GenLit - Your GenAI Agents Management Platform!"

@app.route('/agents', methods=['GET'])
def list_agents():
    return "Here you will see a list of all GenAI agents."

@app.route('/agents/<int:agent_id>', methods=['GET'])
def show_agent(agent_id):
    return f"Details of GenAI agent {agent_id}."

@app.route('/agents/new', methods=['GET', 'POST'])
def create_agent():
    if request.method == 'POST':
        # Here, you'll eventually add logic to save the agent's data
        agent_name = request.form['name']
        return f"Creating a new GenAI agent named {agent_name}."
    return render_template('create_agent.html')

@app.route('/agents/<int:agent_id>/edit', methods=['GET', 'POST'])
def edit_agent(agent_id):
    if request.method == 'POST':
        # Logic to update the agent goes here
        return f"Updating GenAI agent {agent_id}."
    return f"Form to update GenAI agent {agent_id}."

@app.route('/agents/<int:agent_id>/delete', methods=['POST'])
def delete_agent(agent_id):
    # Logic to delete the agent goes here
    return f"GenAI agent {agent_id} has been deleted."

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
