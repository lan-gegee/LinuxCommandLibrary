# TAGLINE

执行 tmt 测试步骤

# TLDR

**运行**全部测试步骤

```tmt run```

**发现**将运行哪些测试

```tmt run discover -v```

以**资源调配**选项运行

```tmt run -a provision -h [container] -i [fedora:rawhide]```

运行选定的**计划**和测试

```tmt run plan -n [/plan/name] test -n [/test/name]```

在浏览器中显示**结果**

```tmt run -l report -h html -o```

带**上下文**运行

```tmt run -c [key=value]```

**交互式**运行

```tmt run -a execute -h tmt --interactive```

**试运行**并输出详细信息

```tmt run -n -vvv```

# SYNOPSIS

**tmt run** [_OPTIONS_] [_STEP_...]

# PARAMETERS

**-a, --all**
> 运行全部测试步骤

**-l, --last**
> 使用上一次运行

**-n, --dry**
> 试运行模式（只显示操作而不执行）

**-v, --verbose**
> 增加详细程度（可重复使用）

**-c, --context** _KEY=VALUE_
> 设置上下文变量

**discover**
> 显示将运行哪些测试

**provision**
> 调配将运行测试的客户机（容器、虚拟机或远程系统）

**prepare**
> 为测试准备已调配的系统（安装软件包、应用角色）

**execute**
> 运行测试

**report**
> 生成测试报告

**finish**
> 测试后清理

# DESCRIPTION

**tmt run** 执行测试管理工具的各步骤以完成测试。默认情况下，所有步骤（discover、provision、prepare、execute、report、finish）依次执行。单个步骤可以单独运行或使用修改后的选项运行。

该命令支持不同的资源调配方式，包括容器、虚拟机和远程系统。测试可以按名称、上下文或计划过滤。

# CAVEATS

运行所有步骤需要合适的资源调配后端。基于容器的执行需要 Podman 或 Docker。某些步骤需要 root 权限。大型测试套件可能需要大量资源。

# INSTALL

```dnf: sudo dnf install tmt```

```brew: brew install tmt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmt](/man/tmt)(1), [tmt-try](/man/tmt-try)(1), [podman](/man/podman)(1)
