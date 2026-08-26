# TAGLINE

从 Flatpak 软件仓库安装应用程序

# TLDR

从已配置的远程仓库**安装应用程序**

```flatpak install [application_id]```

**从指定的远程仓库安装**

```flatpak install [flathub] [org.gnome.gedit]```

仅**为当前用户安装**

```flatpak install --user [application_id]```

**从 .flatpakref 文件安装**

```flatpak install --from [https://example.com/app.flatpakref]```

**从本地 bundle 文件安装**

```flatpak install --bundle [path/to/app.flatpak]```

如果已安装则**改为更新**

```flatpak install --or-update [application_id]```

**无需确认提示**直接安装

```flatpak install -y [application_id]```

# SYNOPSIS

**flatpak install** [_OPTIONS_] [_REMOTE_] _REF_...

**flatpak install** [_OPTIONS_] [**--from**|**--bundle**] _LOCATION_

# PARAMETERS

**-u**, **--user**
> 安装到按用户划分的安装目录。

**--system**
> 安装到默认的系统级安装位置。

**--installation**=_NAME_
> 安装到特定的系统级安装位置。

**--reinstall**
> 如果已安装则先卸载。

**--or-update**
> 如果已安装则静默更新。

**--bundle**
> 将位置视为单个 bundle 的 .flatpak 文件。

**--from**
> 将位置视为 .flatpakref 应用描述文件。

**-y**, **--assumeyes**
> 自动对所有提示回答 yes。

**--no-deploy**
> 只下载而不部署。

**--no-pull**
> 不下载，直接从本地缓存部署。

**-v**, **--verbose**
> 打印调试信息。

**-h**, **--help**
> 显示帮助并退出。

# DESCRIPTION

**flatpak install** 从 Flatpak 软件仓库安装应用程序或运行时。REF 参数使用 **(app|runtime)/ID/ARCH/BRANCH** 格式指定要安装的内容。通常只需要应用 ID；其余部分会被自动匹配，存在歧义时会提示选择。

安装来源包括已配置的远程仓库（如 Flathub）、.flatpakref 文件（应用描述 URL）、.flatpak bundle 文件或 OCI 镜像。默认情况下，应用程序安装到系统范围；使用 **--user** 可进行按用户安装。

依赖项（运行时、扩展）会被自动解析并安装。该命令会提示确认，显示将要下载和安装的内容。

# CAVEATS

系统级安装需要 root 权限或 polkit 身份验证。按用户安装的内容存储在 ~/.local/share/flatpak/ 中。某些应用需要特定的运行时，它们会被自动安装。安装之前必须先配置好相应的远程仓库。

# HISTORY

Flatpak 由 Red Hat 的 Alexander Larsson 开发，首个稳定版发布于 **2015 年**（最初名为 xdg-app）。它提供与 Linux 发行版无关的沙箱化应用分发方式。Flathub 是主要的 Flatpak 仓库，于 **2017 年**上线，如今已成为最大的 Flatpak 应用来源。

# INSTALL

```apt: sudo apt install flatpak```

```dnf: sudo dnf install flatpak```

```pacman: sudo pacman -S flatpak```

```apk: sudo apk add flatpak```

```zypper: sudo zypper install flatpak```

```nix: nix profile install nixpkgs#flatpak```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flatpak](/man/flatpak)(1), [flatpak-update](/man/flatpak-update)(1), [flatpak-run](/man/flatpak-run)(1)
