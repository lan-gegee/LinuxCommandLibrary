# TAGLINE

在本地应用 Puppet manifests

# TLDR

**应用 manifest**

```puppet apply [manifest.pp]```

**试运行而不做更改**

```puppet apply --noop [manifest.pp]```

**以详细输出应用**

```puppet apply --verbose [manifest.pp]```

**以完整调试输出应用**

```puppet apply --debug [manifest.pp]```

**执行内联 Puppet 代码**

```puppet apply -e "package { 'nginx': ensure => present }"```

**带常用测试选项应用**（verbose、detailed-exitcodes、show_diff）

```puppet apply --test [manifest.pp]```

**将日志输出到文件**

```puppet apply --logdest [/var/log/puppet.log] [manifest.pp]```

# SYNOPSIS

**puppet apply** [_options_] _manifest_

# PARAMETERS

_MANIFEST_
> 要编译并应用的 Puppet manifest 文件。

**--noop**
> 试运行模式；显示将要进行的变更而不实际应用。

**-v**, **--verbose**
> 在执行期间打印额外信息。

**-d**, **--debug**
> 启用完整的调试输出。

**-e**, **--execute** _CODE_
> 执行一段指定的 Puppet 代码而不是 manifest 文件。

**--test**
> 启用常用测试选项：verbose、detailed-exitcodes 和 show_diff。

**--detailed-exitcodes**
> 通过退出码提供额外信息（0=无变更，2=已应用变更，4=有失败，6=两者兼有）。

**-l**, **--logdest** _DEST_
> 日志消息的发送位置（syslog、eventlog、console 或文件路径）。默认为 console。

**--catalog** _CATALOG_
> 应用 JSON catalog 而不是编译 manifest。接受文件路径或 stdin。

**-L**, **--loadclasses**
> 从 classfile 加载所有已存储的类。

**--modulepath** _PATH_
> 用于解析类和自定义类型的模块搜索路径。

# DESCRIPTION

**puppet apply** 直接在本地系统上执行 Puppet manifests，无需 Puppet 服务器。它编译并应用指定的 manifest 文件，非常适合独立的配置管理、开发期间的 manifest 测试，以及系统加入 Puppet 基础设施之前的引导初始化。

该命令接受用 Puppet 声明式 DSL 编写的 manifest 文件，也可通过 **-e** 选项接受内联代码。它支持 **--noop** 进行变更的干运行预览，支持 **--verbose** 和 **--debug** 获得详细的执行输出，并支持 **--modulepath** 指定查找 Puppet 模块的位置。由于独立于服务器运行，puppet apply 常用于容器镜像构建、Vagrant 置备以及一次性的系统配置任务。

# CONFIGURATION

**/etc/puppetlabs/puppet/puppet.conf**
> 配置文件，控制模块路径、日志级别、环境设置以及其他影响本地 apply 运行的 Puppet 行为。

**/etc/puppetlabs/code/modules/**
> 默认模块路径，在解析 manifests 中引用的类和自定义类型时搜索该目录。

# CAVEATS

需要安装 Puppet。在没有 Puppet 服务器的模式下运行（masterless 模式）。管理系统资源时必须以 root 运行。

# HISTORY

puppet apply 提供 **Puppet 本地**manifest 执行能力。

# INSTALL

```dnf: sudo dnf install puppet```

```pacman: sudo pacman -S puppet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[puppet](/man/puppet)(1), [puppet-agent](/man/puppet-agent)(1)
