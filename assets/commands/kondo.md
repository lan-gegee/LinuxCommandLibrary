# TAGLINE

清理项目中的依赖和构建产物

# TLDR

**扫描当前目录**寻找可清理的项目

```kondo```

**扫描指定目录**

```kondo [path/to/directory]```

**扫描多个目录**

```kondo [path/to/dir1] [path/to/dir2]```

按一段时间内未被修改来**筛选项目**

```kondo -o [3months]```

# SYNOPSIS

**kondo** [_options_] [_directories_...]

# PARAMETERS

**-o**, **--older** _PERIOD_
> 只保留至少在指定时间段内未被修改的项目（如 3months、1year）。

**-a**, **--all**
> 清理所有找到的项目，不逐一询问。

**-f**, **--follow-symlinks**
> 扫描时跟随符号链接。

**-I**, **--ignored-dirs** _DIRS_
> 扫描时要忽略的目录。

# DESCRIPTION

**kondo** 是一款文件系统清理工具，它递归搜索目录中的已知项目结构，并计算移除依赖目录和构建产物目录可以节省多少空间。它支持 **20 多种项目类型**，包括 Cargo (Rust)、node_modules (JavaScript)、target (Java/Gradle)、__pycache__ (Python) 等。

发现可清理的项目后，kondo 会显示每个项目占用的空间，并询问是否删除这些产物。

# CAVEATS

Kondo 本质上是带确认提示的 **rm -rf**。使用前务必备份你的项目。被删除的构建产物需要重新下载或重新构建。

# HISTORY

**kondo** 由 **tbillington** 创建，使用 **Rust** 编写。其名字借用 Marie Kondo 的整理哲学，应用于开发者的项目目录。

# INSTALL

```pacman: sudo pacman -S kondo```

```brew: brew install kondo```

```nix: nix profile install nixpkgs#kondo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[du](/man/du)(1), [rm](/man/rm)(1), [ncdu](/man/ncdu)(1)
