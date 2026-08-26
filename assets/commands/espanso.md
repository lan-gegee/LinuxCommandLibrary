# TAGLINE

跨平台文本扩展工具

# TLDR

**启动 Espanso**

```espanso start```

**停止 Espanso**

```espanso stop```

**重启服务**

```espanso restart```

**编辑配置**

```espanso edit```

**搜索软件包**

```espanso package search [keyword]```

**安装软件包**

```espanso package install [package_name]```

**显示状态**

```espanso status```

# SYNOPSIS

**espanso** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：start、stop、restart、edit、package 等。

**start**
> 启动 Espanso 服务。

**stop**
> 停止服务。

**restart**
> 重启服务。

**edit**
> 在编辑器中打开配置。

**package search** _KEYWORD_
> 搜索软件包。

**package install** _NAME_
> 安装软件包。

**status**
> 显示服务状态。

**service register**
> 注册 espanso 使其在登录时自动启动。

**env-path register**
> 将 espanso 可执行文件添加到系统 PATH。

**match list**
> 列出当前所有生效的匹配项。

**path**
> 打印解析后的配置、软件包和运行时目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Espanso** 是一个跨平台的文本扩展工具，可将输入的缩写替换为预定义的文本片段。它在后台运行，检测触发字符串并在整个系统范围内展开它们。

配置文件定义触发器与替换内容之间的匹配关系。替换内容可以是静态文本、动态内容（日期、剪贴板）或脚本。软件包则提供预先配置好的扩展条目。

Espanso 适用于所有应用程序，可处理常见的输入模式、样板文本和常用短语。

# CONFIGURATION

**~/.config/espanso/config/default.yml**
> 主配置文件，控制切换键、后端偏好等行为以及全局设置。

**~/.config/espanso/match/base.yml**
> 默认匹配文件，定义触发器和替换内容。可创建更多匹配文件来组织各条扩展。

# CAVEATS

需要后台服务运行。在 macOS 上需要辅助功能权限。某些应用程序可能不支持输入注入。可能出现触发器冲突。

# HISTORY

Espanso 由 **Federico Terzi** 创建，是商业文本扩展工具的开源跨平台替代品。它用 Rust 编写，强调隐私与性能。

# INSTALL

```zypper: sudo zypper install espanso```

```nix: nix profile install nixpkgs#espanso```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdotool](/man/xdotool)(1), [autokey](/man/autokey)(1)

# RESOURCES

```[Source code](https://github.com/espanso/espanso)```

```[Homepage](https://espanso.org/)```

```[Documentation](https://espanso.org/docs/)```

<!-- verified: 2026-07-14 -->
