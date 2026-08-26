# TAGLINE

格式化 Terraform 配置文件

# TLDR

**格式化当前目录**

```terraform fmt```

**递归格式化**

```terraform fmt -recursive```

**检查格式**

```terraform fmt -check```

**显示差异**

```terraform fmt -diff```

**检查格式并显示差异**

```terraform fmt -check -diff```

**格式化指定目录**

```terraform fmt [path/to/directory]```

# SYNOPSIS

**terraform** **fmt** [_options_] [_dir_]

# PARAMETERS

**-recursive**
> 处理子目录。

**-check**
> 检查是否已格式化（是则退出码为 0）。

**-diff**
> 显示格式差异。

**-write**
> 写入更改（默认 true）。

**-list**
> 列出存在格式差异的文件（默认 true）。

**-no-color**
> 禁用 diff 中的彩色输出。

# DESCRIPTION

**terraform fmt** 将 Terraform 配置文件格式化为规范风格。确保跨文件、跨团队格式一致。建议在提交前或 CI 中运行。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-init](/man/terraform-init)(1), [terraform-plan](/man/terraform-plan)(1)
