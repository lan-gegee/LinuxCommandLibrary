# TAGLINE

管理 Vagrant 插件和扩展

# TLDR

**列出插件**

```vagrant plugin list```

**安装插件**

```vagrant plugin install [name]```

**卸载插件**

```vagrant plugin uninstall [name]```

**更新插件**

```vagrant plugin update```

**修复插件**

```vagrant plugin repair```

# SYNOPSIS

**vagrant** **plugin** _command_ [_options_]

# PARAMETERS

**list**
> 列出已安装的插件。

**install** _name_
> 安装插件。

**uninstall** _name_
> 移除插件。

**update** _name_
> 更新插件。

**repair**
> 修复插件问题。

**expunge**
> 移除所有插件。

**--plugin-version** _ver_
> 指定版本。

# DESCRIPTION

**vagrant plugin** 管理 Vagrant 插件。插件通过提供者、预配置器和命令来扩展 Vagrant。可从 RubyGems 或本地文件安装。

# INSTALL

```apt: sudo apt install vagrant```

```dnf: sudo dnf install vagrant```

```nix: nix profile install nixpkgs#vagrant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vagrant](/man/vagrant)(1)
