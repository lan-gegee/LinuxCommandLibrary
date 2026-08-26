# TAGLINE

重建 aspell 字典哈希文件

# TLDR

**重建**所有 aspell 哈希文件

```sudo aspell-autobuildhash```

**强制**重建每个哈希文件

```sudo aspell-autobuildhash --force```

**预览**将要执行的操作而不做任何更改

```sudo aspell-autobuildhash --dry-run```

# SYNOPSIS

**aspell-autobuildhash** [_--force_]

# DESCRIPTION

**aspell-autobuildhash** 负责为字典软件包自动构建 aspell 哈希文件。它是 **dictionaries-common** 软件包的一部分，通常在字典安装或升级后由 dpkg 触发器自动调用。

对每个配置使用它的 aspell 字典，脚本会根据 aspell 兼容级别判断是否需要重建哈希文件，然后重新生成用于快速拼写检查的哈希文件。

# PARAMETERS

**--force**
> 为所有提供兼容性文件的字典重建哈希文件，无论发现的兼容级别如何。

**--dry-run**
> 显示将要执行的操作，但不做任何实际更改。

**--debug**
> 显示关于脚本内部工作的额外信息；同时启用 aspell 词缀校验。

**--triggered**
> 告知脚本它正运行在 dpkg 触发器阶段。

# CAVEATS

写入系统字典目录需要 root 权限。安装字典后通常由软件包管理器自动运行。

# HISTORY

**aspell-autobuildhash** 由 Debian 的 **dictionaries-common** 软件包提供，作者为 Agustin Martin，用于在字典更新后自动重新生成 aspell 哈希文件。

# INSTALL

```apt: sudo apt install aspell```

```dnf: sudo dnf install aspell```

```pacman: sudo pacman -S aspell```

```apk: sudo apk add aspell```

```zypper: sudo zypper install aspell```

```brew: brew install aspell```

```nix: nix profile install nixpkgs#aspell```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aspell](/man/aspell)(1), [aspell-import](/man/aspell-import)(1)

# RESOURCES

```[Documentation](https://manpages.debian.org/testing/dictionaries-common/aspell-autobuildhash.8.en.html)```

<!-- verified: 2026-06-17 -->
