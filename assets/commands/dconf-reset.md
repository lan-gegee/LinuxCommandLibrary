# TAGLINE

将 dconf 键重置为默认值

# TLDR

**重置**指定的键

```dconf reset /[path/to/key]```

重置整个**目录**

```dconf reset -f /[path/to/directory]/```

# SYNOPSIS

**dconf reset** [_options_] _path_

# DESCRIPTION

**dconf reset** 从 dconf 数据库中移除键，从而有效地将其重置为默认值。默认值通常由应用程序的 GSettings schema 定义；移除用户存储的值后，应用程序会回退到这些默认值。

重置单个键时，只会移除那个特定的设置。对目录路径使用 -f 标志会移除该目录树下所有键，适用于彻底重置某个配置部分或整个应用程序设置。

此操作立即生效，且无法通过 dconf 本身撤销。如果可能需要恢复之前的值，建议在重置前先用 "dconf dump" 创建备份。重置操作常用于排查应用行为问题或恢复到已知正常的配置状态。

# PARAMETERS

**-f**
> 强制重置整个目录树

_path_
> 要重置的键或目录

# CAVEATS

重置会移除存储的值，应用程序将改用其 schema 默认值。-f 会重置目录树中的所有键，请谨慎使用。操作不可撤销。

# INSTALL

```apt: sudo apt install dconf-cli```

```dnf: sudo dnf install dconf```

```pacman: sudo pacman -S dconf```

```apk: sudo apk add dconf```

```zypper: sudo zypper install dconf```

```nix: nix profile install nixpkgs#dconf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dconf](/man/dconf)(1), [dconf-read](/man/dconf-read)(1), [dconf-write](/man/dconf-write)(1), [gsettings](/man/gsettings)(1)
