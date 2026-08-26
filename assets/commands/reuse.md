# TAGLINE

管理 FSFE REUSE 软件许可合规

# TLDR

**检查合规性**

```reuse lint```

**添加许可证头**

```reuse annotate --license [MIT] --copyright "[Author]" [file]```

**下载许可证**

```reuse download [MIT]```

**生成 SPDX 清单**

```reuse spdx```

**初始化项目**

```reuse init```

**显示文件状态**

```reuse status```

# SYNOPSIS

**reuse** _command_ [_options_]

# PARAMETERS

**lint**
> 检查合规性。

**annotate**
> 添加许可证头。

**download**
> 获取许可证文本。

**spdx**
> 生成 SPDX 文件。

**init**
> 初始化项目。

**--license** _ID_
> SPDX 许可证标识符。

**--copyright** _TEXT_
> 版权持有者。

# DESCRIPTION

**reuse** 是一个按照 FSFE REUSE 规范管理软件许可的工具，该规范确保项目中的每个文件都具有清晰、机器可读的版权和许可信息。它帮助开发者向源文件添加标准化的 SPDX 许可证头，并验证整个项目满足合规要求。

**lint** 命令检查项目是否符合 REUSE 规范，验证所有文件都有适当的许可和版权标注。**annotate** 命令在源文件中添加或更新 SPDX 头，并自动调整注释风格以匹配文件类型。可以使用 **reuse download** 通过标准的 SPDX 标识符（如 MIT、Apache-2.0 或 GPL-3.0-or-later）下载许可证文本。

该工具还可以通过 **spdx** 命令生成 SPDX 软件物料清单文件，提供项目中所有许可和版权的完整机器可读清单。此输出与 CI/CD 流水线和合规审计工作流集成良好。

# CAVEATS

需要 SPDX 标识符。某些许可证较为复杂。配置有一定学习曲线。

# HISTORY

**reuse** 实现了 **FSFE REUSE** 规范，提供让软件许可清晰且机器可读的工具。

# INSTALL

```dnf: sudo dnf install reuse```

```pacman: sudo pacman -S reuse```

```apk: sudo apk add reuse```

```zypper: sudo zypper install reuse```

```brew: brew install reuse```

```nix: nix profile install nixpkgs#reuse```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[licensecheck](/man/licensecheck)(1)
