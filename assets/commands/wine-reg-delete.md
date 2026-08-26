# TAGLINE

从 Wine 注册表删除键或值

# TLDR

**删除**注册表键及其下所有内容

```wine reg delete [HKCU\Software\MyApp]```

从某个键中**删除单个值**

```wine reg delete [HKCU\Software\MyApp] /v [Name]```

**删除键的默认（无名）值**

```wine reg delete [HKCU\Software\MyApp] /ve```

**删除键下的所有值**但保留键本身

```wine reg delete [HKCU\Software\MyApp] /va```

**不经确认提示删除**键

```wine reg delete [HKCU\Software\MyApp] /f```

# SYNOPSIS

**wine reg delete** _key_ [**/v** _value_ | **/ve** | **/va**] [**/f**]

# DESCRIPTION

**wine reg delete** 从 Wine 前缀中移除注册表键、单个值或键内的所有值。它与 Windows 的 **reg delete** 命令一致。如果不带任何值选项，整个键及其所有子键和值都会被移除。

默认情况下命令在删除前会请求确认。使用 **/f** 可跳过提示，这在脚本中以非交互方式运行时是必需的。

# PARAMETERS

**/v**  _value_
> 删除键下指定名称的值。

**/ve**
> 删除键的默认（无名）值。

**/va**
> 删除键下的所有值，但保留键本身及其子键不变。

**/f**
> 不经确认提示强制删除。

# CAVEATS

删除键而不指定值时，其下所有子键也会一并被移除。此操作无法撤销，如果之后可能需要恢复，请先用 **wine reg export** 导出该键。

# INSTALL

```dnf: sudo dnf install wine```

```pacman: sudo pacman -S wine```

```apk: sudo apk add wine```

```zypper: sudo zypper install wine```

```nix: nix profile install nixpkgs#wine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wine](/man/wine)(1), [wine-reg](/man/wine-reg)(1), [wine-reg-add](/man/wine-reg-add)(1), [wine-reg-query](/man/wine-reg-query)(1), [wine-reg-copy](/man/wine-reg-copy)(1)

# RESOURCES

```[Source code](https://gitlab.winehq.org/wine/wine)```

```[Homepage](https://www.winehq.org)```

<!-- verified: 2026-06-22 -->
