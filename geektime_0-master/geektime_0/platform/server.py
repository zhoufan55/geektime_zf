from geektime_0.platform.app import app
from geektime_0.platform.route.auth import auth_bp
from geektime_0.platform.route.task import task_bp
from geektime_0.platform.route.testcase import testcase_bp

if __name__ == '__main__':
    app.register_blueprint(auth_bp)
    app.register_blueprint(testcase_bp)
    app.register_blueprint(task_bp)
    # with app.app_context():
    #     db.create_all()
    # user1=User()
    # user1.username='seveniruby2'
    # user1.email='seveniruby@ceshiren.com'
    # db.session.add(user1)
    # db.session.commit()

    app.run(debug=True)
