# TAGLINE

向 Wine 注册表添加键或值

# TLDR

**创建**注册表键

```wine reg add [HKCU\Software\MyApp]```

向某个键**添加字符串值**

```wine reg add [HKCU\Software\MyApp] /v [Name] /t [REG_SZ] /d [value]```

**添加 DWORD 值**

```wine reg add [HKCU\Software\MyApp] /v [Enabled] /t [REG_DWORD] /d [1]```

**设置键的默认（无名）值**

```wine reg add [HKCU\Software\MyApp] /ve /d [default]```

**不提示直接覆盖**已有值

```wine reg add [HKCU\Software\MyApp] /v [Name] /d [new] /f```

# SYNOPSIS

**wine reg add** _key_ [**/v** _value_ | **/ve**] [**/t** _type_] [**/s** _separator_] [**/d** _data_] [**/f**]

# DESCRIPTION

**wine reg add** 在 Wine 前缀中创建注册表键，或在现有键中添加（或覆盖）值。它的行为与 Windows 的 **reg add** 命令一致。如果不带任何值选项，它只是确保指定的键存在。

一个值由其名称（**/v**）、类型（**/t**）和数据（**/d**）描述。默认类型是 **REG_SZ**（字符串）。当指定的值已存在时，除非给出 **/f**，否则 reg add 在覆盖前会提示确认。

# PARAMETERS

**/v**  _value_
> 要在该键下添加的值名称。

**/ve**
> 添加或设置键的默认（无名）值。

**/t**  _type_
> 值的数据类型，如 **REG_SZ**、**REG_EXPAND_SZ**、**REG_MULTI_SZ**、**REG_DWORD**、**REG_BINARY** 或 **REG_NONE**。默认为 **REG_SZ**。

**/s**  _separator_
> 用于分隔 **REG_MULTI_SZ** 值各元素的字符。默认为 **\0**。

**/d**  _data_
> 要存储在值中的数据。

**/f**
> 强制执行操作，不经确认提示直接覆盖已有的值。

# INSTALL

```dnf: sudo dnf install wine```

```pacman: sudo pacman -S wine```

```apk: sudo apk add wine```

```zypper: sudo zypper install wine```

```nix: nix profile install nixpkgs#wine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wine](/man/wine)(1), [wine-reg](/man/wine-reg)(1), [wine-reg-delete](/man/wine-reg-delete)(1), [wine-reg-query](/man/wine-reg-query)(1), [wine-reg-copy](/man/wine-reg-copy)(1)

# RESOURCES

```[Source code](https://gitlab.winehq.org/wine/wine)```

```[Homepage](https://www.winehq.org)```

<!-- verified: 2026-06-22 -->
