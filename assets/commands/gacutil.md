# TAGLINE

全局程序集缓存（GAC）管理工具

# TLDR

**将程序集安装到 GAC**

```gacutil -i [assembly.dll]```

**从 GAC 卸载程序集**

```gacutil -u [AssemblyName]```

**列出 GAC 中的程序集**

```gacutil -l```

**列出指定程序集**

```gacutil -l [AssemblyName]```

**从软件包安装**

```gacutil -i [assembly.dll] -package [name]```

# SYNOPSIS

**gacutil** [_options_] [_assembly_]

# PARAMETERS

**-i** _assembly_
> 将程序集安装到 GAC。

**-u** _name_
> 从 GAC 卸载程序集。

**-l** [_name_]
> 列出程序集（可按名称过滤）。

**-il** _listfile_
> 从列表文件安装程序集。

**-ul** _listfile_
> 从列表文件卸载程序集。

**-us** _assembly_
> 使用程序集文件中的完整名称卸载程序集。

**-package** _name_
> 安装时的软件包名；会在 prefix/lib/mono/NAME/ 下创建符号链接。

**-check_refs**
> 检查已安装的程序集是否引用了非强命名的程序集。

**-root** _dir_
> GAC 操作的根目录前缀。

**-gacdir** _dir_
> 指定 GAC 目录（已弃用，请改用 -root）。

# DESCRIPTION

**gacutil** 管理 .NET 程序集的全局程序集缓存（GAC）。GAC 存储可被多个 .NET 应用程序共享的程序集。

在 Linux 上，gacutil 由 Mono 提供。它负责在 GAC 中安装、卸载和列出程序集。强命名的程序集可以通过 GAC 在多个应用间共享。

# CAVEATS

安装到 GAC 需要强命名的程序集。Mono 的 GAC 与 Windows 的 .NET GAC 不同。可能需要 root 权限。.NET Core 不使用 GAC；程序集是自包含的。

# HISTORY

GAC 由 Microsoft 随 **.NET Framework 1.0** 推出，用于程序集共享。Mono 实现了包括 gacutil 在内的兼容工具，支持跨平台 .NET 开发。随着 .NET Core/.NET 5+ 的到来，GAC 模式被 NuGet 软件包取代。

# INSTALL

```pacman: sudo pacman -S mono```

```apk: sudo apk add mono```

```brew: brew install mono```

```nix: nix profile install nixpkgs#mono```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mono](/man/mono)(1), [mcs](/man/mcs)(1), [dotnet](/man/dotnet)(1)
