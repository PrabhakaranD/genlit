from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://genlit_admin:genlit_admin@localhost/genlit_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f'<Agent {self.name}>'

@app.route('/')
def home():
    return "Welcome to GenLit - Your GenAI Agents Management Platform!"

@app.route('/agents', methods=['GET'])
def list_agents():
    agents = Agent.query.filter_by(is_active=True).all()
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
        return f"A new GenAI agent named {agent_name} has been created."
    return render_template('create_agent.html')

@app.route('/agents/<int:agent_id>/edit', methods=['GET', 'POST'])
def edit_agent(agent_id):
    agent = Agent.query.get_or_404(agent_id)
    if request.method == 'POST':
        agent.name = request.form['name']
        db.session.commit()
        return redirect(url_for('list_agents'))
    return render_template('edit_agent.html', agent=agent)


@app.route('/agents/inactive', methods=['GET'])
def list_inactive_agents():
    agents = Agent.query.filter_by(is_active=False).all()
    return render_template('list_inactive_agents.html', agents=agents)



@app.route('/agents/<int:agent_id>/delete', methods=['POST'])
def delete_agent(agent_id):
    agent = Agent.query.get_or_404(agent_id)
    agent.is_active = False
    db.session.commit()
    return redirect(url_for('list_agents'))

@app.route('/agents/<int:agent_id>/restore', methods=['POST'])
def restore_agent(agent_id):
    agent = Agent.query.get_or_404(agent_id)
    agent.is_active = True
    db.session.commit()
    return redirect(url_for('list_agents'))

with app.app_context():
    db.create_all()

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()



