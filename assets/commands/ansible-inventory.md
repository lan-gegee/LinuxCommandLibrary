# TAGLINE

显示 Ansible inventory 信息

# TLDR

**列出** inventory 中的所有主机

```ansible-inventory --list```

显示 inventory 的**图形**

```ansible-inventory --graph```

显示**主机详情**

```ansible-inventory --host [hostname]```

使用**指定的 inventory**

```ansible-inventory -i [inventory.ini] --list```

以 **YAML** 格式输出

```ansible-inventory --list --yaml```

列出匹配**组模式**的主机

```ansible-inventory --graph [webservers]```

将 inventory **导出**到文件

```ansible-inventory --list --export --output [inventory.json]```

以 **TOML** 格式显示 inventory

```ansible-inventory --list --toml```

# SYNOPSIS

**ansible-inventory** [_options_] [_-i inventory_] [_--list_|_--graph_|_--host host_] [_group_]

# DESCRIPTION

**ansible-inventory** 检查并显示 Ansible inventory 数据。它展示 Ansible 如何解析你的 inventory，包括动态 inventory、组成员关系和主机变量。

该工具可用于调试 inventory 配置，并了解 Ansible 实际使用的有效 inventory 结构。

# PARAMETERS

**--list**
> 以 JSON 格式输出所有主机

**--graph**
> 以树状图形式输出 inventory

**--host** _hostname_
> 输出指定主机的变量

**-i** _inventory_
> Inventory 来源

**--yaml**
> 以 YAML 格式输出

**--vars**
> 在输出中包含主机/组变量

**--export**
> 输出与 inventory 插件兼容的格式

**-y**
> YAML 输出（--yaml 的简写）

**--playbook-dir** _path_
> 设置用于相对路径的 playbook 目录

# CONFIGURATION

**/etc/ansible/hosts**
> 默认的 inventory 文件，列出受管主机和组。

**/etc/ansible/ansible.cfg**
> 系统级 Ansible 配置，包含默认 inventory 路径。

**~/.ansible.cfg**
> 每用户 Ansible 配置，覆盖系统默认值。

**ansible.cfg**
> 当前目录中的项目级配置，优先级最高。

# CAVEATS

动态 inventory 在此命令运行时才会求值。大型 inventory 可能产生大量输出。显示的变量是求值前的原始值（未经过 Jinja2 模板处理）。

# HISTORY

**ansible-inventory** 在 Ansible 2.4（**2017 年**）中引入，旨在提供更好的 inventory 检查能力，取代了以往临时调试 inventory 问题的方法。

# INSTALL

```dnf: sudo dnf install ansible-core```

```pacman: sudo pacman -S ansible-core```

```apk: sudo apk add ansible-core```

```zypper: sudo zypper install ansible-core```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ansible](/man/ansible)(1), [ansible-playbook](/man/ansible-playbook)(1)
