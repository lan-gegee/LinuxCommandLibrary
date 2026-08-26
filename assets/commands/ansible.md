# TAGLINE

无代理的 IT 自动化与配置管理工具

# TLDR

**Ping** inventory 中的所有主机

```ansible all -m ping```

在主机上执行**命令**

```ansible [webservers] -a "uptime"```

以 **sudo** 执行

```ansible [webservers] -a "apt update" --become```

运行**临时模块**

```ansible [hosts] -m [apt] -a "name=nginx state=present" --become```

使用**指定的 inventory**

```ansible -i [inventory.ini] all -m ping```

# SYNOPSIS

**ansible** _pattern_ [_-m module_] [_-a args_] [_-i inventory_] [_options_]

# DESCRIPTION

**ansible** 是一款无代理的 IT 自动化工具，通过 SSH 在远程系统上执行任务。它采用推送模式，受管节点除 Python 和 SSH 访问外无需安装任何软件。

对于临时命令，ansible 会对匹配模式的主机执行模块。对于复杂的自动化，请配合 YAML playbook 使用 ansible-playbook。

# PARAMETERS

**-m** _module_, **--module-name** _module_
> 要执行的模块名称（默认：command）

**-a** _args_, **--args** _args_
> 模块参数，采用 key=value 或 JSON 形式

**-i** _inventory_, **--inventory** _inventory_
> Inventory 文件/路径或逗号分隔的主机列表

**-b**, **--become**
> 以权限提升方式（become）执行操作

**-K**, **--ask-become-pass**
> 提示输入权限提升密码

**-u** _user_, **--user** _user_
> 以该用户身份连接

**-k**, **--ask-pass**
> 提示输入 SSH 连接密码

**-f** _forks_, **--forks** _forks_
> 并行进程数（默认：5）

**-l** _pattern_, **--limit** _pattern_
> 用额外的模式进一步限制所选主机

**-v**, **-vvv**, **--verbose**
> 提高输出详细程度（重复使用可获得更多细节）

**-C**, **--check**
> 试运行；预测变更但不实际应用

**--diff**
> 显示被修改文件的差异（与 --check 配合使用）

**--list-hosts**
> 输出匹配主机的列表；不执行操作

# CONFIGURATION

**/etc/ansible/ansible.cfg**
> 系统级 Ansible 配置，包含默认模块路径、连接设置和权限提升配置。

**~/.ansible.cfg**
> 每用户 Ansible 配置，覆盖系统默认值。

**ansible.cfg**
> 当前目录中的项目级配置，优先级最高。

**/etc/ansible/hosts**
> 默认的 inventory 文件，列出受管主机和组。

# CAVEATS

受管节点上需要有 Python。建议使用基于 SSH 密钥的身份验证。Windows 主机需要使用 WinRM 而非 SSH。大型 inventory 建议改用 ansible-playbook。

# HISTORY

**Ansible** 由 Michael DeHaan 创建并于 **2012 年**发布。Red Hat 于 **2015 年**收购了 Ansible 公司。它已成为最受欢迎的配置管理与自动化工具之一。

# INSTALL

```dnf: sudo dnf install ansible-core```

```pacman: sudo pacman -S ansible-core```

```apk: sudo apk add ansible-core```

```zypper: sudo zypper install ansible-core```

```brew: brew install ansible```

```nix: nix profile install nixpkgs#ansible```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ansible-playbook](/man/ansible-playbook)(1), [ansible-inventory](/man/ansible-inventory)(1), [ansible-vault](/man/ansible-vault)(1), [ansible-doc](/man/ansible-doc)(1)

# RESOURCES

```[Source code](https://github.com/ansible/ansible)```

```[Documentation](https://docs.ansible.com/ansible/latest/cli/ansible.html)```

<!-- verified: 2026-06-11 -->
