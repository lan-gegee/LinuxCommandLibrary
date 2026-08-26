# TAGLINE

从 Galaxy 管理 Ansible role 和 collection

# TLDR

从 Galaxy **安装**一个 role

```ansible-galaxy install [username.role_name]```

从 Galaxy 安装 **collection**

```ansible-galaxy collection install [community.docker]```

从 **requirements 文件**安装

```ansible-galaxy install -r [requirements.yml]```

**列出**已安装的 role

```ansible-galaxy list```

**初始化**新 role

```ansible-galaxy init [role_name]```

**搜索** role

```ansible-galaxy search [nginx]```

# SYNOPSIS

**ansible-galaxy** [_role_|_collection_] _command_ [_options_]

# DESCRIPTION

**ansible-galaxy** 管理来自 Ansible Galaxy 及其他来源的 Ansible role 和 collection。Galaxy 是社区贡献内容的公共仓库，提供可复用的自动化组件。

该工具可以安装、创建和管理 role（传统内容）以及 collection（打包内容，包括模块、插件和 role）。子命令按内容类型分组为 **ansible-galaxy role** _command_ 和 **ansible-galaxy collection** _command_；如果省略类型，则默认为 role（例如 "ansible-galaxy install" 等价于 "ansible-galaxy role install"）。

# PARAMETERS

**install** _name_
> 安装一个 role（安装 collection 则使用 "collection install"）

**init** _name_
> 创建新的 role 或 collection 脚手架

**list**
> 列出已安装的 role 或 collection

**search** _query_
> 在 Galaxy 中搜索 role

**info** _name_
> 显示某个 role 或 collection 的详细信息

**remove** _name_
> 移除已安装的 role 或 collection

**build**
> 构建 collection 归档产物（仅限 collection）

**publish** _tarball_
> 将 collection 发布到 Galaxy 服务器（仅限 collection）

**-r** _file_, **--role-file** _file_, **--requirements-file** _file_
> 按 YAML requirements 文件中的清单安装

**-p** _path_, **--roles-path** _path_
> role 的安装路径（collection 使用 --collections-path）

**--force**
> 强制覆盖已存在的 role 或 collection

**-s** _server_, **--server** _server_
> Galaxy API 服务器 URL

**--offline**
> 离线工作（init/install/verify，仅使用已安装的内容）

# CONFIGURATION

**/etc/ansible/ansible.cfg**
> 系统级 Ansible 配置，包括 Galaxy 服务器 URL 和 role 路径。

**~/.ansible.cfg**
> 每用户 Ansible 配置，覆盖系统默认值。

**ansible.cfg**
> 当前目录中的项目级配置，优先级最高。

# CAVEATS

Galaxy 内容由社区维护；在生产环境使用前请先行审查。collection 名称带命名空间（namespace.collection）。role 和 collection 的安装路径不同。

# HISTORY

**ansible-galaxy** 随 Ansible Galaxy 于 **2013** 年推出，用于分享和分发 role。collection 支持于 Ansible 2.9（**2019** 年）加入，成为一种新的内容分发格式。

# INSTALL

```dnf: sudo dnf install ansible-core```

```pacman: sudo pacman -S ansible-core```

```apk: sudo apk add ansible-core```

```zypper: sudo zypper install ansible-core```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ansible](/man/ansible)(1), [ansible-playbook](/man/ansible-playbook)(1), [ansible-doc](/man/ansible-doc)(1)

# RESOURCES

```[Source code](https://github.com/ansible/ansible)```

```[Documentation](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html)```

<!-- verified: 2026-06-11 -->
