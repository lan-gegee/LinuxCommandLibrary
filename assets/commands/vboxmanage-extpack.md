# TAGLINE

管理 VirtualBox 扩展包

# TLDR

**安装扩展包**

```vboxmanage extpack install [extension.vbox-extpack]```

**安装并替换现有版本**

```vboxmanage extpack install --replace [extension.vbox-extpack]```

**按名称卸载扩展包**

```vboxmanage extpack uninstall "[Oracle VM VirtualBox Extension Pack]"```

**强制卸载扩展包**

```vboxmanage extpack uninstall --force "[Oracle VM VirtualBox Extension Pack]"```

**列出已安装的扩展包**

```vboxmanage list extpacks```

**清理失败操作留下的临时文件**

```vboxmanage extpack cleanup```

# SYNOPSIS

**vboxmanage** **extpack** _command_ [_options_]

# PARAMETERS

**install** [**--replace**] _tarball_
> 从指定文件安装扩展包。如果已安装旧版本且未使用 --replace，则安装会失败。

**uninstall** [**--force**] _name_
> 按名称卸载扩展包。即使该包不存在也会成功返回。

**cleanup**
> 清理安装或卸载失败操作遗留的临时文件和目录。

**--replace**
> 与 install 搭配使用。在安装新版本前卸载任何现有版本。

**--force**
> 与 uninstall 搭配使用。绕过大多数拒绝卸载扩展包的情况。

# DESCRIPTION

**vboxmanage extpack** 管理 VirtualBox 扩展包。扩展包提供 USB 2.0/3.0、VirtualBox RDP 和磁盘加密等附加功能。安装或卸载扩展包通常需要管理员权限。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-list](/man/vboxmanage-list)(1)
