# TAGLINE

Ansible 角色的测试框架

# TLDR

在当前角色中**初始化测试场景**

```molecule init scenario```

**运行完整测试序列**

```molecule test```

**创建测试实例**

```molecule create```

**对实例运行 playbook**

```molecule converge```

**校验实例状态**

```molecule verify```

**登录实例**

```molecule login```

**销毁测试实例**

```molecule destroy```

# SYNOPSIS

**molecule** _command_ [_--scenario-name name_] [_options_]

# PARAMETERS

**init role** _NAME_
> 用 Molecule 创建新的 Ansible 角色。

**init scenario**
> 为现有角色添加场景。

**test**
> 运行完整测试序列。

**create**
> 创建实例。

**converge**
> 运行 playbook。

**verify**
> 运行验证测试。

**destroy**
> 销毁实例。

**login** [_HOST_]
> 登录到实例的 shell。

**list**
> 列出实例及其状态。

**lint**
> 运行 linter。

**cleanup**
> 运行清理 playbook。

**-s** _NAME_, **--scenario-name** _NAME_
> 目标场景。

**-d** _NAME_, **--driver-name** _NAME_
> 驱动：docker、podman、delegated、vagrant。

**--all**
> 对所有场景运行。

**--parallel**
> 并行运行各场景。

**--destroy** _WHEN_
> 何时销毁：always、never、passing。

# DESCRIPTION

**Molecule** 是一个 Ansible 角色测试框架。它会创建测试实例、对其运行 playbook、校验结果并进行清理——从而支持测试驱动的基础设施开发。

场景（Scenario）定义了如何测试一个角色：用哪个驱动创建实例、运行哪些 playbook、由哪个验证器检查结果。默认场景使用 Docker，但也支持 Podman、Vagrant 和云服务商。

完整测试序列依次运行：lint、cleanup、destroy、dependency、syntax、create、prepare、converge、idempotence、verify、cleanup、destroy。开发过程中可以单独执行各个阶段。

验证通常使用 Ansible 的 assert 模块或基于 Python 的 Testinfra。测试会检查角色是否达到了预期状态：文件存在、服务运行、配置正确。

幂等性测试会把 playbook 运行两次，若第二次运行仍有变更则判定失败。这确保角色具备良好的幂等性。

CI 集成可与 GitHub Actions、GitLab CI 等平台配合。test 命令会返回适合自动化处理的退出码。

# CAVEATS

容器化测试需要 Docker/Podman。某些角色需要特权的容器。Windows 测试能力有限。大型测试矩阵可能很慢。云驱动会产生费用。容器中的 systemd 需要特殊设置。

# HISTORY

**Molecule** 由 **Cisco** 工程师创建，约于 **2015 年**发布，旨在改进 Ansible 角色测试。Red Hat 后来接手了这个项目。它以结构化框架取代了临时性的测试方式，成为 Ansible 角色测试的事实标准。

# INSTALL

```pacman: sudo pacman -S molecule```

```zypper: sudo zypper install molecule```

```brew: brew install molecule```

```nix: nix profile install nixpkgs#molecule```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ansible](/man/ansible)(1), [ansible-lint](/man/ansible-lint)(1), [docker](/man/docker)(1)
