# TAGLINE

管理 Azure Container Apps 的终端界面

# TLDR

**启动 TUI** 并连接到 Azure

```az-tui```

**使用模拟数据启动**，无需连接 Azure 即可测试

```az-tui --mock```

**启动前限定特定资源组**

```ACA_RG="my-resource-group" az-tui```

**显示版本并退出**

```az-tui -version```

# SYNOPSIS

**az-tui** [_options_]

# PARAMETERS

**-mock**, **-m**
> 使用模拟数据而不连接 Azure CLI

**-version**
> 输出版本信息并退出

# DESCRIPTION

**az-tui** 是一个基于终端的用户界面，用于管理 Azure Container Apps，设计灵感来自 **K9s**。它提供键盘驱动的界面，可以直接在终端中浏览、检查和调试容器应用，无需打开 Azure 门户。

该工具采用分层导航模型：资源组、容器应用、修订版本（revision）、容器和环境变量。用户可以查看 JSON 格式的详细应用元数据、检查修订版本的活跃状态和流量分配百分比、实时流式查看容器日志，还可以在运行中的容器内执行命令进行故障排查。

**az-tui** 使用 Go 语言编写，基于 Bubble Tea TUI 框架，通过 Azure CLI 与 Azure 通信。导航采用受 VIM 启发的按键绑定：**/** 筛选，**:** 切换上下文，**Enter** 进入下一层，**Esc** 返回上一层，**q** 退出。模式专属的绑定包括 **r** 刷新、**R** 重启修订版本、**l** 查看日志、**s** 打开 shell、**v** 显示环境变量。

模拟模式（**--mock**）提供合成数据，供开发和测试使用，无需 Azure 凭据。

# CONFIGURATION

可以设置 **ACA_RG** 环境变量，将浏览范围限制在特定的 Azure 资源组。若未设置，则显示订阅中的所有资源组。

# CAVEATS

需要安装 Azure CLI 并已通过 **az login** 完成身份验证。必须安装 Azure Container Apps 扩展（**az extension add -n containerapp**）。仅支持管理 Azure Container Apps；不支持其他 Azure 服务。该项目尚处于早期开发阶段。

# HISTORY

**az-tui** 由 **IAL32** 创建，于 **2024** 年 **8 月**作为采用 MIT 许可证的开源项目发布在 GitHub 上。它使用 Go 编写，基于 Charm 生态（Bubble Tea、Bubbles、Lip Gloss）构建。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [k9s](/man/k9s)(1), [docker](/man/docker)(1)
