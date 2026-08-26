# TAGLINE

显示 SELinux 安全上下文

# TLDR

获取**当前执行**环境的上下文

```secon```

获取某个**进程**的上下文

```secon --pid 1```

获取某个**文件**的上下文

```secon --file path/to/file```

获取**符号链接**的上下文（不解析）

```secon --link path/to/symlink```

**解析**上下文规范

```secon system_u:system_r:container_t:s0```

# SYNOPSIS

**secon** [_options_] [_context_]

# PARAMETERS

**--pid** _pid_
> 获取指定进程的上下文

**--file** _path_
> 获取文件的上下文（跟随符号链接）

**--link** _path_
> 获取符号链接的上下文（不跟随）

# DESCRIPTION

**secon** 检索并显示 SELinux 安全上下文。它可以显示当前执行环境、进程、文件的安全上下文，或解析上下文规范。

输出包含 SELinux 上下文的用户、角色、类型和级别组件。

# CAVEATS

需要启用 SELinux。文件上下文可能与实际访问时的上下文不同。

# HISTORY

属于 **libselinux-utils**，提供 SELinux 上下文检查工具。

# INSTALL

```apt: sudo apt install policycoreutils```

```dnf: sudo dnf install policycoreutils```

```zypper: sudo zypper install policycoreutils```

```nix: nix profile install nixpkgs#policycoreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[runcon](/man/runcon)(1), [chcon](/man/chcon)(1), [semanage](/man/semanage)(8)
