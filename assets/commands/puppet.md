# TAGLINE

声明式配置管理工具

# TLDR

**在本地应用 manifest**

```puppet apply [manifest.pp]```

**检查 manifest 语法**

```puppet parser validate [manifest.pp]```

**以测试模式运行 puppet agent**

```puppet agent --test```

**以干运行模式运行 puppet agent**

```puppet agent --test --noop```

**列出可用模块**

```puppet module list```

**从 Puppet Forge 安装模块**

```puppet module install [author-module]```

**检查系统上的资源**

```puppet resource [user] [root]```

**查看或设置配置值**

```puppet config print [server]```

# SYNOPSIS

**puppet** _subcommand_ [_options_]

# PARAMETERS

**apply**
> 在本地编译并应用 Puppet manifest。

**agent**
> 从 Puppet 服务器请求 catalog 并执行。

**parser**
> 校验 Puppet manifest 语法。

**module**
> 安装、列出、升级和管理 Puppet 模块。

**resource**
> 检查和操作系统上的资源。

**config**
> 查看和修改 Puppet 配置设置。

**ssl**
> 管理 SSL 密钥和证书。

**help**
> 显示子命令的帮助信息。

**--test**
> 以前台方式运行一次 agent 并输出详细信息。

**--noop**
> 模拟变更而不实际应用（干运行）。

**--verbose**
> 启用详细日志。

**--debug**
> 启用完整的调试日志。

**--environment** _env_
> 选择指定的 Puppet 环境。

# DESCRIPTION

**puppet** 是一个配置管理工具，使用声明式语言自动化基础设施的预置和管理。管理员通过用 Puppet 的 DSL 编写的 manifests 描述系统的期望状态，该工具通过安装软件包、管理文件、配置服务和管理用户来确保机器收敛到该状态。

Puppet 有两种运行模式：客户端-服务器架构（agent 从 Puppet 服务器拉取 catalog），以及使用 **puppet apply** 在本地执行 manifest 的独立模式。资源抽象层自动处理平台差异，因此同一份 manifest 无需修改即可管理 Debian、Red Hat 及其他发行版上的软件包。

其生态系统包括用于通过 Puppet Forge 共享可复用配置代码的模块系统、收集系统信息的 Facter，以及将数据与代码分离的 Hiera。Puppet 支持多环境以便在生产上线前测试变更，并提供关于配置漂移和强制操作的详细报告。

# CONFIGURATION

**/etc/puppetlabs/puppet/puppet.conf**
> 主配置文件，控制服务器地址、环境、运行间隔、证书设置和模块路径。

**/etc/puppetlabs/code/environments/production/manifests/**
> 生产环境中定义节点配置的站点 manifests 的默认位置。

**/etc/puppetlabs/code/environments/production/modules/**
> 模块目录，包含带有类、自定义类型和模板的可复用 Puppet 模块。

**FACTERLIB**
> 环境变量，指定搜索自定义 Facter facts 的额外目录。

# CAVEATS

需要安装 Puppet。支持主从（master-agent）或独立模式。**--test** 标志组合了 --onetime、--verbose、--no-daemonize，并在失败时返回非零退出码。

# HISTORY

Puppet 由 **Puppet Labs**（现为 Perforce）创建，用于 IT 自动化。

# INSTALL

```dnf: sudo dnf install puppet```

```pacman: sudo pacman -S puppet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[puppet-apply](/man/puppet-apply)(1), [puppet-agent](/man/puppet-agent)(1), [ansible](/man/ansible)(1), [chef](/man/chef)(1)
