# TAGLINE

HashiCorp 出品的跨平台机器镜像创建工具

# TLDR

**从模板构建镜像**

```packer build [template.pkr.hcl]```

**验证模板**

```packer validate [template.pkr.hcl]```

**初始化插件**

```packer init [template.pkr.hcl]```

**格式化模板文件**

```packer fmt [template.pkr.hcl]```

**使用变量构建**

```packer build -var "[key]=[value]" [template.pkr.hcl]```

**只构建指定目标**

```packer build -only [amazon-ebs.web-server] [template.pkr.hcl]```

**检查模板**

```packer inspect [template.pkr.hcl]```

**启用调试模式**

```packer build -debug [template.pkr.hcl]```

# SYNOPSIS

**packer** _command_ [_-var key=value_] [_-only target_] [_-except target_] [_options_] _template_

# PARAMETERS

**build**
> 从模板构建镜像。

**validate**
> 检查模板语法。

**init**
> 安装所需的插件。

**fmt**
> 格式化模板文件。

**inspect**
> 显示模板组件。

**console**
> 交互式 HCL 控制台。

**-var** _key=value_
> 设置变量值。

**-var-file** _file_
> 变量定义文件。

**-only** _name_
> 只构建指定的 builder。

**-except** _name_
> 跳过指定的 builder。

**-force**
> 强制构建，覆盖已有结果。

**-on-error** _ACTION_
> 出错时的动作：cleanup、abort、ask、run-cleanup-provisioner。

**-debug**
> 带断点的调试模式。

**-parallel-builds** _N_
> 并行构建上限。

**-timestamp-ui**
> 在 UI 输出中添加时间戳。

# DESCRIPTION

**Packer** 是 HashiCorp 的工具，用于从单一源配置在多个平台上创建机器镜像。它自动完成 AWS、Azure、GCP、Docker、VMware 及许多其他平台的镜像构建。

模板定义 builder（在哪里创建镜像）、provisioner（如何配置镜像）和 post-processor（对完成的镜像做什么）。现代模板使用 HCL 格式（.pkr.hcl），不过 JSON 仍受支持。

builder 创建最初的机器实例。例如 amazon-ebs 用于 AWS AMI，azure-arm 用于 Azure 镜像，docker 用于容器。每个 builder 处理特定平台的细节。

provisioner 在机器启动后运行：shell 脚本、Ansible、Chef、Puppet 或文件上传来配置镜像。多个 provisioner 按顺序执行，逐步构建配置。

post-processor 处理完成的镜像：上传到 registry、压缩或创建 Vagrant box。镜像可以分发到多个区域或云平台。

# CAVEATS

云端 builder 需要平台凭据。构建时间因平台而异且差别显著。大镜像需要更多时间和存储。调试模式会在步骤之间暂停。JSON 模板已弃用但仍然可用。非内置的 builder 需要先初始化插件。

# HISTORY

**Packer** 由 Mitchell Hashimoto 开发，于 **2013** 年由 **HashiCorp** 发布。它解决了跨多个平台创建相同机器镜像的难题。该工具成为不可变基础设施 DevOps 工作流中的重要一环。**2020** 年引入 HCL2 模板格式，与 Terraform 语法保持一致。

# INSTALL

```pacman: sudo pacman -S packer```

```nix: nix profile install nixpkgs#packer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [vagrant](/man/vagrant)(1), [docker](/man/docker)(1), [ansible](/man/ansible)(1)
