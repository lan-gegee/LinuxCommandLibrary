# TAGLINE

根据策略设置 SELinux 文件安全上下文

# TLDR

按**默认策略**设置文件上下文

```sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts [path/to/directory]```

以**递归**方式设置文件上下文并显示变更

```sudo setfiles -v /etc/selinux/targeted/contexts/files/file_contexts [path/to/directory]```

**预览**变更而不实际修改上下文

```sudo setfiles -n /etc/selinux/targeted/contexts/files/file_contexts [path/to/directory]```

**强制**完整替换上下文

```sudo setfiles -F /etc/selinux/targeted/contexts/files/file_contexts [path/to/directory]```

使用**多线程**加快处理速度

```sudo setfiles -T 4 /etc/selinux/targeted/contexts/files/file_contexts [path/to/directory]```

在重新打标时**排除**某个目录

```sudo setfiles -e [path/to/exclude] /etc/selinux/targeted/contexts/files/file_contexts [path/to/directory]```

# SYNOPSIS

**setfiles** [**-cdlmnpsvFIUW**] [**-e** _dir_] [**-r** _rootpath_] [**-T** _nthreads_] _spec_file_ _pathname_...

# PARAMETERS

**-c** _policy_
> 针对指定的二进制策略文件校验上下文

**-d**
> 显示每个文件匹配到哪条规范（调试）

**-e** _directory_
> 将目录排除在打标之外（可重复）

**-f** _infilename_
> 从文件中读取要处理的文件列表

**-F**
> 强制完整替换上下文，包括 user、role 和 range

**-n**
> 试运行；显示将要更改的内容但不实际修改

**-p**
> 以百分比或 1024 块为增量显示进度

**-r** _rootpath_
> 使用备用根路径进行上下文匹配

**-s**
> 将变更记录到 syslog 而非 stdout

**-v**
> 详细输出；显示标签被更改的文件

**-T** _nthreads_
> 使用的线程数（0 = CPU 核心数）

**-I**
> 忽略已存储的目录摘要；强制检查标签

**-D**
> 在扩展属性中设置或更新目录 SHA1 摘要

**-W**
> 显示关于没有匹配规范的条目的警告

**-l**
> 每 10 秒将变更记录一次到 SETFILES_PROGRESS 环境变量指定的文件

# DESCRIPTION

**setfiles** 根据规范文件中的模式到上下文映射，初始化并修正文件系统上的 SELinux 安全上下文标签。它是在 SELinux 策略变更或系统安装后对文件重新打标的主要工具。

规范文件（通常为 **/etc/selinux/targeted/contexts/files/file_contexts**）包含与文件路径匹配的正则表达式，用于确定合适的安全上下文。与 **restorecon** 不同，setfiles 需要显式提供规范文件参数。

# CAVEATS

需要启用 SELinux；在非 SELinux 系统上该命令无效。对大型文件系统重新打标可能耗时较长。使用 **-F** 会强制更改所有上下文组件，可能干扰正在运行的服务。在生产系统上应先使用 **-n** 试运行选项。

# HISTORY

**setfiles** 是 SELinux **policycoreutils** 软件包的一部分，自 **2000** 年起由 **NSA**（国家安全局）与 SELinux 一同开发。SELinux 于 **2003** 年随内核版本 **2.6** 合入 Linux 内核主线。该工具已逐步支持多线程和基于摘要的优化。

# INSTALL

```apt: sudo apt install policycoreutils```

```dnf: sudo dnf install policycoreutils```

```zypper: sudo zypper install policycoreutils```

```nix: nix profile install nixpkgs#policycoreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restorecon](/man/restorecon)(8), [fixfiles](/man/fixfiles)(8), [semanage](/man/semanage)(8), [semanage-fcontext](/man/semanage-fcontext)(8), [chcon](/man/chcon)(1), [getenforce](/man/getenforce)(8), [sestatus](/man/sestatus)(8)
