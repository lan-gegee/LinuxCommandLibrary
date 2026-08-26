# TAGLINE

管理分布式系统的部署与生命周期操作。

# TLDR

**部署** release

```bosh -d [deployment] deploy [manifest.yml]```

**列出**部署

```bosh deployments```

**SSH** 进入实例

```bosh -d [deployment] ssh [instance]```

**查看**日志

```bosh -d [deployment] logs [instance]```

**更新** cloud config

```bosh update-cloud-config [cloud-config.yml]```

# SYNOPSIS

**bosh** [_options_] _command_

# DESCRIPTION

**bosh** 是 BOSH 的命令行界面。BOSH 是一款用于分布式系统的版本工程、部署和生命周期管理的工具。它常被用于部署 Cloud Foundry 及其他复杂的分布式应用。

该工具管理基础设施供给、软件部署，并处理跨多个云提供商的运维事务。

# PARAMETERS

**-d**, **--deployment** _name_
> 部署名称。

**-e**, **--environment** _alias_
> 环境别名。

**-n**, **--non-interactive**
> 非交互模式。

**--json**
> JSON 输出。

**--column** _header_
> 过滤输出列。

# COMMON COMMANDS

**deployments**
> 列出所有部署。

**deploy** _manifest_
> 创建或更新部署。

**delete-deployment**
> 删除部署。

**ssh** _instance_
> SSH 进入虚拟机。

**logs** _instance_
> 获取日志。

**vms**
> 列出虚拟机。

**tasks**
> 列出任务。

**cloud-config**
> 显示云端配置。

# WORKFLOW

```bash
# Target environment
bosh alias-env prod -e 10.0.0.6 --ca-cert cert.pem

# Log in
bosh -e prod login

# Upload stemcell
bosh -e prod upload-stemcell stemcell.tgz

# Upload release
bosh -e prod upload-release release.tgz

# Deploy
bosh -e prod -d myapp deploy manifest.yml

# Check VMs
bosh -e prod -d myapp vms

# SSH
bosh -e prod -d myapp ssh instance/0
```

# FEATURES

- 多云支持（AWS、GCP、Azure、vSphere）
- 自动健康监控
- 滚动更新
- 自动复活（虚拟机自动恢复）
- 快照与备份
- 配置管理
- 网络隔离

# CAVEATS

学习曲线陡峭。配置复杂。需要专用基础设施。最适合大规模部署。Manifest 语法可能相当繁琐。缺乏经验时调试困难。

# HISTORY

**BOSH** 由 VMware 在 **2010 年**前后为 Cloud Foundry 部署而创建，后来成为管理复杂分布式系统的开源项目。

# INSTALL

```apt: sudo apt install bosh```

```zypper: sudo zypper install bosh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cf](/man/cf)(1), [terraform](/man/terraform)(1), [kubectl](/man/kubectl)(1)

# RESOURCES

```[Source code](https://github.com/cloudfoundry/bosh-cli)```

```[Homepage](https://bosh.io)```

```[Documentation](https://bosh.io/docs/cli-v2/)```

<!-- verified: 2026-06-19 -->
