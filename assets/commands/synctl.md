# TAGLINE

Matrix Synapse 主服务器控制接口

# TLDR

**启动 Synapse 服务器**

```synctl start```

**停止 Synapse 服务器**

```synctl stop```

**重启 Synapse 服务器**

```synctl restart```

**使用指定的配置文件启动**

```synctl start [/path/to/homeserver.yaml]```

**启动特定的 worker**

```synctl start -w [/path/to/worker.yaml]```

**重启所有 worker 和主进程**

```synctl restart -a [/path/to/workers/]```

# SYNOPSIS

**synctl** {start|stop|restart} [_configfile_] [_options_]

# PARAMETERS

**start**
> 启动 Synapse 服务器或 worker。

**stop**
> 停止 Synapse 服务器或 worker。

**restart**
> 重启 Synapse 服务器或 worker。

_configfile_
> 配置文件路径（默认：homeserver.yaml）。

**-w**, **--worker** _file_
> 使用指定的配置文件操作单个 worker。

**-a**, **--all-processes** _dir_
> 操作目录中的所有 worker 和主进程。

# DESCRIPTION

**synctl** 是 Matrix Synapse 的控制接口。Synapse 是 Matrix 通信协议的参考主服务器实现。synctl 负责管理 Synapse 服务器及其 worker 进程的启动、停止和重启。

对于单实例部署，synctl 操作主 homeserver 进程。对于使用 worker 的扩展部署，-a 选项可管理配置目录中定义的所有 worker 进程。

配置文件采用 YAML 格式，定义服务器设置、数据库连接、联邦参数和资源限制。

# ENVIRONMENT

**SYNAPSE_CACHE_FACTOR**
: 控制内存缓存大小。默认为 0.5。降低该值可减少内存占用，提高该值可获得更好性能。

# CAVEATS

配置文件必须存在且为有效的 YAML。使用 worker 时，每个 worker 需要自己的配置文件。内存占用可能较大，请相应调整 SYNAPSE_CACHE_FACTOR。需要 Python 3 及已安装的依赖。

# HISTORY

**Synapse** 由 Element（前身为 New Vector）开发，是 Matrix 协议的参考实现。Matrix 是一个用于去中心化实时通信的开放标准。Synapse 于 2014 年首次发布，至今仍是部署最广泛的 Matrix 主服务器。

# INSTALL

```dnf: sudo dnf install synapse```

```pacman: sudo pacman -S synapse```

```apk: sudo apk add synapse```

```nix: nix profile install nixpkgs#synapse```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[register_new_matrix_user](/man/register_new_matrix_user)(1), [systemctl](/man/systemctl)(1)
