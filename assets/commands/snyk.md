# TAGLINE

查找并修复安全漏洞

# TLDR

**测试项目漏洞**

```snyk test```

**测试指定文件**

```snyk test --file=[package.json]```

**持续监控项目**

```snyk monitor```

**测试容器镜像**

```snyk container test [image:tag]```

**测试 IaC 文件**

```snyk iac test [/path/to/terraform/]```

**测试代码问题**

```snyk code test```

**身份验证**

```snyk auth```

**忽略特定漏洞**

```snyk ignore --id=[SNYK-JS-LODASH-567746]```

# SYNOPSIS

**snyk** _command_ [_--file file_] [_--severity-threshold level_] [_options_] [_target_]

# PARAMETERS

**test**
> 测试项目漏洞。

**monitor**
> 记录项目快照以便持续监控。

**container test** _IMAGE_
> 测试容器镜像。

**container monitor** _IMAGE_
> 监控容器镜像。

**iac test** _PATH_
> 测试基础设施即代码。

**code test**
> 测试源代码（SAST）。

**auth** [_TOKEN_]
> 与 Snyk 进行身份验证。

**ignore**
> 忽略某个问题。

**wizard**
> 交互式修复。

**fix**
> 应用修复措施解决漏洞。

**sbom**
> 生成软件物料清单（SBOM）。

**policy**
> 管理 .snyk 策略文件。

**--file** _FILE_
> 要测试的清单文件。

**--severity-threshold** _LEVEL_
> 只报告：low、medium、high、critical。

**--json**
> 以 JSON 输出。

**--sarif**
> 以 SARIF 输出。

**--all-projects**
> 测试目录中的所有项目。

**--dev**
> 在扫描中包含开发依赖。

**--fail-on** _TYPE_
> 失败条件：all、upgradable、patchable。

**--prune-repeated-subdependencies**
> 剪除重复的子依赖。

**-d**, **--debug**
> 调试输出。

**--org** _ORG_
> 指定组织。

# DESCRIPTION

**Snyk** 用于查找并修复代码、依赖项、容器和基础设施即代码中的漏洞。它可集成到开发工作流和 CI/CD 流水线中，并提供持续监控。

依赖测试会对照 Snyk 的漏洞数据库扫描包清单（package.json、requirements.txt、pom.xml 等）。结果会显示 CVE、严重程度以及可用的修复方案。

容器扫描逐层分析 Docker 镜像，识别基础镜像和应用依赖中的易受攻击软件包。建议中还包括更安全的基础镜像替代方案。

基础设施即代码测试可在部署前发现 Terraform、CloudFormation、Kubernetes 及其他 IaC 文件中的错误配置。问题涵盖安全组、加密设置和访问控制等。

静态分析（code test）在源代码中发现安全问题：注入缺陷、硬编码的机密信息及其他漏洞。

monitor 命令会在 Snyk 服务中创建快照，以便在发现新 CVE 时持续发出漏洞警报。

# CAVEATS

完整功能需要账户。某些功能需要付费计划。访问数据库需要联网。大型项目扫描耗时较长。可能出现误报。并非所有包生态系统都得到完整支持。

# HISTORY

**Snyk** 由 Guy Podjarny 于 **2015 年**创立。其名字是"kyns"（开源安全）的倒写。它从 JavaScript 依赖扫描起步，随后扩展到容器、IaC 和代码分析。公司获得了大量融资，成为开发者安全工具领域的领导者。

# INSTALL

```nix: nix profile install nixpkgs#snyk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm-audit](/man/npm-audit)(1), [safety](/man/safety)(1), [trivy](/man/trivy)(1), [checkov](/man/checkov)(1), [docker](/man/docker)(1)
