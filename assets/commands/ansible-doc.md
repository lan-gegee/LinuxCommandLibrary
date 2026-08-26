# TAGLINE

显示 Ansible 模块和插件的文档

# TLDR

**查看**某个模块的文档

```ansible-doc [apt]```

**列出**所有可用模块

```ansible-doc -l```

列出匹配**模式**的模块

```ansible-doc -l | grep [docker]```

显示模块用法的**代码片段**

```ansible-doc -s [yum]```

显示 **collection** 模块的文档

```ansible-doc [community.docker.docker_container]```

列出某类**插件**

```ansible-doc -t [callback] -l```

# SYNOPSIS

**ansible-doc** [_-l_] [_-s_] [_-t type_] [_module_]

# DESCRIPTION

**ansible-doc** 显示 Ansible 模块、插件和 collection 的文档。它会展示模块参数、返回值、示例和注意事项，可作为快速参考，无需访问在线文档。

该工具可以列出所有可用模块并按插件类型过滤，有助于发现可用的自动化选项。

# PARAMETERS

**-l** [_filter_], **--list** [_filter_]
> 列出可用插件；可选过滤器可以是命名空间或 collection 名称

**-s**, **--snippet**
> 显示 playbook 片段（适用于 inventory、lookup 和 module 插件类型）

**-t** _type_, **--type** _type_
> 要查询的插件类型（默认：module）。可选值包括 module、become、cache、callback、cliconf、connection、httpapi、inventory、lookup、netconf、shell、vars、strategy、test、filter、role、keyword

**-F**, **--list_files**
> 显示插件名称及其源文件（隐含 --list）

**-e** _entry_point_, **--entry-point** _entry_point_
> 选择 role 的入口点（配合 -t role 使用）

**-j**, **--json**
> 将输出改为 JSON 格式

**-M** _path_, **--module-path** _path_
> 将冒号分隔的路径添加到模块库搜索路径之前

# CONFIGURATION

**ansible.cfg**
> Ansible 主配置文件，按当前目录、~/.ansible.cfg、/etc/ansible/ansible.cfg 的顺序查找。

**ANSIBLE_CONFIG**
> 用于指定替代配置文件路径的环境变量。

# CAVEATS

核心模块与社区模块的文档质量参差不齐。某些模块的文档可能已过时。collection 模块使用完全限定名称。

# HISTORY

自早期版本起，**ansible-doc** 就是 Ansible 的一部分，提供对模块文档的离线访问。collection 支持随 Ansible 2.9 于 **2019** 年加入。

# INSTALL

```dnf: sudo dnf install ansible-core```

```pacman: sudo pacman -S ansible-core```

```apk: sudo apk add ansible-core```

```zypper: sudo zypper install ansible-core```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ansible](/man/ansible)(1), [ansible-galaxy](/man/ansible-galaxy)(1), [ansible-playbook](/man/ansible-playbook)(1)

# RESOURCES

```[Source code](https://github.com/ansible/ansible)```

```[Documentation](https://docs.ansible.com/ansible/latest/cli/ansible-doc.html)```

<!-- verified: 2026-06-11 -->
