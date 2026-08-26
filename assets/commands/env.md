# TAGLINE

在修改过的环境变量下运行程序

# TLDR

**显示**所有环境变量

```env```

**在指定环境中运行**命令

```env VAR=value [command]```

**清空**环境

```env -i [command]```

**取消设置**变量

```env -u [VAR] [command]```

# SYNOPSIS

**env** [_options_] [_VAR=value_]... [_command_]

# DESCRIPTION

**env** 在修改后的环境中运行程序。它可以显示当前的环境变量、设置新变量、取消已有变量，或以干净的环境运行命令。

该命令适合临时设置变量或调试环境问题。

# PARAMETERS

**-i**, **--ignore-environment**
> 以空环境启动

**-u** _var_, **--unset=**_var_
> 从环境中移除变量

**-0**, **--null**
> 用 NUL 而非换行符结束各行

**-C** _dir_, **--chdir=**_dir_
> 运行命令前先切换目录

**-S** _string_
> 处理字符串并将其拆分为参数（在 shebang 行中很有用）

**-v**, **--verbose**
> 为每个处理步骤打印详细信息

# WORKFLOW

```bash
# Display all environment variables
env

# Set variable for one command
env DEBUG=1 ./program

# Multiple variables
env VAR1=value1 VAR2=value2 command

# Clear environment
env -i command

# Clean environment with specific variables
env -i PATH=/usr/bin HOME=/home/user command

# Unset variable
env -u DISPLAY command

# Change directory first
env -C /tmp ls

# In shebang for portability
#!/usr/bin/env python3
```

# COMMON USES

**Shebang 行：**
```bash
#!/usr/bin/env bash
#!/usr/bin/env python3
#!/usr/bin/env node
```

**临时变量：**
```bash
env NODE_ENV=production npm start
env DATABASE_URL=postgres://... rails console
```

**干净环境：**
```bash
env -i PATH="$PATH" command
```

**调试：**
```bash
env | grep PATH
env | sort
```

# VARIABLE FORMAT

变量显示形式如下：
```
NAME=value
PATH=/usr/bin:/bin
HOME=/home/user
```

# COMPARISON WITH EXPORT

**env**
> 在修改后的环境中运行命令

**export**
> 为当前 shell 及其子进程设置变量

```bash
# env (one command only)
env VAR=value command

# export (persistent)
export VAR=value
command  # VAR is available
```

# CAVEATS

用 env 设置的变量在命令退出后不会保留。shell 内建命令（如 `cd`、`alias`）无法通过 env 运行，因为 env 使用 `execvp`。使用 `-i` 时必须显式设置 PATH，否则找不到命令。包含空格的值需要加引号。`-C` 和 `-S` 是 GNU 扩展，并非所有平台都支持。

# HISTORY

**env** 自 Unix 早期便已存在，被纳入 POSIX 标准，用于环境操作。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils-env```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[export](/man/export)(1), [printenv](/man/printenv)(1), [set](/man/set)(1)
