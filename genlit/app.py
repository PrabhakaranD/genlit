from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://genlit_admin:genlit_admin@localhost/genlit_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Agent {self.name}>'

@app.route('/')
def home():
    return "Welcome to GenLit - Your GenAI Agents Management Platform!"

@app.route('/agents', methods=['GET'])
def list_agents():
    agents = Agent.query.all()
    return render_template('list_agents.html', agents=agents)

@app.route('/agents/<int:agent_id>', methods=['GET'])
def show_agent(agent_id):
    agent = Agent.query.get_or_404(agent_id)
    return render_template('show_agent.html', agent=agent)


@app.route('/agents/new', methods=['GET', 'POST'])
def create_agent():
    if request.method == 'POST':
        agent_name = request.form['name']
        new_agent = Agent(name=agent_name)
        db.session.add(new_agent)
        db.session.commit()
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

with app.app_context():
    db.create_all()

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()



