# TAGLINE

执行 Ansible playbook

# TLDR

**运行**一个 playbook

```ansible-playbook [playbook.yml]```

使用 **inventory 文件**运行

```ansible-playbook -i [inventory.ini] [playbook.yml]```

以 **sudo** 运行

```ansible-playbook [playbook.yml] --become --ask-become-pass```

**检查**模式（试运行）

```ansible-playbook [playbook.yml] --check```

运行指定的**标签**

```ansible-playbook [playbook.yml] --tags "[deploy,config]"```

传递**额外变量**

```ansible-playbook [playbook.yml] -e "env=production version=1.2.3"```

# SYNOPSIS

**ansible-playbook** [_-i inventory_] [_-e vars_] [_--tags tags_] [_options_] _playbook.yml_

# DESCRIPTION

**ansible-playbook** 执行 Ansible playbook，即定义自动化任务的 YAML 文件。Playbook 可以预置服务器、部署应用、配置服务，并编排复杂的多层部署。

与临时的 ansible 命令不同，playbook 通过变量、条件判断、循环和 handler 定义完整的自动化工作流。

# PARAMETERS

**-i** _inventory_, **--inventory** _inventory_
> Inventory 文件/路径或逗号分隔的主机列表

**-e** _vars_, **--extra-vars** _vars_
> 额外变量（key=value 形式、YAML/JSON 或 @file.yml）

**-t** _tags_, **--tags** _tags_
> 只运行带有这些标签的 play 和任务

**--skip-tags** _tags_
> 跳过标签匹配这些值的 play 和任务

**-b**, **--become**
> 以权限提升方式（become）运行

**-K**, **--ask-become-pass**
> 提示输入权限提升密码

**-C**, **--check**
> 试运行，不做任何更改

**-D**, **--diff**
> 显示被修改文件的差异（与 --check 配合使用）

**-l** _hosts_, **--limit** _hosts_
> 用额外的模式进一步限制所选主机

**--list-tasks**
> 列出将要执行的所有任务

**--list-tags**
> 列出所有可用标签

**-f** _forks_, **--forks** _forks_
> 并行进程数（默认：5）

**--start-at-task** _task_
> 从匹配该名称的任务开始执行 playbook

**--step**
> 在每个任务运行前进行确认

**--syntax-check**
> 检查 playbook 语法而不执行它

**--flush-cache**
> 清除 inventory 中每台主机的事实缓存

# CONFIGURATION

**/etc/ansible/ansible.cfg**
> 系统级 Ansible 配置，包含默认 inventory、forks 和连接设置。

**~/.ansible.cfg**
> 每用户 Ansible 配置，覆盖系统默认值。

**ansible.cfg**
> 当前目录中的项目级配置，优先级最高。

**/etc/ansible/hosts**
> 未指定 inventory 时使用的默认 inventory 文件。

# CAVEATS

Playbook 语法错误会立即失败；建议先用 --syntax-check。检查模式并非对所有模块都完美有效。请务必先在非生产环境中测试。

# HISTORY

自项目于 **2012 年**创立以来，**ansible-playbook** 一直是 Ansible 自动化的主要执行方式，支撑了基础设施即代码和声明式自动化。

# INSTALL

```dnf: sudo dnf install ansible-core```

```pacman: sudo pacman -S ansible-core```

```apk: sudo apk add ansible-core```

```zypper: sudo zypper install ansible-core```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ansible](/man/ansible)(1), [ansible-vault](/man/ansible-vault)(1), [ansible-lint](/man/ansible-lint)(1), [ansible-galaxy](/man/ansible-galaxy)(1)

# RESOURCES

```[Source code](https://github.com/ansible/ansible)```

```[Documentation](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html)```

<!-- verified: 2026-06-11 -->
