# TAGLINE

管理 Azure CLI 扩展

# TLDR

**列出已安装的扩展**

```az extension list```

**列出可用的扩展**

```az extension list-available```

按名称**安装扩展**

```az extension add --name [extension_name]```

**安装扩展的特定版本**

```az extension add --name [extension_name] --version [1.2.3]```

**更新扩展**

```az extension update --name [extension_name]```

**移除扩展**

```az extension remove --name [extension_name]```

**从本地 wheel 文件安装**

```az extension add --source [path/to/extension.whl]```

**显示扩展详情**

```az extension show --name [extension_name]```

# SYNOPSIS

**az extension** _subcommand_ [_options_]

# DESCRIPTION

**az extension** 是 Azure CLI 的一个子命令，用于管理 CLI 扩展。扩展为 Azure CLI 添加新的命令组和功能，而无需更新核心安装。

扩展是以 wheel 文件形式分发的 Python 软件包。可以从官方 Azure 扩展索引、URL 或本地文件安装。某些 Azure 服务需要先安装对应扩展才能使用其命令。

扩展按用户安装，其版本可以不同于 CLI 自带的版本。可以启用动态安装功能，在使用不可用命令时自动提示安装相应扩展。

# PARAMETERS

**list**
> 显示当前已安装的扩展。

**list-available**
> 显示可安装的扩展。

**add**
> 安装扩展。

**update**
> 将扩展更新到最新版本。

**remove**
> 卸载扩展。

**show**
> 显示已安装扩展的详情。

**list-versions**
> 列出扩展的可用版本。

**--name** _name_
> 扩展名称。

**--source** _path_
> wheel 文件的路径或 URL。

**--version** _version_
> 要安装的特定版本。

**--yes**
> 不提示确认。

**--upgrade**
> 若已安装则更新。

**--allow-preview** _{false, true}_
> 若存在预览包则将其纳入安装范围。

**--system**
> 安装到所有用户共享的系统目录而非每用户目录。

**--pip-extra-index-urls** _urls_
> 额外的软件包索引 URL，空格分隔（符合 PEP 503）。

**--pip-proxy** _proxy_
> pip 为扩展依赖使用的代理，格式为 [user:passwd@]proxy.server:port。

# CAVEATS

扩展可能对 Azure CLI 有版本兼容性要求。升级 CLI 可能需要同时更新扩展。某些扩展处于预览阶段，可能有破坏性变更。从第三方来源安装的扩展应经过安全验证。从本地源安装时要求 wheel 与 Python 版本匹配。

# HISTORY

Azure CLI 扩展系统随 **2017** 年的 **Azure CLI 2.0** 推出，旨在提供模块化功能而不让核心安装变得臃肿。扩展索引已增长到包含数百个扩展，涵盖预览服务、实验性功能和合作伙伴集成。**动态安装**功能可在找不到命令时自动建议相应扩展。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [pip](/man/pip)(1), [az-config](/man/az-config)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/extension)```

<!-- verified: 2026-06-18 -->
