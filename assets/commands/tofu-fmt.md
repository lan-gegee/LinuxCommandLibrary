# TAGLINE

格式化 OpenTofu 配置文件

# TLDR

**格式化当前目录**

```tofu fmt```

**递归格式化**

```tofu fmt -recursive```

**检查格式（未格式化则以非零状态退出）**

```tofu fmt -check```

**显示格式更改的差异**

```tofu fmt -diff```

**从 stdin 格式化并写入 stdout**

```cat main.tf | tofu fmt -```

# SYNOPSIS

**tofu** **fmt** [_options_] [_target_]

# DESCRIPTION

**tofu fmt** 将 OpenTofu 配置文件重写为规范的格式和风格。它应用 HCL 语言风格约定的一部分，并进行其他一些提高可读性的微调。OpenTofu 是由 Linux 基金会维护的 Terraform 开源分支。

默认情况下，**tofu fmt** 扫描当前目录中的配置文件。如果提供目标目录，它会扫描该目录。如果提供单个文件，则只处理该文件。目标为连字符（_-_) 时从标准输入读取。

# PARAMETERS

**-list**=_false_
> 不列出包含格式不一致问题的文件。

**-write**=_false_
> 不覆盖输入文件（**-check** 或从 stdin 读取时隐含此行为）。

**-diff**
> 显示格式更改的差异。

**-check**
> 检查输入是否已格式化。如果所有输入均已正确格式化则退出状态为 0；否则非零。

**-recursive**
> 同时处理子目录中的文件。默认只处理给定的目录。

# CAVEATS

除非使用 **-check**、**-write=false** 或 stdin 输入，否则该命令会就地修改文件。**tofu fmt** 的格式化结果在大版本之间可能不稳定；升级后请重新运行。语法有效但未格式化的文件会被修改；无效文件会报错且不做修改。

# HISTORY

在 HashiCorp 将 Terraform 许可证更改为 Business Source License 后，**OpenTofu** 于 **2023 年**从 **Terraform** 分叉而来。**fmt** 子命令继承自 Terraform，并与 **terraform fmt** 基本保持兼容。

# INSTALL

```dnf: sudo dnf install opentofu```

```pacman: sudo pacman -S opentofu```

```apk: sudo apk add opentofu```

```zypper: sudo zypper install opentofu```

```brew: brew install opentofu```

```nix: nix profile install nixpkgs#opentofu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tofu](/man/tofu)(1), [terraform-fmt](/man/terraform-fmt)(1)
