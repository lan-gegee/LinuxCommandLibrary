# TAGLINE

Concourse CI 系统的命令行界面

# TLDR

**设置构建目标**

```fly -t [target] set-pipeline```

**触发作业**

```fly -t [target] trigger-job -j [pipeline/job]```

**查看作业日志**

```fly -t [target] watch -j [pipeline/job]```

**登录 Concourse**

```fly -t [target] login -c [https://ci.example.com]```

**同步 fly 版本**

```fly -t [target] sync```

# SYNOPSIS

**fly** [_options_] _command_ [_arguments_]

# PARAMETERS

_COMMAND_
> 操作类型：login、set-pipeline、trigger-job、watch 等。

**-t**, **--target** _TARGET_
> 保存在 ~/.flyrc 中的 Concourse 目标名称。

**login**
> 向 Concourse 服务器进行身份验证（用 **-c** _url_ 指定 Concourse URL，**-n** _team_ 指定团队）。

**logout**
> 清除目标的已保存令牌。

**targets**
> 列出所有已配置的目标及其令牌过期时间。

**set-pipeline**
> 从 YAML 创建或更新流水线（**-p** _pipeline_ **-c** _config.yml_）。

**get-pipeline**
> 输出流水线当前的配置（**-p** _pipeline_）。

**destroy-pipeline**
> 移除流水线（**-p** _pipeline_）。

**unpause-pipeline**, **pause-pipeline**
> 启用或禁用流水线。

**trigger-job**
> 开始执行作业（**-j** _pipeline/job_）。

**watch**
> 流式查看某次构建的输出（**-j** _pipeline/job_ 或 **-b** _build_）。

**execute**
> 在本地运行一次性任务（**-c** _task.yml_）。

**sync**
> 更新本地 fly 二进制文件以匹配服务器版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fly** 是 Concourse CI 的命令行界面，Concourse CI 是一个基于容器的持续集成系统。它管理流水线、触发构建并与 Concourse 服务器交互。

该工具处理流水线配置、作业管理和构建监控。每个 Concourse 实例都注册为一个命名目标，便于在不同 CI 服务器之间切换。

fly 支持可脚本化的 CI/CD 工作流，并提供对构建日志和状态的实时访问。

# CAVEATS

版本必须与服务器匹配。目标需要定期重新认证。流水线的 YAML 语法比较特殊。

# HISTORY

fly 是 **Concourse CI** 的 CLI，由 Pivotal（现 VMware）创建。Concourse 开创了将 CI 流水线视为代码的做法，专注于容器和可复现性。

# INSTALL

```zypper: sudo zypper install fly```

```nix: nix profile install nixpkgs#fly```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[concourse](/man/concourse)(1), [jenkins](/man/jenkins)(1), [flyctl](/man/flyctl)(1)
