# TAGLINE

将 OpenStreetMap 数据导入 PostgreSQL/PostGIS 数据库

# TLDR

**导入 OSM 数据**

```osm2pgsql -d [database] [file.osm.pbf]```

**以 slim 模式导入**

```osm2pgsql -d [database] -s [file.osm.pbf]```

**使用自定义样式导入**

```osm2pgsql -d [database] -S [style.lua] [file.osm.pbf]```

**追加新数据**

```osm2pgsql -d [database] -a [updates.osc]```

**设置进程数量**

```osm2pgsql -d [database] -j [4] [file.osm.pbf]```

# SYNOPSIS

**osm2pgsql** [_options_] _file_...

# PARAMETERS

**-d** _database_
> 数据库名称。

**-s**, **--slim**
> 将临时数据存入数据库。

**-S** _file_
> 样式文件。

**-a**, **--append**
> 追加模式。

**-c**, **--create**
> 创建表（默认）。

**-j** _num_
> 进程数量。

**-C** _MB_
> 缓存大小。

**-H** _host_
> 数据库主机。

**-U** _user_
> 数据库用户。

# DESCRIPTION

**osm2pgsql** 将 OpenStreetMap 数据导入 PostgreSQL/PostGIS 数据库。它常用于创建供 Mapnik 渲染地图瓦片的数据库。

该工具可以处理全量星球数据导入和增量更新。

# TYPICAL WORKFLOW

```bash
# Create database
createdb gis
psql -d gis -c "CREATE EXTENSION postgis;"

# Import data
osm2pgsql -d gis -s -C 2000 planet.osm.pbf
```

# CAVEATS

需要 PostGIS。全量星球导入需要大量资源。增量更新请使用 slim 模式。

# HISTORY

osm2pgsql 为 **OpenStreetMap** 项目而开发，旨在利用 PostgreSQL 实现 OSM 数据的地图渲染。

# INSTALL

```apt: sudo apt install osm2pgsql```

```dnf: sudo dnf install osm2pgsql```

```pacman: sudo pacman -S osm2pgsql```

```brew: brew install osm2pgsql```

```nix: nix profile install nixpkgs#osm2pgsql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

