# TAGLINE

生成随机身份信息

# TLDR

显示**随机姓名**和地址

```rig```

显示**男性**随机身份

```rig -m```

显示**女性**随机身份

```rig -f```

使用**指定目录**中的数据文件

```rig -d path/to/directory```

显示**指定数量**的身份信息

```rig -c 5```

# SYNOPSIS

**rig** [_options_]

# PARAMETERS

**-m**
> 仅生成男性身份。

**-f**
> 仅生成女性身份。

**-d** _directory_
> 使用指定目录中的数据文件。

**-c** _count_
> 要生成的身份数量。

# DESCRIPTION

**rig** 生成随机身份信息，包括名字、姓氏、街道地址、城市、州、邮编和电话区号。同一地区的各个组成部分在地理上保持一致。

它适用于测试应用程序、生成示例数据，或向数据库填充外观逼真但虚构的个人信息。

# CAVEATS

生成的数据是随机且虚构的。可用的姓名和地点由数据文件决定。

# HISTORY

作为一个生成逼真个人信息的随机测试数据的实用工具而创建。

# INSTALL

```apt: sudo apt install rig```

```dnf: sudo dnf install rig```

```brew: brew install rig```

```nix: nix profile install nixpkgs#rig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pwgen](/man/pwgen)(1)
