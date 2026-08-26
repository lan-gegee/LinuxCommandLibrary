# TAGLINE

KeePassXC 密码管理器的命令行界面

# TLDR

**列出数据库中的条目**

```keepassxc-cli ls [database.kdbx]```

**显示条目详情**

```keepassxc-cli show [database.kdbx] [entry]```

**复制密码到剪贴板**

```keepassxc-cli clip [database.kdbx] [entry]```

**添加新条目**

```keepassxc-cli add [database.kdbx] [entry]```

**生成密码**

```keepassxc-cli generate -L [20]```

**创建新数据库**

```keepassxc-cli db-create [database.kdbx]```

**搜索条目**

```keepassxc-cli search [database.kdbx] [query]```

# SYNOPSIS

**keepassxc-cli** _command_ [_options_]

# PARAMETERS

## 通用选项

**-k**, **--key-file** _path_
> 指定用于解锁数据库的密钥文件路径。

**--no-password**
> 停用数据库的密码密钥。

**-q**, **--quiet**
> 静默密码提示和其他次要输出。

## 命令

**ls** _database_ [_group_]
> 列出数据库或组中的条目。使用 **-R** 进行递归列出。

**show** _database_ _entry_
> 显示条目详情。使用 **-a** 选择特定属性。

**clip** _database_ _entry_ [_timeout_]
> 复制密码到剪贴板。超时后清除（默认 10 秒）。

**add** _database_ _entry_
> 添加新条目。使用 **-g** 生成密码，**-u** 设置用户名。

**edit** _database_ _entry_
> 编辑已有条目。

**rm** _database_ _entry_
> 移除条目。

**generate**
> 生成随机密码。使用 **-L** 设置长度（默认 16）。

**db-create** _database_
> 创建新数据库。

**search** _database_ _term_
> 搜索条目。

**analyze** _database_
> 分析密码强度。

**merge** _database1_ _database2_
> 合并两个数据库。第一个数据库会被结果覆盖。

**import** _database_ _xml_
> 将 XML 导出的内容导入新数据库。

**export** _database_
> 将数据库内容导出到 stdout（xml 或 csv 格式）。

**open** _database_
> 以交互式 shell 模式打开数据库。

**attachment-export** _database_ _entry_ _name_ _export-file_
> 将附件导出到文件。

**attachment-import** _database_ _entry_ _name_ _import-file_
> 将文件作为附件导入条目。

# DESCRIPTION

**keepassxc-cli** 是 KeePassXC 密码管理器的命令行界面。它允许从终端查询和修改 KeePass 数据库条目（.kdbx 格式）。支持密码生成、剪贴板操作和数据库管理。

# CAVEATS

在共享系统上避免使用 --password。在 CLI 编辑前请先关闭 GUI，以防数据库损坏。

# INSTALL

```apt: sudo apt install keepassxc-full```

```dnf: sudo dnf install keepassxc```

```pacman: sudo pacman -S keepassxc```

```apk: sudo apk add keepassxc```

```zypper: sudo zypper install keepassxc```

```nix: nix profile install nixpkgs#keepassxc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1)
