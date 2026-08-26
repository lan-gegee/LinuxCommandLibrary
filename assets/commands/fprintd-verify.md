# TAGLINE

将指纹与已录入的指纹进行比对验证

# TLDR

验证当前用户的**所有已存指纹**

```fprintd-verify```

验证当前用户的**指定指纹**

```fprintd-verify -f [left-thumb|left-index-finger|right-thumb|...]```

验证**特定用户**的指纹

```fprintd-verify [username]```

验证**特定用户**的**指定指纹**

```fprintd-verify -f [finger_name] [username]```

显示**帮助**

```fprintd-verify -h```

# SYNOPSIS

**fprintd-verify** [_options_] [_username_]

# PARAMETERS

**-f**, **--finger** _FINGER_
> 指定要验证的手指：left-thumb、left-index-finger、left-middle-finger、left-ring-finger、left-little-finger、right-thumb、right-index-finger、right-middle-finger、right-ring-finger、right-little-finger。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**fprintd-verify** 将扫描到的指纹与 fprintd 数据库中已录入的指纹进行比对测试。它会提示用户扫描手指，并报告扫描结果是否与任何已录入的指纹匹配。它通过 D-Bus 与 fprintd 守护进程通信。

该命令适合用来测试指纹录入的质量以及排查认证问题。若不指定手指，系统会尝试与所有已录入的手指进行比对。

# CAVEATS

验证能否成功取决于扫描质量，可能需要多次尝试。传感器上的水分或污垢等环境因素会影响结果。此命令仅用于测试；实际登录认证使用 PAM 模块 **pam_fprintd**。fprintd 守护进程必须正在运行，此命令才能工作。

# INSTALL

```apt: sudo apt install fprintd```

```dnf: sudo dnf install fprintd```

```pacman: sudo pacman -S fprintd```

```apk: sudo apk add fprintd```

```zypper: sudo zypper install fprintd```

```nix: nix profile install nixpkgs#fprintd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fprintd](/man/fprintd)(1), [fprintd-enroll](/man/fprintd-enroll)(1), [fprintd-delete](/man/fprintd-delete)(1), [fprintd-list](/man/fprintd-list)(1)
