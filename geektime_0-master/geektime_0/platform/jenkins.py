from jenkinsapi.jenkins import Jenkins

jenkins = Jenkins('http://42.192.248.147:8087/', useCrumb=True, username='404', password='zhoufan794336')
# todo: 按需添加认证信息
