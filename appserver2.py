from flask import Flask
from flask import request
from flask import render_template

from mongodb2_client import insert_note
from mongodb2_client import find_all_notes
from mongodb2_client import delete_all_notes
app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template("submit_form_2.html")

@app.route('/find-all-notes',methods=['GET'])
def find_all_docs():
    doc_list = find_all_notes()
    return render_template("showdiary.html", data=doc_list)

@app.route('/insert-note',methods=['POST'])
def insert_note_doc():
    title=request.form['title']
    note=request.form['note']
    date=request.form['date']
    insert_note(title, note, date)
    return show_form()

@app.route('/delete-all-notes',methods=['POST'])
def delete_all():
    delete_all_notes()
    return show_form()


if __name__ == "__main__":
    app.run()
