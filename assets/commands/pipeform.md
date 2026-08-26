# TAGLINE

可视化 Terraform 运行进度的 TUI

# TLDR

**将 Terraform plan 通过管道传入 TUI**

```terraform plan -json | pipeform```

**将 Terraform apply 通过管道传入 TUI**

```terraform apply -auto-approve -json | pipeform```

**导出计时数据到 CSV**

```terraform apply -json | pipeform --time-csv=[output.csv]```

# SYNOPSIS

_terraform_command_ **-json** | **pipeform** [_options_]

# PARAMETERS

**--time-csv** _PATH_
> 生成包含计时数据的 CSV 文件以便进一步分析。

# DESCRIPTION

**pipeform** 是一个用于可视化 Terraform 操作进度的 TUI。它通过管道读取 Terraform 机器可读的 JSON 输出，并交互式地显示执行进度。执行完成后，输出变量会以表格形式展示并支持复制到剪贴板。

# CAVEATS

所有通过管道传入的 Terraform 命令都必须带有 **-json** 标志。仅支持 Terraform 机器可读的 JSON 输出格式。

# HISTORY

**pipeform** 由 **magodo** 创建，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#pipeform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1)
