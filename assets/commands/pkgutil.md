# TAGLINE

查询和管理 macOS 软件包收据

# TLDR

**列出已安装的软件包**

```pkgutil --pkgs```

**显示软件包信息**

```pkgutil --pkg-info [com.apple.pkg.Safari]```

**列出软件包文件**

```pkgutil --files [com.apple.pkg.Safari]```

**查找文件属于哪个软件包**

```pkgutil --file-info [/usr/bin/python3]```

**遗忘软件包收据**（不会卸载文件）

```sudo pkgutil --forget [com.example.package]```

**展开软件包以便检查**

```pkgutil --expand [package.pkg] [expanded_dir]```

# SYNOPSIS

**pkgutil** [_options_] [_packages_]

# PARAMETERS

**--pkgs**
> 列出所有软件包。

**--pkg-info** _id_
> 显示软件包信息。

**--files** _id_
> 列出已安装的文件。

**--verify** _id_
> 验证软件包安装。

**--forget** _id_
> 移除软件包收据。

**--file-info** _path_
> 显示特定文件由哪个软件包安装。

**--only-files**
> 在 --files 输出中仅列出文件（不含目录）。

**--only-dirs**
> 在 --files 输出中仅列出目录（不含文件）。

**--regexp**
> 将 package-id 参数视为正则表达式进行匹配。

**--expand** _pkg_ _dir_
> 将扁平软件包展开到目录以便检查。

**--flatten** _pkg_ _dir_
> 将展开的软件包重新压平为扁平软件包。

**--bom** _path_
> 从扁平软件包中提取 BOM 文件。

**--volume** _path_
> 目标卷（默认：/）。

**-f**, **--force**
> 破坏性操作跳过确认。

**-v**, **--verbose**
> 人类可读的输出，附带额外上下文。

# DESCRIPTION

**pkgutil** 是 macOS 的软件包收据管理工具。它查询安装器数据库，可以列出已安装的软件包、显示软件包元数据、验证安装完整性，以及列出属于某软件包的文件。

**--forget** 命令从数据库中移除软件包收据而不删除任何已安装的文件，适合清理过期条目。**--expand** 命令解压 .pkg 归档以便检查。软件包标识符采用反向 DNS 记法（如 com.apple.pkg.Safari）。

注意 pkgutil 只管理收据——它无法安装或卸载软件包。安装请使用 **installer**，卸载则需手动移除。

# EXAMPLES

```bash
# List all Apple packages
pkgutil --pkgs | grep com.apple

# Get package details
pkgutil --pkg-info com.apple.pkg.Safari

# List package files
pkgutil --files com.apple.pkg.Safari | head

# Find package owning file
pkgutil --file-info /usr/bin/python3

# Expand pkg for inspection
pkgutil --expand package.pkg expanded_dir
```

# CAVEATS

仅适用于 macOS。--forget 不会卸载，只移除收据。部分软件包受系统保护。

# HISTORY

pkgutil 是 Apple 为 macOS 安装器软件包系统提供的命令行界面，用于管理 .pkg 安装。

# SEE ALSO

[brew](/man/brew)(1)
