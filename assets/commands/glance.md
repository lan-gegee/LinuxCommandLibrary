# TAGLINE

OpenStack 镜像服务（Glance）的旧版命令行客户端

# TLDR

**列出镜像**

```glance image-list```

**显示镜像详情**

```glance image-show [image-id]```

**从本地文件创建镜像**

```glance image-create --name [image-name] --disk-format [qcow2] --container-format [bare] --file [image.qcow2]```

**下载镜像数据**

```glance image-download [image-id] --file [output.qcow2]```

**更新镜像**

```glance image-update [image-id] --name [new-name]```

**删除镜像**

```glance image-delete [image-id]```

# SYNOPSIS

**glance** [_options_] _command_ [_command-options_]

# PARAMETERS

**image-list**
> 列出可用镜像。

**image-show** _image-id_
> 显示某个镜像的详情。

**image-create**
> 创建新的镜像记录，可用 **--file** 上传数据。

**image-update** _image-id_
> 更新镜像的元数据。

**image-download** _image-id_
> 将镜像数据下载到文件。

**image-upload** _image-id_
> 为已有镜像上传数据。

**image-delete** _image-id_
> 删除镜像。

**--file** _path_
> 要上传或保存下载数据的本地文件。

**--disk-format** _format_
> 磁盘格式（raw、qcow2、vmdk、vdi、iso、ami 等）。

**--container-format** _format_
> 容器格式（bare、ovf、aki、ari、ami 等）。

**--os-auth-token** _token_
> 身份验证令牌，可作为用户名/密码的替代方案。

**--os-username** _user_, **--os-password** _pass_
> OpenStack 凭据，也可通过环境变量设置。

**--os-image-url** _url_
> Glance API 端点，覆盖服务目录中的地址。

# DESCRIPTION

**glance** 是 **python-glanceclient** 附带的独立命令行客户端，用于 OpenStack 镜像服务（Glance）。该服务存储并提供用于启动 Nova 实例的虚拟机镜像。

它早于统一的 **openstack** CLI 出现，现在已被视为旧版工具：OpenStack 的部署实践和官方文档都引导用户在日常镜像管理中使用 `openstack image` 子命令（参见 [openstack-image](/man/openstack-image)(1)）。`glance` 二进制程序仍可用于依赖它的脚本和环境。

# CAVEATS

在当前的 OpenStack 发行版中已被 `openstack image ...` 取代；新部署应优先使用统一 CLI。需要 OpenStack 凭据（通过 `clouds.yaml`、环境变量或 `--os-*` 选项）。大镜像的上传/下载可能耗时较长，且受项目存储配额限制。

# HISTORY

Glance 是 OpenStack 最早的服务之一，与 **Nova** 一同随 **2010** 年 Austin 版本发布。在 OpenStack 将各服务的客户端整合为单一的 `openstack` 命令之前，`glance` CLI 多年来一直是它的专用客户端。

# INSTALL

```nix: nix profile install nixpkgs#glance```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openstack](/man/openstack)(1), [openstack-image](/man/openstack-image)(1), [nova](/man/nova)(1), [qemu-img](/man/qemu-img)(1)

# RESOURCES

```[Source code](https://github.com/openstack/python-glanceclient)```

```[CLI documentation](https://docs.openstack.org/python-glanceclient/latest/cli/details.html)```

<!-- verified: 2026-07-17 -->
