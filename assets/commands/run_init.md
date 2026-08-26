# TAGLINE

在新建的 init 命名空间中执行程序

# TLDR

在 init 上下文中**运行**脚本

```sudo run_init path/to/script```

带**参数**运行脚本

```sudo run_init path/to/script start```

显式指定**上下文类型**

```sudo run_init -t context_type path/to/script```

**试运行**：只显示上下文而不执行

```sudo run_init -n path/to/script```

# SYNOPSIS

**run_init** [_options_] _script_ [_args_...]

# PARAMETERS

**-t**, **--type** _context_
> 显式指定 SELinux 上下文类型

**-n**, **--dry-run**
> 只显示上下文而不运行脚本

# DESCRIPTION

**run_init** 在正确的 SELinux 上下文中运行 init 脚本。它确保系统服务脚本以正确的 SELinux 域执行，以满足安全策略要求。

通常用于手动运行那些正常情况下由 init 系统启动的服务脚本。

# CAVEATS

需要启用 SELinux。用户必须拥有切换到 init 上下文的权限。

# HISTORY

属于 **policycoreutils** 软件包，提供用于正确处理上下文的 SELinux 管理工具。

# INSTALL

```apt: sudo apt install newrole```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[runcon](/man/runcon)(1), [semanage](/man/semanage)(8), [systemctl](/man/systemctl)(1)
