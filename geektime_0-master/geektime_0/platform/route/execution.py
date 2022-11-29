from dataclasses import asdict

from flask import Blueprint, request
from sqlalchemy.orm import Query

from geektime_0.platform.app import app
from geektime_0.platform.db import db
from geektime_0.platform.domain.execution import Execution
from geektime_0.platform.domain.task import Task
from geektime_0.platform.domain.testcase import TestCase
from geektime_0.platform.jenkins import jenkins

task_bp = Blueprint('task', __name__)


@task_bp.route('/execution/<id>', methods=['GET'])
def execution_get(id):
    query: Query = Execution.query
    execution = query.filter(Execution.id == id).scalar()
    app.logger.error(execution)
    # tasks = [asdict(task) for task in task.tasks]

    return {
        'errcode': 0,
        'data': asdict(execution),
        # 'tasks': tasks
    }


@task_bp.route('/execution', methods=['POST'])
def execution_post():
    query: Query = Task.query
    task = query.filter(Task.id == request.json['task_id']).scalar()
    execution = Execution()
    execution.name = task.name
    execution.task = task

    # task.testcase_id = request.json['testcase_id']
    db.session.add(execution)
    db.session.commit()

    # 任务调度
    # jenkins['demo'].get_last_build().get_artifacts()
    return {
        'errcode': 0,
    }
