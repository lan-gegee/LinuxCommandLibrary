# TAGLINE

Portage 系统维护工具

# TLDR

同步设为 **auto-sync** 的软件仓库

```sudo emaint sync [-a|--auto]```

同步**指定的**软件仓库

```sudo emaint sync [-r|--repo] [repository]```

同步**所有**软件仓库

```sudo emaint sync [-A|--allrepos]```

**清空** Portage 的续传列表

```sudo emaint cleanresume [-f|--fix]```

**清理** Portage 日志

```sudo emaint logs [-C|--clean]```

# SYNOPSIS

**emaint** _module_ [_options_]

# DESCRIPTION

**emaint** 在 Gentoo 系统上执行 Portage 维护任务。它按模块组织，每个模块负责一个方面：软件仓库同步、续传列表、日志轮转、二进制包主机，以及对 Portage 自身数据库的一致性检查。

大多数模块遵循相同的模式：**-c/--check** 只报告问题而不做任何改动，**-f/--fix** 则执行修复。运行 `emaint --help` 可列出当前安装的 Portage 版本所支持的模块。

**emaint sync** 是更新软件仓库的现代前端，能够理解 repos.conf 中针对每个仓库的设置，而 `emerge --sync` 出现得更早、不支持这些设置。

# PARAMETERS

**sync**
> 同步软件仓库

**-a, --auto**
> 仅同步启用了 auto-sync 的软件仓库

**-r, --repo** _name_
> 同步指定的软件仓库

**-A, --allrepos**
> 不管是否启用 auto-sync，同步所有软件仓库

**cleanresume**
> 清空 Portage 的续传列表（即 `emerge --resume` 会重放的内容）

**logs**
> 轮转并清理 Portage 日志目录

**merges**
> 检测并修复被中断的 emerge 留下的半完成合并的软件包

**binhost**
> 为二进制包主机重新生成 Packages 索引

**world**
> 检查并修复 world 文件中的无效条目

**-c, --check**
> 只报告问题，不做任何更改

**-C, --clean**
> 清理旧条目（logs 模块）

**-f, --fix**
> 执行修复

# CONFIGURATION

**/etc/portage/repos.conf**
> Portage 的软件仓库配置，控制哪些软件仓库会被同步。

# CAVEATS

Gentoo Linux 专属。需要 root 权限。属于 Portage 软件包管理系统的一部分。

# SEE ALSO

[emerge](/man/emerge)(1), [eselect](/man/eselect)(1), [eselect-repository](/man/eselect-repository)(1)

# RESOURCES

```[Source code](https://github.com/gentoo/portage)```

```[Documentation](https://wiki.gentoo.org/wiki/Portage)```

<!-- verified: 2026-07-14 -->
