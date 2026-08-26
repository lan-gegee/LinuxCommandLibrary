# TAGLINE

应用来自 Puppet 服务器的配置

# TLDR

**运行一次 agent**

```puppet agent --test```

**在前台运行**

```puppet agent --no-daemonize --verbose```

**试运行（noop）**

```puppet agent --test --noop```

**使用指定服务器运行**

```puppet agent --test --server [puppet.example.com]```

**启用 agent**

```puppet agent --enable```

**禁用 agent**

```puppet agent --disable "[reason]"```

# SYNOPSIS

**puppet agent** [_--test_] [_--noop_] [_--server host_] [_options_]

# PARAMETERS

**--test**
> 单次运行并输出结果。

**--noop**
> 试运行模式。

**--server** _HOST_
> Puppet 服务器。

**--no-daemonize**
> 在前台运行。

**--enable**
> 启用 agent 运行。

**--disable** _MSG_
> 禁用并附上消息。

**--verbose**
> 详细输出。

**--debug**
> 调试输出。

# DESCRIPTION

**puppet agent** 是 Puppet 配置管理系统的客户端组件。它连接到 Puppet 服务器，获取编译后的目标系统状态目录（catalog），并应用必要的变更使本机符合要求。agent 负责 SSL 证书管理、通过 Facter 提交系统信息（facts），以及详细报告所应用的变更。

在守护进程模式下，agent 作为后台服务运行，以可配置的间隔（通常为每 30 分钟）向服务器签到。对于手动操作，**--test** 执行一次带详细输出的单次运行，而 **--noop** 则预览将要进行的变更而不实际应用。可以使用锁消息临时禁用 agent，以防止在维护窗口期间运行。

# CONFIGURATION

**/etc/puppetlabs/puppet/puppet.conf**
> agent 配置，包括服务器主机名、运行间隔、环境、证书名称和 splay 设置。

**/etc/puppetlabs/puppet/ssl/**
> SSL 证书目录，包含 agent 的私钥、已签名的证书以及用于服务器身份验证的 CA 证书。

**/opt/puppetlabs/puppet/cache/state/agent_disabled.lock**
> agent 被禁用时创建的锁文件，以 JSON 格式包含禁用消息。

# CAVEATS

需要安装 Puppet。需要服务器或本地 manifests。需要 root 权限。

# HISTORY

**Puppet** 由 **Luke Kanies** 于 2005 年创建。agent 组件负责在整个基础设施中管理系统配置。

# INSTALL

```dnf: sudo dnf install puppet```

```pacman: sudo pacman -S puppet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[puppet](/man/puppet)(1), [facter](/man/facter)(1), [ansible](/man/ansible)(1)
