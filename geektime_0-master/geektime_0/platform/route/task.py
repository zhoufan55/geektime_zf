from dataclasses import asdict

from flask import Blueprint, request
from sqlalchemy.orm import Query

from geektime_0.platform.app import app
from geektime_0.platform.db import db
from geektime_0.platform.domain.task import Task
from geektime_0.platform.domain.testcase import TestCase
from geektime_0.platform.jenkins import jenkins

task_bp = Blueprint('task', __name__)


@task_bp.route('/task/<id>', methods=['GET'])
def task_id_get(id):
    query: Query = Task.query
    task = query.filter(Task.id == id).scalar()
    app.logger.error(task)
    # tasks = [asdict(task) for task in task.tasks]

    return {
        'errcode': 0,
        'data': asdict(task),
        # 'tasks': tasks
    }


@task_bp.route('/task', methods=['GET'])
def task_get():
    tasks = Task.query.all()
    data = [asdict(task) for task in tasks]

    return {
        'errcode': 0,
        'data': data,
        # 'tasks': tasks
    }


@task_bp.route('/task', methods=['POST'])
def task_post():
    testcase = TestCase.query.filter(TestCase.id == request.json['testcase_id']).scalar()
    task = Task()
    task.name = testcase.name
    task.testcase = testcase

    # task.testcase_id = request.json['testcase_id']
    db.session.add(task)
    db.session.commit()

    # 任务调度
    jenkins['testcase_run'].invoke(build_params={
        'testcase': testcase.name,
        'git': testcase.data,
        'taskid': task.id
    })
    return {
        'errcode': 0,
    }


@task_bp.route('/task/<tid>', methods=['POST'])
def task_id_post(tid):
    task = Task.query.filter(Task.id == tid).first()
    task.name = request.json['name']
    # task.testcase_id = request.json['testcase_id']
    db.session.add(task)
    db.session.commit()
    return {
        'errcode': 0
    }
