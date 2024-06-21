#pip install GitPython
from git import Git, Repo
import time

repo = Repo.init('.')  #初始化
repo = Repo('.')
repo.index.add(['mygit.py'])  #檔案
now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
repo.index.commit(now)  #註解
g = Git(repo.working_dir)
g.push('https://github.com/tu202/gittest.git')
