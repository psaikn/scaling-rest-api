import os
import json
import re

from flask import request, Blueprint, jsonify

from api import db, app
from api.utils import authorize

books = Blueprint('books', __name__, url_prefix='/books')

@books.route('/create', methods=['POST'])
@authorize
def createbooks(user):
    bookname = request.form.get('bookname')
    author = request.form.get('author')
    published_date = request.form.get('published_date')
    no_of_books = request.form.get('no_of_books')
    rack_no = request.form.get('rack_no')
    user_id = user.get('user_id')
    try:
        sql = ("INSERT INTO `books` (`book_name`, `author`, `publisheddate`, `no_of_books`, `rack_no`, `user_id`) "
               "VALUES ('{}', '{}', '{}', '{}','{}','{}');")
        sql = sql.format(bookname, author, published_date, no_of_books, rack_no, user_id)
        app.logger.info('Books Uploaded - SQL Insert: {}'.format(sql))
        db.session.execute(sql)
        db.session.commit()
        return jsonify({"meesage": "Records Create Sucessfully"})
    except Exception as e:
        app.logger.error('materialUpload- Exception: {}'.format(e))
        return jsonify({"message": "Failure"})


@books.route('/update', methods=['POST'])
@authorize
def updatebooks(user):
    book_id = request.form.get('bookid')
    bookname = request.form.get('bookname')
    author = request.form.get('author')
    published_date = request.form.get('published_date')
    no_of_books = request.form.get('no_of_books')
    rack_no = request.form.get('rack_no')
    user_id = user.get('user_id')
    try:
        sql = "SELECT * FROM books where book_id={}".format(book_id)
        rows = db.session.execute(sql).fetchall()
        if not rows:
            app.logger.error('Book Not Found: {}'.format(book_id))
            return jsonify({"message": "Unable to Update the book records",
                            "reason": "Unable to fetch the records matching to book id"})
        elif len(rows) > 1:
            return jsonify({"message": "Unable to Update the book records",
                            "reason": "Found more than one records for same book id"})
        else:
            sql = ("UPDATE books SET book_name='{}', author='{}', publisheddate='{}',"
                   " no_of_books='{}', rack_no='{}', user_id='{}'"
                   " WHERE book_id={}"
                   )
            sql = sql.format(bookname, author, published_date, no_of_books, rack_no, user_id, book_id)
            db.session.execute(sql)
            db.session.commit()
            return jsonify({"meesage": "Records Updated Sucessfully"})
    except Exception as e:
        app.logger.error('Update Failed- Exception: {}'.format(e))
        return jsonify({"message": "Failure", "exception": e})


@books.route('/all', methods=['GET'])
@authorize
def getallbooks(user):
    try:
        sql = "SELECT * FROM books"
        rows = db.session.execute(sql).fetchall()
        data = []
        for row in rows:
            data.append({"book_name": row['book_name'], "author": row['author'], "publisheddate": row['publisheddate'],
                         "no_of_books": row['no_of_books'], "rack_no": row['rack_no']})
        return jsonify({"meesage": "Records fetched Sucessfully", "data": data})
    except Exception as e:
        app.logger.error('Fetching Failed- Exception: {}'.format(e))
        return jsonify({"message": "Failure", "exception": e})


@books.route('/getbook', methods=['POST'])
@authorize
def getbooks(user):
    book_id = request.form.get('bookid')
    try:
        sql = "SELECT * FROM books where book_id={}".format(book_id)
        rows = db.session.execute(sql).fetchall()
        data = []
        for row in rows:
            data.append({"book_name": row['book_name'], "author": row['author'], "publisheddate": row['publisheddate'],
                         "no_of_books": row['no_of_books'], "rack_no": row['rack_no']})
        return jsonify({"meesage": "Records fetched Sucessfully", "data": data})
    except Exception as e:
        app.logger.error('Fetching Failed- Exception: {}'.format(e))
        return jsonify({"message": "Failure", "exception": e})


