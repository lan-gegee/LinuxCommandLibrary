# TAGLINE

从命令行读取和修改 Wine 注册表

# TLDR

向注册表键**添加**值

```wine reg add [HKCU\Software\MyApp] /v [Setting] /t [REG_SZ] /d [value] /f```

**查询**键及其值

```wine reg query [HKCU\Software\MyApp]```

从键中**删除**值

```wine reg delete [HKCU\Software\MyApp] /v [Setting] /f```

把键（含子键）**复制**到另一个位置

```wine reg copy [HKCU\Software\MyApp] [HKCU\Software\MyAppBackup] /s /f```

从 .reg 文件**导入**注册表项

```wine reg import [file.reg]```

将键**导出**为 .reg 文件

```wine reg export [HKCU\Software\MyApp] [file.reg]```

# SYNOPSIS

**wine reg** _operation_ _key_ [_options_]

operation := **add** | **delete** | **query** | **copy** | **import** | **export**

# DESCRIPTION

**wine reg** 是 Wine 对 Windows **reg.exe** 控制台工具的重新实现。它让你无需启动图形化的 **regedit** 即可检查和编辑 Wine 前缀的注册表，这对编写安装脚本、在 Wine 前缀中应用调整以及自动化应用程序配置非常方便。

注册表键通过其根键和路径来定位，例如 **HKEY_CURRENT_USER\Software\MyApp**。也接受标准的根键缩写：**HKLM**（HKEY_LOCAL_MACHINE）、**HKCU**（HKEY_CURRENT_USER）、**HKCR**（HKEY_CLASSES_ROOT）、**HKU**（HKEY_USERS）和 **HKCC**（HKEY_CURRENT_CONFIG）。

该工具操作的是由 **WINEPREFIX** 环境变量指定的前缀的注册表（默认为 **~/.wine**）。每个操作都是一个独立的子命令，各有自己的说明页。

# OPERATIONS

**add**
> 创建键，或在其中添加或覆盖值。

**delete**
> 移除键、单个值或键下的所有值。

**query**
> 显示存储在键下的值，可选递归进入子键。

**copy**
> 将一个键的值（可选连同子键）复制到另一个键。

**import**
> 将 .reg 文件的内容合并进注册表。

**export**
> 将键及其内容写入 .reg 文件。

# CAVEATS

根据你所用的 shell，键路径中的反斜杠可能需要引号或转义处理。编辑错误前缀的注册表是常见失误；如果你维护多个前缀，请显式设置 **WINEPREFIX**。与原生 Windows 工具一样，粗心的修改可能破坏应用程序，因此修改前请先用 **export** 备份相关键。

# INSTALL

```dnf: sudo dnf install wine```

```pacman: sudo pacman -S wine```

```apk: sudo apk add wine```

```zypper: sudo zypper install wine```

```nix: nix profile install nixpkgs#wine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wine](/man/wine)(1), [reg](/man/reg)(1), [wine-reg-add](/man/wine-reg-add)(1), [wine-reg-delete](/man/wine-reg-delete)(1), [wine-reg-query](/man/wine-reg-query)(1), [wine-reg-copy](/man/wine-reg-copy)(1)

# RESOURCES

```[Source code](https://gitlab.winehq.org/wine/wine)```

```[Homepage](https://www.winehq.org)```

```[Documentation](https://gitlab.winehq.org/wine/wine/-/wikis/home)```

<!-- verified: 2026-06-22 -->
