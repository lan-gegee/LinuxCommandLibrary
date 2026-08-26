# TAGLINE

执行 System V 风格 init 脚本动作

# TLDR

**启动服务**

```sudo invoke-rc.d [service] start```

**停止服务**

```sudo invoke-rc.d [service] stop```

**重启服务**

```sudo invoke-rc.d [service] restart```

**检查服务状态**

```invoke-rc.d [service] status```

**重新加载服务配置**

```sudo invoke-rc.d [service] reload```

**查询策略层是否允许某动作**

```invoke-rc.d --query [service] start```

# SYNOPSIS

**invoke-rc.d** [_--quiet_] [_--force_] [_--try-anyway_] [_--disclose-deny_] [_--query_] [_--no-fallback_] _name_ _action_ [_init script parameters..._]

# PARAMETERS

_NAME_
> /etc/init.d/ 中 init 脚本的名称。

_ACTION_
> 要执行的动作：start、stop、restart、reload、force-reload、force-stop、try-restart 或 status。

**--quiet**
> 抑制警告和信息性消息。

**--force**
> 无论策略和 init 脚本子系统错误如何都尝试运行 init 脚本。不建议在维护者脚本中使用。

**--try-anyway**
> 检测到非致命错误时仍尝试运行 init 脚本。

**--disclose-deny**
> 当动作被策略层拒绝时返回状态码 101 而不是 0。

**--query**
> 查询将采取什么动作而不实际执行。返回状态码 100-106。隐含 --disclose-deny 和 --no-fallback。

**--no-fallback**
> 忽略策略层的任何回退动作请求。

**--help**
> 显示帮助信息。

# DESCRIPTION

**invoke-rc.d** 在基于 Debian 的系统上执行 System V 风格的 init 脚本动作。它提供一个标准接口，会遵循运行级别约束以及系统管理员通过 policy-rc.d 设置的本地策略。

该工具在执行动作前会检查 /usr/sbin/policy-rc.d。它是在软件包维护者脚本中控制服务的推荐方式，因为它能正确处理可能存在的策略限制（例如 chroot 环境或容器中）。

# CAVEATS

Debian/Ubuntu 特有。在 systemd 系统上，invoke-rc.d 会重定向到 systemctl。policy-rc.d 机制允许管理员阻止服务动作，这在 Docker 容器中很常用，可防止软件包安装期间启动服务。

# HISTORY

invoke-rc.d 是为 **Debian** 创建的，用于提供符合策略的 init 脚本调用方式，尤其是在软件包维护者脚本中。

# INSTALL

```apt: sudo apt install runit-init```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[service](/man/service)(8), [systemctl](/man/systemctl)(1), [update-rc.d](/man/update-rc.d)(8)
