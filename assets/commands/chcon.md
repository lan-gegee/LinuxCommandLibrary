# TAGLINE

更改文件的 SELinux 安全上下文

# TLDR

查看文件的**安全上下文**

```ls -lZ path/to/file```

使用**参考文件**设置上下文

```chcon --reference reference_file target_file```

设置**完整上下文**

```chcon user:role:type:level filename```

仅更改 **user** 部分

```chcon -u user filename```

仅更改 **role** 部分

```chcon -r role filename```

仅更改 **type** 部分

```chcon -t type filename```

**递归**更改上下文

```chcon -R -t type path/to/directory```

# SYNOPSIS

**chcon** [_OPTION_]... _CONTEXT_ _FILE_...

**chcon** [_OPTION_]... [**-u** _USER_] [**-r** _ROLE_] [**-t** _TYPE_] [**-l** _RANGE_] _FILE_...

**chcon** [_OPTION_]... **--reference**=_RFILE_ _FILE_...

# DESCRIPTION

**chcon** 更改文件的 SELinux 安全上下文。SELinux 上下文由四个部分组成：user、role、type 和 range（级别）。上下文可以通过完整字符串指定，也可以按各个部分分别指定，或者从参考文件复制而来。

使用 chcon 所做的上下文更改是临时的，会在系统重新打标签或运行 restorecon 时被覆盖。要持久更改上下文，请使用 **semanage fcontext** 定义规则，并用 **restorecon** 应用它们。chcon 命令主要用于在进行永久更改之前测试和调试 SELinux 策略。

# PARAMETERS

**-u, --user=USER**
> 设置安全上下文的 user 部分

**-r, --role=ROLE**
> 设置安全上下文的 role 部分

**-t, --type=TYPE**
> 设置安全上下文的 type 部分

**-l, --range=RANGE**
> 设置安全上下文的 range/level 部分

**--reference=RFILE**
> 使用 RFILE 的安全上下文

**-R, --recursive**
> 递归地操作文件和目录

**-h, --no-dereference**
> 影响符号链接本身而非其所指向的文件

**--dereference**
> 影响符号链接指向的文件（非链接时的默认行为）

**-v, --verbose**
> 为每个处理的文件输出诊断信息

**--preserve-root**
> 拒绝在 / 上递归操作

**-H**
> 配合 -R 时，仅跟随命令行中的符号链接

**-L**
> 配合 -R 时，跟随所有符号链接

**-P**
> 配合 -R 时，绝不跟随符号链接（默认）

# CAVEATS

使用 chcon 所做的更改是临时的，可能会被 restorecon 或系统重新打标签重置。要进行永久更改，请使用 semanage fcontext 和 restorecon。必须启用 SELinux 此命令才能工作。

# HISTORY

**chcon** 是 GNU **coreutils** 的一部分，在启用了 SELinux 的系统上为文件提供 SELinux 安全上下文管理。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restorecon](/man/restorecon)(8), [semanage](/man/semanage)(8), [ls](/man/ls)(1), [secon](/man/secon)(1)

# RESOURCES

```[Source code](https://github.com/coreutils/coreutils)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html)```

<!-- verified: 2026-06-22 -->
