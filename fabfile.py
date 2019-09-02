from fabric.api import env, run

from fabric.operations import sudo

GIT_REPO = "https://github.com/FangXianShen/blog_project.git" 

env.user = 'root' 
env.password = '970626HeJY'

# ��д���Լ���������Ӧ������
env.hosts = ['114.55.92.22']

# һ�������Ϊ 22 �˿ڣ������ 22 �˿���鿴������������ṩ���ṩ����Ϣ
env.port = '22'


def deploy():
        source_folder = '/home/fangz/sites/fangshiyu.top/blog_project' 
        run('cd %s && git pull' % source_folder) 
        run("""
            cd {} &&
            ../env/bin/pip install -r requirements.txt &&
            ../env/bin/python3 manage.py collectstatic --noinput &&
            ../env/bin/python3 manage.py makemigrations &&
            ../env/bin/python3 manage.py migrate
            """.format(source_folder))
        sudo('systemctl restart blog.service') 
        sudo('service nginx reload')
