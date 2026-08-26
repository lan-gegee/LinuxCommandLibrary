# TAGLINE

录入用于认证的指纹

# TLDR

为当前用户录入**右手食指**

```fprintd-enroll```

为当前用户录入**指定的手指**

```fprintd-enroll -f [left-thumb|left-index-finger|right-thumb|...]```

为**特定用户**录入右手食指

```fprintd-enroll [username]```

为**特定用户**录入**指定的手指**

```fprintd-enroll -f [finger_name] [username]```

显示**帮助**

```fprintd-enroll --help```

# SYNOPSIS

**fprintd-enroll** [_options_] [_username_]

# PARAMETERS

**-f**, **--finger** _FINGER_
> 指定要录入的手指：left-thumb、left-index-finger、left-middle-finger、left-ring-finger、left-little-finger、right-thumb、right-index-finger、right-middle-finger、right-ring-finger、right-little-finger。默认：right-index-finger。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fprintd-enroll** 将指纹录入 fprintd 数据库以用于生物识别认证。录入过程中，会提示用户多次扫描手指，以建立可靠的指纹模板。

默认手指为 right-index-finger（右手食指）。多次运行该命令并指定不同的 **--finger** 值即可录入多枚指纹。

已录入的指纹可用于 PAM 认证，在正确配置后支持指纹登录、sudo 验证以及其他认证场景。

# CAVEATS

录入质量取决于指纹读取器和皮肤状态。皮肤干燥或受损可能导致录入效果不佳。需要多次扫描才能生成可靠的模板。为其他用户录入指纹可能需要 root 权限。

# INSTALL

```apt: sudo apt install fprintd```

```dnf: sudo dnf install fprintd```

```pacman: sudo pacman -S fprintd```

```apk: sudo apk add fprintd```

```zypper: sudo zypper install fprintd```

```nix: nix profile install nixpkgs#fprintd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fprintd](/man/fprintd)(1), [fprintd-delete](/man/fprintd-delete)(1), [fprintd-list](/man/fprintd-list)(1), [fprintd-verify](/man/fprintd-verify)(1)
