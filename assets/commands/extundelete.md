# TAGLINE

ext3/ext4 文件恢复工具

# TLDR

从分区**恢复所有**已删除的文件

```sudo extundelete [/dev/sdXN] --restore-all```

恢复**指定文件**

```extundelete [/dev/sdXN] --restore-file [path/to/file]```

恢复**指定目录**

```extundelete [/dev/sdXN] --restore-directory [path/to/directory]```

恢复在某个日期**之后**删除的文件

```extundelete [/dev/sdXN] --restore-all --after [1577840400]```

# SYNOPSIS

**extundelete** _device_ [_options_]

# DESCRIPTION

**extundelete** 通过解析文件系统日志从 ext3 和 ext4 分区中恢复已删除的文件。它可以恢复单个文件、目录或所有可恢复的文件。

在删除后立即运行（日志尚未回绕之前）效果最佳。

# PARAMETERS

**--restore-all**
> 恢复所有可恢复的文件

**--restore-file** _path_
> 恢复指定文件

**--restore-directory** _path_
> 恢复指定目录

**--after** _time_
> 只恢复在给定 Unix 时间戳之后删除的文件

**--before** _time_
> 只恢复在给定时间戳之前删除的文件

# CAVEATS

仅适用于 ext3/ext4 文件系统。为获得最佳效果，恢复前应卸载分区。路径相对于文件系统根目录（开头不加 /）。恢复成败取决于日志的状态。

# INSTALL

```apt: sudo apt install extundelete```

```dnf: sudo dnf install extundelete```

```zypper: sudo zypper install extundelete```

```nix: nix profile install nixpkgs#extundelete```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[testdisk](/man/testdisk)(8), [photorec](/man/photorec)(8), [debugfs](/man/debugfs)(8)

# RESOURCES

```[Homepage](http://extundelete.sourceforge.net/)```

<!-- verified: 2026-07-15 -->
