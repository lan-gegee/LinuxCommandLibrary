# TAGLINE

GNOME 配置数据库管理工具

# TLDR

**读取**某个键的值

```dconf read /[path/to/key]```

**列出**子目录和键

```dconf list /[path/to/directory]/```

**写入**某个键的值

```dconf write /[path/to/key] "[value]"```

**将键重置**为默认值

```dconf reset /[path/to/key]```

**监视**更改

```dconf watch /[path/to/key]```

**以 INI 格式导出**目录

```dconf dump /[path/to/directory]/```

# SYNOPSIS

**dconf** _command_ [_arguments_]

# DESCRIPTION

**dconf** 是 GNOME 和 GTK 应用程序的底层配置系统。它提供一个简单的键值数据库，按类似文件系统的层级结构组织，并以二进制格式存储设置以便快速读取。

数据库采用基于路径的键结构（如 /org/gnome/desktop/interface/font-name），值以 GVariant 格式存储，支持带类型的数据，包括字符串、整数、布尔和数组。写入 dconf 的更改对正在监视该数据库的运行中应用程序立即生效。

对大多数用户而言，gsettings 提供了更高层、经 schema 校验的接口。dconf 适用于批量操作、通过脚本修改配置，以及使用 dump 和 load 命令进行备份/恢复。对管理多台 GNOME 系统或创建配置档案的系统管理员来说尤其有用。

# PARAMETERS

**read** _key_
> 读取键值

**write** _key_ _value_
> 写入键值

**reset** _key_
> 将键重置为默认值

**list** _dir_
> 列出键和子目录

**watch** _path_
> 监视更改

**dump** _dir_
> 以 INI 格式导出目录

**load** _dir_
> 从 INI 格式导入

**update**
> 根据 /etc/dconf/db 中的 keyfile 编译系统 dconf 数据库（编辑后需以 root 运行）

# CONFIGURATION

**~/.config/dconf/user**
> 存储用户 GNOME 和 GTK 应用程序配置值的二进制数据库文件。

# CAVEATS

值必须为 GVariant 格式。字符串需要在双引号内加单引号。更改立即生效。需要 schema 校验的设置请优先使用 gsettings。

# INSTALL

```apt: sudo apt install dconf-cli```

```dnf: sudo dnf install dconf```

```pacman: sudo pacman -S dconf```

```apk: sudo apk add dconf```

```zypper: sudo zypper install dconf```

```nix: nix profile install nixpkgs#dconf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gsettings](/man/gsettings)(1), [dconf-read](/man/dconf-read)(1), [dconf-write](/man/dconf-write)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/dconf)```

<!-- verified: 2026-07-11 -->
