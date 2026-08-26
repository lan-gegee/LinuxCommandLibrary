# TAGLINE

向维护者报告 bash 的 bug

# TLDR

**报告** bash bug

```bashbug```

# SYNOPSIS

**bashbug** [_--help_] [_--version_] [_email-address_]

# DESCRIPTION

**bashbug** 是一个向维护者报告 bash bug 的脚本。它收集系统信息和 bash 版本详情，打开编辑器撰写 bug 报告，然后通过电子邮件发送给 bash 开发者。

默认情况下，稳定版会将报告发送至 **bug-bash@gnu.org**；可选的 _email-address_ 参数可以覆盖收件人。编辑器依次从 **DEFEDITOR**、**EDITOR** 或 **VISUAL** 中选择，若都未设置则回退到常见编辑器，最终使用 **vi**。

# PARAMETERS

**--help**
> 打印用法信息并退出。

**--version**
> 打印 bashbug 版本并退出。

_email-address_
> 将报告发送到该地址而非默认地址。

# WORKFLOW

1. 运行 `bashbug`
2. 编辑器随模板打开
3. 描述该 bug
4. 保存并退出
5. 邮件发送给 bash 维护者

# INFORMATION COLLECTED

- bash 版本
- 操作系统
- 机器架构
- 所用编译器
- 配置选项

# CAVEATS

需要配置好可用的邮件系统。可能并非在所有系统上都能使用。建议改通过项目的 issue 跟踪器报告 bug。现代 bug 报告通常经由在线平台完成。

# HISTORY

**bashbug** 自早期版本起就随 bash 发行版一同发布，以便于向开发团队报告 bug。

# INSTALL

```apt: sudo apt install bash```

```dnf: sudo dnf install bash```

```pacman: sudo pacman -S bash```

```apk: sudo apk add bash-dev```

```zypper: sudo zypper install bash```

```brew: brew install bash```

```nix: nix profile install nixpkgs#bash```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bash](/man/bash)(1), [reportbug](/man/reportbug)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/bash/)```

```[Source code](https://git.savannah.gnu.org/cgit/bash.git)```

<!-- verified: 2026-06-19 -->
