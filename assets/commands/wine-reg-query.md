# TAGLINE

显示 Wine 注册表中的键和值

# TLDR

**查询**某个键并列出其值

```wine reg query [HKCU\Software\MyApp]```

**查询键的单个值**

```wine reg query [HKCU\Software\MyApp] /v [Name]```

**查询键的默认（无名）值**

```wine reg query [HKCU\Software\MyApp] /ve```

**递归查询**键（包括所有子键）

```wine reg query [HKCU\Software\MyApp] /s```

# SYNOPSIS

**wine reg query** _key_ [**/v** _value_ | **/ve**] [**/s**]

# DESCRIPTION

**wine reg query** 读取并打印 Wine 前缀中某个注册表键的内容。它与 Windows 的 **reg query** 命令一致。如果不带任何值选项，它列出直接存储在指定键下的值。

对每个值，输出会显示其名称、类型和数据。使用 **/s** 可遍历该键下的整个子树，适合一次性查看应用程序的完整配置。

# PARAMETERS

**/v**  _value_
> 查询键下指定名称的值。

**/ve**
> 查询键的默认（无名）值。

**/s**
> 递归查询所有子键及其值。

# INSTALL

```dnf: sudo dnf install wine```

```pacman: sudo pacman -S wine```

```apk: sudo apk add wine```

```zypper: sudo zypper install wine```

```nix: nix profile install nixpkgs#wine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wine](/man/wine)(1), [wine-reg](/man/wine-reg)(1), [wine-reg-add](/man/wine-reg-add)(1), [wine-reg-delete](/man/wine-reg-delete)(1), [wine-reg-copy](/man/wine-reg-copy)(1)

# RESOURCES

```[Source code](https://gitlab.winehq.org/wine/wine)```

```[Homepage](https://www.winehq.org)```

<!-- verified: 2026-06-22 -->
