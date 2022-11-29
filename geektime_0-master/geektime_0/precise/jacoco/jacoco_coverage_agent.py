import os

from geektime_0.precise.core.coverage_agent import CoverageAgent


class JacocoCoverageAgent(CoverageAgent):
    def __init__(self, home, project, host='127.0.0.1', port=6300):
        self.host = host
        self.port = port
        self.jacoco_home = home
        self.project = project

    def clear(self):
        os.system('rm jacoco.exec || :')
        os.system(f'java -jar {self.jacoco_home}/lib/jacococli.jar '
                  f'dump '
                  f'--address {self.host} '
                  f'--port {self.port} '
                  f'--destfile jacoco.exec '
                  f'--reset')


    def collect(self, path='/tmp/jacoco') -> str:
        self.clear()
        os.system('ls')
        os.system('rm -rf /tmp/jacoco; '
                  'mkdir /tmp/jacoco')
        os.system(f'java -jar {self.jacoco_home}/lib/jacococli.jar '
                  f'report jacoco.exec '
                  f'--classfiles {self.project}/target/classes/ '
                  f'--sourcefiles {self.project}/src/main/java/ '
                  f'--html {path} '
                  f'--xml {path}/jacoco.xml '
                  f'--csv {path}/jacoco.csv')
        return f'{path}/jacoco.xml'
