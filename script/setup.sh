#!/usr/bin/env bash

system_update(){
echo '正在系统更新'
#apt update -y
#apt upgrate -y
#sed -i 's/\r//g' setup.sh 传输后格式调整
yum update -y
echo -e '系统更新完成\n'
}

install_software(){
echo '正在安装系统组件'
BASIC='man gcc make sudo lsof ssh openssl tree vim language-pack-zh-hans'
EXT='dnsutils iputils-ping net-tools psmisc sysstat'
NETWORK='curl telnet traceroute wget'
LIBS='libbz2-dev libpcre3 libpcre3-dev libreadline-dev libsqlite3-dev libssl-dev zlib1g-dev'
LIBS2='bzip2-devel bzip2-libs  readline readline-devel readline-static  openssl openssl-devel openssl-static sqlite-devel'
SOFTWARE='git mysql-server zip p7zip apache2-utils sendmail'
#apt install -y $BASIC $EXT $NETWORK $LIBS $SOFTWARE
yum install -y $BASIC $EXT $NETWORK $LIBS $SOFTWARE $LIBS2

echo '删除临时文件'
#apt autoremove
#apt autoclean
#yum autoremove
#yum autoclean

echo '设置中文环境'
locale-gen zh_CN.UTF-8
export LC_ALL='zh_CN.utf8'
echo "export LC_ALL='zh_CN.utf8'" >> /ect/bash.bashrc

echo '运行邮箱服务'
service sendmail start

echo -e '安装系统组件完成\n'
}


install_nginx(){
echo '正在安装Nginx'
if ! which nginx >/dev/null
then
    wget -P /tmp 'http://nginx.org/download/nginx-1.14.1.tar.gz'
    tar -zxf /tmp/nginx-1.14.1.tar.gz -C /tmp
    cd /tmp/nginx-1.14.1
    ./configure
    make
    make install
    cd -
    rm -rf /tmp/nginx*
    ln -s /user/local/nginx/sbin/nginx /user/local/bin/nginx
    echo -e '安装Nginx完成\n'
else
    echo -e 'Nginx已经存在\n'
fi
}

install_redis(){
echo '正在安装Redis'
if ! which redis-server >/dev/null
then
    wget -P /tmp 'http://download.redis.io/releases/redis-5.0.0.tar.gz'
    tar -zxf /tmp/redis-5.0.0.tar.gz -C /tmp
    cd /tmp/redis-5.0.0
    make && make install
    cd -
    rm -rf /tmp/redis*
    echo -e 'Redis已经安装完成\n'
else
    echo -e 'Redis已经存在\n'
fi
}


install_pyenv(){
echo '正在安装pyenv'
if ! which pyenv > /dev/null
then
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    echo -e 'pyenv安装完成\n'
else
    echo -e 'pyenv已经存在\n'
fi
}

#
#Cloning into '/root/.pyenv/plugins/pyenv-virtualenv'...
#fatal: unable to access 'https://github.com/pyenv/pyenv-virtualenv.git/': Encountered end of file
#Failed to git clone https://github.com/pyenv/pyenv-virtualenv.git
#pyenv: no such command `virtualenv-init'
#解决办法1： brew install pyenv-virtualenv 命令进行安装即可。
#解决方法2： git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

set_pyenv_conf(){
echo '正在设置pyenv'
cat >> $HOME/.bashrc << EOF
#PyenvConfig
export PATH="\$HOME/.pyenv/bin:\$PATH"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init - )"
EOF

source $HOME/.bashrc
echo -e 'pyenv设置完成\n'
}

install_python(){
echo '正在安装python 3.6'
if ! pyenv versions|grep 3.6.7 >/dev/null
then
    pyenv install -v 3.6.7
#    pyenv install 3.6.7
    echo -e 'python 3.6.7安装完成\n'
else
    echo -e 'Python 3.6.7已经存在\n'
fi
pyenv global 3.6.7
}


project_init(){
echo '正在设置项目环境'
proj='/opt/transparent/'
mkdir -p $proj/{backend,frontend,deployment,data,logs}

echo '创建python环境'
if [ ! -d $proj/.venv ]; then
    python -m venv $proj/.venv
fi
source $proj/.venv/bin/activate
pip install -U pip
if [ -f $proj/requirements.txt ]; then
    pip install -r $proj/requirements.txt
fi
deactivate

echo -e '项目创建完成\n'
}


install_all(){
system_update
install_software
install_nginx
install_redis
install_pyenv
set_pyenv_conf
install_python
project_init
}

cat << EOF 请输入执行编号:[1-9]
===============
[1] 更新系统
[2] 安装系统组件
[3] 安装Nginx
[4] 安装Redis
[5] 安装pyenv
[6] 设置pyenv环境
[7] 安装Python
[8] 初始化项目
[9] 全部执行
[q] 退出
===============
EOF

if [ -n $1]; then
  input=2
  #$1
  echo "执行操作：$1"
else
  read -p "请选择：" input
fi

case $input in
  1) system_update;;
  2) install_software;;
  3) install_nginx;;
  4) install_redis;;
  5) install_pyenv;;
  6) set_pyenv_conf;;
  7) install_python;;
  8) project_init;;
  9) install_all;;
  *) exit;;
esac