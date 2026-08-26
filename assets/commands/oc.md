# TAGLINE

openShift CLI

# TLDR

**登录集群**

```oc login [https://api.cluster:6443]```

**获取资源**

```oc get [pods|services|deployments]```

**从 YAML 创建**

```oc apply -f [manifest.yaml]```

**切换项目**

```oc project [project_name]```

**查看日志**

```oc logs [pod_name]```

**在 pod 中执行**

```oc exec -it [pod_name] -- [command]```

# SYNOPSIS

**oc** [_command_] [_options_]

# PARAMETERS

**login** _URL_
> 对集群进行身份验证。

**get** _RESOURCE_
> 列出资源。

**apply** **-f** _FILE_
> 应用配置。

**project** _NAME_
> 切换项目/命名空间。

**logs** _POD_
> 查看 pod 日志。

**exec** _POD_
> 在 pod 中执行命令。

**--help**
> 显示帮助信息。

# DESCRIPTION

**oc** 是 OpenShift 的 CLI，用于管理 OpenShift/Kubernetes 集群。

该工具在 kubectl 基础上扩展了 OpenShift 特性，是 OpenShift 的主要操作界面。

# CAVEATS

包含 OpenShift 特有的扩展。与 kubectl 兼容。需要集群访问权限。

# HISTORY

oc 由 **Red Hat** 开发，是 OpenShift Container Platform 的命令行界面。

# INSTALL

```zypper: sudo zypper install oc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [docker](/man/docker)(1), [podman](/man/podman)(1)
