# TAGLINE

恢复文件上的 SELinux 安全上下文

# TLDR

**恢复**文件或目录的安全上下文

```restorecon [path/to/file_or_directory]```

以详细输出**递归恢复**目录的安全上下文

```restorecon -R -v [path/to/directory]```

使用所有可用线程并显示进度地**递归恢复**安全上下文

```restorecon -R -T [0] -p [path/to/directory]```

**预览**标签更改而不实际应用

```restorecon -R -n -v [path/to/directory]```

# SYNOPSIS

**restorecon** [_options_] _pathname_...

# PARAMETERS

**-R**, **-r**
> 递归修改目录中的文件标签。

**-v**
> 显示文件标签的变化。

**-n**
> 不更改任何文件标签（试运行）。

**-p**
> 以 1k 块为单位打印文件数来显示进度。

**-F**
> 对可自定义文件强制将上下文重置为 file_context 的值。

**-e** _directory_
> 在递归操作中排除某个目录（可重复，需要完整路径）。

**-f** _infilename_
> 从 infilename 读取要处理的文件列表。用 **-** 表示 stdin。

**-T** _nthreads_
> 使用最多 nthreads 个线程进行并行处理。

**-i**
> 忽略不存在的文件。

**-x**
> 阻止 restorecon 跨越文件系统边界。

**-W**
> 显示关于没有匹配文件的条目的警告。

# DESCRIPTION

**restorecon** 根据 SELinux 文件上下文数据库中配置的持久规则，恢复文件和目录上的 SELinux 安全上下文。它通常在创建新文件后或文件上下文变得不正确时使用。

该工具在 **/etc/selinux/*/contexts/files/** 中查找正确的上下文并将其应用到指定文件。这对 SELinux 策略的正确执行至关重要。

# CAVEATS

仅在启用 SELinux 的系统上可用。更改文件上下文需要相应的权限。大型目录树可能耗时较长；使用 **-T** 进行并行处理。

# INSTALL

```apt: sudo apt install policycoreutils```

```dnf: sudo dnf install policycoreutils```

```zypper: sudo zypper install policycoreutils```

```nix: nix profile install nixpkgs#policycoreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[semanage-fcontext](/man/semanage-fcontext)(8), [chcon](/man/chcon)(1), [matchpathcon](/man/matchpathcon)(8), [setfiles](/man/setfiles)(8), [fixfiles](/man/fixfiles)(8), [getenforce](/man/getenforce)(8)
