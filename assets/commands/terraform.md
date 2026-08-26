# TAGLINE

基础设施即代码配置工具

# TLDR

**初始化 Terraform 工作目录**

```terraform init```

**预览基础设施变更**

```terraform plan```

**应用基础设施变更**

```terraform apply```

**销毁受管基础设施**

```terraform destroy```

**格式化配置文件**

```terraform fmt```

**校验配置语法**

```terraform validate```

**显示当前状态**

```terraform show```

**列出状态中的资源**

```terraform state list```

**导入既有基础设施**

```terraform import [resource_type.name] [id]```

# SYNOPSIS

**terraform** _command_ [_options_] [_args_]

# PARAMETERS

**init**
> 初始化工作目录，下载 provider

**plan**
> 创建显示拟议变更的执行计划

**apply**
> 应用变更以达到期望状态

**destroy**
> 销毁所有受管基础设施

**fmt**
> 将配置文件格式化为规范风格

**validate**
> 检查配置的语法与一致性

**show**
> 显示当前状态或已保存的计划

**output**
> 从状态读取输出值

**state**
> 高级状态管理命令

**import**
> 将既有基础设施导入状态

**workspace**
> 管理 workspace

**-auto-approve**
> 跳过交互式确认（apply/destroy）

**-var** _'key=value'_
> 设置输入变量

**-var-file** _file_
> 从文件加载变量

**-target** _resource_
> 针对特定资源

**-parallelism** _n_
> 限制并发操作数

# DESCRIPTION

**terraform** 是一款基础设施即代码工具，用于安全高效地构建、变更和版本化云基础设施。它使用声明式配置文件来描述期望的基础设施状态。

配置使用 HCL（HashiCorp Configuration Language）编写，定义服务器、网络和数据库等资源。Terraform 通过名为 provider 的插件与云服务商（AWS、Azure、GCP 等）通信。

工作流为：**init**（准备）、**plan**（预览）、**apply**（执行）。状态跟踪在 **terraform.tfstate** 中，使 Terraform 能够知道哪些已存在、哪些需要变更。

workspace 允许用同一配置管理多个环境（dev、staging、prod），各自使用不同的状态文件。

# CONFIGURATION

**terraform.tfvars**
> 默认变量值文件，存在于工作目录时自动加载

**\*.auto.tfvars**
> 附加变量文件，按字母顺序自动加载

**~/.terraformrc** 或 **%APPDATA%/terraform.rc**
> CLI 配置文件，用于 provider 安装方式、凭据和插件缓存

**TF_VAR_name**
> 以 TF_VAR_ 为前缀的环境变量用于设置输入变量的值

**TF_CLI_CONFIG_FILE**
> 覆盖默认 CLI 配置文件的位置

# CAVEATS

状态文件包含敏感信息（密码、密钥），应安全存储。团队协作请使用远程 backend（S3、Terraform Cloud）以获得状态锁定。

**terraform destroy** 不可逆。务必先运行 **plan** 并仔细核对销毁计划。

provider 版本应在配置中固定，以确保可重现性。意外的 provider 更新可能引发问题。

在 Terraform 之外所做的更改（手动控制台操作）会导致状态漂移。可使用 **terraform refresh** 或 **import** 来协调。

# HISTORY

Terraform 由 **HashiCorp** 创建，由 Mitchell Hashimoto 于 **2014** 年首次发布。它开创了面向多云配置的"基础设施即代码"方法，并成为声明式基础设施管理的事实标准。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [ansible](/man/ansible)(1), [pulumi](/man/pulumi)(1), [tofu](/man/tofu)(1)
