# TAGLINE

更新 PlatformIO 软件包和库（已废弃）

# TLDR

**更新所有软件包**

```pio update```

**仅更新核心软件包**

```pio update --core-packages```

**检查更新但不安装**

```pio update --dry-run```

# SYNOPSIS

**pio update** [_options_]

# PARAMETERS

**--core-packages**
> 仅更新核心软件包。

**--dry-run**
> 检查新版本但不安装。

**-c**, **--only-check**
> **--dry-run** 的已废弃别名。

# DESCRIPTION

**pio update** 用于更新已安装的 PlatformIO Core 软件包、开发平台和全局库，相当于 **pio platform update** 和 **pio lib update** 的组合。

# CAVEATS

自 PlatformIO 6.0 起已废弃，将在未来版本中移除。请改用 **pio pkg update**。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-upgrade](/man/pio-upgrade)(1), [pio-pkg](/man/pio-pkg)(1), [pio-platform](/man/pio-platform)(1), [pio-lib](/man/pio-lib)(1)
