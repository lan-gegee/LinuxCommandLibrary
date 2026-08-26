# TAGLINE

基于 Procfile 的应用的进程管理器

# TLDR

使用当前目录的 Procfile **启动**应用

```foreman start```

以**指定的 Procfile** 启动应用

```foreman start -f [Procfile]```

启动**特定**进程

```foreman start [process]```

**校验** Procfile 格式

```foreman check```

用该进程的环境变量运行**一次性命令**

```foreman run [command]```

启动所有进程，但**排除**名为 "worker" 的进程

```foreman start -m all=1,worker=0```

# SYNOPSIS

**foreman** _command_ [_options_]

# PARAMETERS

**start**
> 启动 Procfile 中定义的所有进程

**check**
> 校验 Procfile 格式

**run**
> 使用应用的环境运行一次性命令

**export**
> 将进程导出为其他格式（systemd、upstart 等）

**-f**, **--procfile** _FILE_
> 指定替代的 Procfile

**-d**, **--root** _DIR_
> 指定替代的应用根目录

**-e**, **--env** _FILE_
> 指定要加载的环境文件

**-m**, **--formation** _SPEC_
> 指定进程编组（如 web=2,worker=1）

**-p**, **--port** _PORT_
> 指定起始端口号

**-t**, **--timeout** _SECONDS_
> 指定关机超时时间

# CONFIGURATION

**Procfile**
> 以 name:command 行的形式定义进程类型（例如 web: python app.py）。

**.env**
> foreman 自动加载的环境变量。

# DESCRIPTION

**foreman** 是一个面向 Procfile 应用的进程管理器。它读取声明了组成应用的各个进程的 Procfile，并在开发环境中运行它们，让多进程管理变得简单。

Procfile 以 **name: command** 格式的行定义进程类型。例如：**web: python app.py** 和 **worker: python worker.py**。Foreman 启动所有已定义的进程并把它们的输出转发到终端。

Foreman 还会从 **.env** 文件加载环境变量，并可将进程定义导出为 systemd、upstart 或 launchd 等系统 init 格式以便生产部署。

# CAVEATS

foreman 主要为开发环境设计。生产环境请导出到合适的进程管理器。端口分配从 **-p** 的值开始按顺序递增，可能与现有服务冲突。

# HISTORY

foreman 由 David Dollar 于 **2011** 年在 Heroku 创建，用于在本地管理基于 Procfile 的应用。Procfile 格式成为十二要素（twelve-factor）应用中定义进程类型的标准，被许多 PaaS 提供商采用。

# INSTALL

```brew: brew install foreman```

```nix: nix profile install nixpkgs#foreman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pm2](/man/pm2)(1)
