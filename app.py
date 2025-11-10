from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models.database import db, Person, Expense
import pandas as pd

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

#Crear tablas si no existen 
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    people = Person.query.all()
    expenses = Expense.query.all()
    return render_template('index.html', people=people, expenses=expenses)

@app.route('/add_person', methods=['POST'])
def add_person():
   name = request.form['name']
   if name:
        person = Person(name=name)
        db.session.add(person)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    description = request.form['description']
    amount = float(request.form['amount'])
    person_id = int(request.form['person_id'])
    expense = Expense(description=description, amount=amount, person_id=person_id)
    db.session.add(expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_person/<int:person_id>', methods=['POST'])
def delete_person(person_id):
    person = Person.query.get(person_id)
    if person:
        # borrar todos los gastos de esa persona primero
        Expense.query.filter_by(person_id=person.id).delete()
        db.session.delete(person)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/summary')
def summary():
    expenses = Expense.query.all()
    data = []

    for e in expenses:
        if e.payer:
            data.append({'person': e.payer.name, 'amount': e.amount})

    # obtener todos los nombres registrados
    all_people = [p.name for p in Person.query.all()]

    if not data:
        # si no hay gastos aún, todos tienen saldo cero
        summary = pd.DataFrame({'person': all_people, 'amount': [0]*len(all_people), 'balance': [0]*len(all_people)})
        return render_template('summary.html', summary=summary.to_dict(orient='records'), transactions=[])

    df = pd.DataFrame(data)
    summary = df.groupby('person', as_index=False)['amount'].sum()

    # asegurar que todos estén, incluso los que no pagaron nada
    for person in all_people:
        if person not in summary['person'].values:
            summary.loc[len(summary)] = [person, 0.0]

    total = summary['amount'].sum()
    per_person = total / len(all_people)
    summary['balance'] = summary['amount'] - per_person

    # Calcular quién debe pagarle a quién
    transactions = []
    debtors = summary[summary['balance'] < 0].copy()
    creditors = summary[summary['balance'] > 0].copy()

    for i, debtor in debtors.iterrows():
        amount_owed = -debtor['balance']
        for j, creditor in creditors.iterrows():
            if amount_owed == 0:
                break
            pay_amount = min(amount_owed, creditor['balance'])
            if pay_amount > 0:
                transactions.append(
                    f"{debtor['person']} debe pagarle ${pay_amount:.2f} a {creditor['person']}"
                )
                creditors.at[j, 'balance'] -= pay_amount
                amount_owed -= pay_amount

    return render_template(
        'summary.html',
        summary=summary.to_dict(orient='records'),
        transactions=transactions
    )
if __name__ == '__main__':
    app.run(debug=True)