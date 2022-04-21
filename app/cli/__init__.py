import os

import click
from flask.cli import with_appcontext
from app.db import db


@click.command(name='create-db')
@with_appcontext
def create_database():
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../../database')
    # make a directory if it doesn't exist
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
    db.create_all()


@click.command(name='create-log-folder')
@with_appcontext
def create_log_folder():
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../logs')
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)


@click.command(name='my_message')
@with_appcontext
def create_my_message():
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    memessage = os.path.join(root, '../logs/mymessage.log')
    # make a directory if it doesn't exist
    if not os.path.exists(memessage):
        os.mkdir(memessage)


@click.command(name='create_log_file')
@with_appcontext
def create_log_file():
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../logs')

    errors_log_file = os.path.join(logdir, '../errors.log')
    flask_log_file = os.path.join(logdir, '../flask.log')
    myapp_log_file = os.path.join(logdir, '../myapp.log')
    request_log_file = os.path.join(logdir, '../request.log')
    sqlalchemy_log_file = os.path.join(logdir, '../sqlalchemy.log')
    werkzeug_log_file = os.path.join(logdir, '../werkzeug.log')

    # here we will make a directory if it doesnt exist
    if not os.path.exists(errors_log_file):
        os.mkdir(errors_log_file)
    if not os.path.exists(flask_log_file):
        os.mkdir(flask_log_file)
    if not os.path.exists(myapp_log_file):
        os.mkdir(myapp_log_file)
    if not os.path.exists(request_log_file):
        os.mkdir(request_log_file)
    if not os.path.exists(sqlalchemy_log_file):
        os.mkdir(sqlalchemy_log_file)
    if not os.path.exists(werkzeug_log_file):
        os.mkdir(werkzeug_log_file)
