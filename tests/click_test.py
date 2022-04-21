"""Testing to log files and lof folders"""
import os

from click.testing import CliRunner

from app import create_log_folder, create_database, create_my_message, create_log_file

runner = CliRunner()


def test_create_mymessage():
    """testing mymessage log file"""
    response = runner.invoke(create_my_message)
    assert response.exit_code == 0
    log_file_mymessage = '/home/myuser/app/logs/mymessage.log'
    assert os.path.exists(log_file_mymessage)


def test_create_log_folder():
    """Here wea re testing existence of log folders"""
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    #root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = '/home/myuser/app/logs'
    # make a directory if it doesn't exist
    assert os.path.exists(logdir),""

def test_create_database():
    """Testing the create database"""
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir)


def test_create_log_file():
    """here we are testing the create log file"""
    response = runner.invoke(create_log_file)
    assert response.exit_code == 0
    log_file_errors = '/home/myuser/app/logs/errors.log'
    assert os.path.exists(log_file_errors), 'not found errors.log '
    log_file_flask = '/home/myuser/app/logs/flask.log'
    assert os.path.exists(log_file_flask), 'not found flask.log '
    log_file_myapp = '/home/myuser/app/logs/myapp.log'
    assert os.path.exists(log_file_myapp), 'not found myapp.log '
    log_file_request = '/home/myuser/app/logs/request.log'
    assert os.path.exists(log_file_request), 'not found request.log '
    log_file_sqlalchemy = '/home/myuser/app/logs/sqlalchemy.log'
    assert os.path.exists(log_file_sqlalchemy), 'not found sqlalchemy.log '
    log_file_werkzeug = '/home/myuser/app/logs/werkzeug.log'
    assert os.path.exists(log_file_werkzeug), 'not found werkzeug.log '
