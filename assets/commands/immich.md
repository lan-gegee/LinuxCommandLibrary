# TAGLINE

自托管的照片和视频备份方案

# TLDR

**启动 Immich 服务器**

```docker compose up -d```

**停止 Immich**

```docker compose down```

**查看日志**

```docker compose logs -f```

**备份数据库**

```docker exec immich_postgres pg_dump > backup.sql```

# SYNOPSIS

**immich** 以 Docker 容器方式运行

# PARAMETERS

通过 docker-compose.yml 和 .env 文件配置。

**UPLOAD_LOCATION**
> 照片存储路径。

**DB_PASSWORD**
> 数据库密码。

**IMMICH_VERSION**
> 版本标签。

# DESCRIPTION

**Immich** 是一个自托管的照片和视频备份方案。它提供类似 Google Photos 的功能，配有移动应用和网页界面。

该平台支持人脸识别、地理位置和自动整理。它专为个人照片管理而设计。

# CAVEATS

通过 Docker 运行。资源占用较高。提供移动应用。

# HISTORY

Immich 由 **Alex Tran** 创建，是 Google Photos 的开源替代品。

# INSTALL

```nix: nix profile install nixpkgs#immich```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[immich-cli](/man/immich-cli)(1), [docker](/man/docker)(1)
