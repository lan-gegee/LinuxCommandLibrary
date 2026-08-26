# TAGLINE

rm 的安全包装器，防止误删重要文件

# TLDR

**删除文件**，并防止删除黑名单中的路径

```safe-rm [path/to/file]```

在保护检查下**递归删除目录**

```safe-rm -r [path/to/directory]```

在遵守受保护路径的前提下**强制删除文件**

```safe-rm -rf [path/to/directory]```

**删除多个文件**并显示详细输出

```safe-rm -v [file1] [file2] [file3]```

# SYNOPSIS

**safe-rm** [_rm options_] [_files_]

# PARAMETERS

safe-rm 接受所有标准 **rm** 选项，并在验证路径不受保护后将其透传给真正的 rm 命令。

**-r**, **-R**, **--recursive**
> 递归删除目录及其内容

**-f**, **--force**
> 忽略不存在的文件和参数，从不提示

**-i**
> 每次删除前提示

**-v**, **--verbose**
> 显示正在进行的操作

# DESCRIPTION

**safe-rm** 是 rm 命令的包装器，可防止意外删除重要的系统文件和目录。它在把参数传给真正的 rm 之前，会先对照可配置的黑名单进行检查。

当用户尝试删除受保护的路径时，safe-rm 会拒绝该操作并显示警告。这为 **rm -rf /** 之类的灾难性失误提供了安全保障。

受保护的路径可在 **/etc/safe-rm.conf**（系统级保护）和 **~/.safe-rm**（用户级设置）中配置。每个文件每行一个路径。若两者均为空，则使用一份默认的关键系统路径列表。

要将 safe-rm 作为默认的 rm 使用，可在 PATH 中排在 /bin 之前的目录里创建符号链接：
```ln -s /usr/bin/safe-rm /usr/local/bin/rm```

# CONFIGURATION

**/etc/safe-rm.conf**
> 系统级的受保护路径列表，每行一个。对任何列出路径的删除操作都会被阻止。

**~/.safe-rm**
> 用户级的额外受保护路径列表。

# CAVEATS

safe-rm 无法防范所有删除方式。例如，若 /usr/lib 受保护，**rm -rf /usr/lib** 会被阻止；但运行 **cd /usr/lib && rm -rf *** 会绕过保护，因为此时受保护的路径本身并不是参数。

# HISTORY

safe-rm 的诞生是为了防止误删关键系统文件。**2020 年 11 月**发布的 1.0.0 版本是用 **Rust** 完全重写的版本，取代了最初的实现。该项目采用 GPLv3 许可证。

# INSTALL

```apt: sudo apt install safe-rm```

```brew: brew install safe-rm```

```nix: nix profile install nixpkgs#safe-rm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rm](/man/rm)(1), [trash-cli](/man/trash-cli)(1), [shred](/man/shred)(1)
