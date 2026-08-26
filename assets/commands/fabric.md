# TAGLINE

Python SSH 自动化与部署工具

# TLDR

在远程主机上执行 shell 命令

```fab -H [host] -- [command]```

运行 fabfile.py 中定义的任务

```fab [taskname]```

在指定主机上运行任务

```fab -H [user@host] [taskname]```

列出所有可用任务

```fab --list```

使用指定 SSH 密钥运行任务

```fab -i [~/.ssh/key] -H [host] [taskname]```

显示指定任务的详细帮助

```fab -d [taskname]```

# SYNOPSIS

**fab** [_options_] [_task_[:_arg_,...]]...

# PARAMETERS

**-H**, **--hosts** _hosts_
> 以逗号分隔的主机列表。

**-i** _key_
> SSH 身份认证文件。

**-u**, **--user** _user_
> SSH 用户名。

**-l**, **--list**
> 列出可用任务。

**-p**, **--password**
> 提示输入 SSH 密码。

**-d** _task_
> 显示任务的 docstring。

**--** _command_
> 直接运行 shell 命令。

**-c**, **--config** _file_
> 配置文件路径。

**-r**, **--roles** _roles_
> 要操作的角色。

# DESCRIPTION

**Fabric** 是一个 Python 库和命令行工具，用于通过 SSH 在远程服务器上执行 shell 命令。它简化了部署、系统管理和自动化任务。

任务用 Python 定义在 **fabfile.py** 中。Fabric 2.x 提供了比 1.x 更简洁的 API，包含 Connection 对象和更简单的 task 装饰器。

# FABFILE EXAMPLE

```python
from fabric import task

@task
def deploy(c):
    c.run("git pull")
    c.run("pip install -r requirements.txt")
    c.run("systemctl restart myapp")

@task
def uptime(c):
    c.run("uptime")
```

# CAVEATS

2.x 版本与 1.x 有显著差异。需要 SSH 访问权限。Fabric 2+ 需要 Python 3。复杂的部署可考虑 Ansible 或类似工具。

# HISTORY

Fabric 由 **Jeff Forcier** 于 **2009 年**创建，作为 Python 部署场景下 Capistrano 的更简替代方案。**2018 年**发布的 2.0 版本是一次彻底重写，API 全面现代化。

# INSTALL

```pacman: sudo pacman -S fabric```

```brew: brew install fabric```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ansible](/man/ansible)(1), [ssh](/man/ssh)(1)
