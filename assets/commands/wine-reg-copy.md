# TAGLINE

在 Wine 注册表内复制键及其值

# TLDR

把一个键的值**复制**到另一个键

```wine reg copy [HKCU\Software\MyApp] [HKCU\Software\MyAppCopy]```

**连同所有子键一起复制**键

```wine reg copy [HKCU\Software\MyApp] [HKCU\Software\MyAppCopy] /s```

**复制**键且**不经提示覆盖目标**

```wine reg copy [HKCU\Software\MyApp] [HKCU\Software\MyAppCopy] /f```

以**非交互方式复制**整个子树

```wine reg copy [HKCU\Software\MyApp] [HKCU\Software\MyAppCopy] /s /f```

# SYNOPSIS

**wine reg copy** _source_key_ _dest_key_ [**/s**] [**/f**]

# DESCRIPTION

**wine reg copy** 将某个注册表键的值复制到 Wine 前缀内的另一个键。它与 Windows 的 **reg copy** 命令一致。默认情况下只复制直接存储在源键下的值；加上 **/s** 则同时复制其下所有子键。

当目标中已存在同名值时，除非提供 **/f**，否则命令在覆盖前会提示确认。源和目标可以是同一根键内的不同键，也可以跨不同的根键。

# PARAMETERS

**/s**
> 复制源键下的所有子键和值，而不仅仅是其直属的值。

**/f**
> 强制复制，不经确认提示直接覆盖目标中已有的值。

# INSTALL

```dnf: sudo dnf install wine```

```pacman: sudo pacman -S wine```

```apk: sudo apk add wine```

```zypper: sudo zypper install wine```

```nix: nix profile install nixpkgs#wine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wine](/man/wine)(1), [wine-reg](/man/wine-reg)(1), [wine-reg-add](/man/wine-reg-add)(1), [wine-reg-delete](/man/wine-reg-delete)(1), [wine-reg-query](/man/wine-reg-query)(1)

# RESOURCES

```[Source code](https://gitlab.winehq.org/wine/wine)```

```[Homepage](https://www.winehq.org)```

<!-- verified: 2026-06-22 -->
