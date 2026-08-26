# TAGLINE

将 Sailfish 应用部署到设备或模拟器

# TLDR

**将应用部署到设备**

```sfdk deploy```

**使用手动方式部署**

```sfdk deploy --manual```

**使用 zypper dup 方式部署**

```sfdk deploy --zypper-dup```

**仅预览部署而不实际执行**

```sfdk deploy --dry-run```

# SYNOPSIS

**sfdk deploy** [_options_]

# PARAMETERS

**--sdk**
> 通过 SDK 连接进行部署。

**--manual**
> 手动部署（复制 RPM 包并安装）。

**--rsync**
> 使用 rsync 进行部署。

**--zypper-dup**
> 使用 zypper 发行版升级进行部署。

**--dry-run**
> 仅预览部署，不实际应用更改。

# DESCRIPTION

**sfdk deploy** 将已构建的 Sailfish OS 应用包部署到先前在 Sailfish IDE 中注册过的设备或模拟器。它始终部署输出目录中最新构建的版本，并遵循软件包依赖关系。根据目标环境的不同，可以使用多种部署方式。

# SEE ALSO

[sfdk](/man/sfdk)(1), [sfdk-prepare](/man/sfdk-prepare)(1), [sfdk-undeploy](/man/sfdk-undeploy)(1)
