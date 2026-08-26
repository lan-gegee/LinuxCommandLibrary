# TAGLINE

校验 TeX Live 安装的完整性

# TLDR

**检查安装的所有方面**

```tlmgr check all```

**检查数据库中列出的文件是否都存在**

```tlmgr check files```

**检查缺失的依赖**

```tlmgr check depends```

**检查软件包之间运行文件的冲突**

```tlmgr check runfiles```

**检查 ls-R 文件的一致性**

```tlmgr check lsr```

**以详细输出运行检查**

```tlmgr -v check all```

# SYNOPSIS

**tlmgr check** [_what_] [_options_]

# PARAMETERS

**files**
> 检查本地 TLPDB 中列出的所有文件是否确实存在于磁盘上。

**depends**
> 列出作为已安装集合的依赖但自身未安装的软件包，以及不属于任何集合的软件包。

**executes**
> 检查 TeX Live 数据库中 execute 指令所引用的文件是否存在。

**runfiles**
> 列出在 runfiles 区段中出现多次的文件名（已知重复项除外）。

**lsr**
> 检查 ls-R 文件的一致性。在定义新目录树或修改 TEXMF 变量后很有用。

**all**
> 运行以上全部检查。

# DESCRIPTION

**tlmgr check** 校验 TeX Live 安装的一致性和完整性。如果没有发现问题，则没有任何输出。使用 `tlmgr -v check` 可获得详细输出，显示正在检查的内容。此操作不需要写权限，在用户模式和普通模式下行为相同。

# SEE ALSO

[tlmgr](/man/tlmgr)(1), [tlmgr-install](/man/tlmgr-install)(1), [tlmgr-update](/man/tlmgr-update)(1)
