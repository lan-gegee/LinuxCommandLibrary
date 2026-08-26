# TAGLINE

NixOS 系统配置文件

# TLDR

**编辑系统配置**

```sudo nano /etc/nixos/configuration.nix```

**修改后重建系统**

```sudo nixos-rebuild switch```

**测试配置而不设为默认**

```sudo nixos-rebuild test```

**只构建而不激活**

```sudo nixos-rebuild build```

**回滚到上一代**

```sudo nixos-rebuild switch --rollback```

**检查配置语法**

```nix-instantiate --parse /etc/nixos/configuration.nix```

**基础配置示例**

```nix
{ config, pkgs, ... }:
{
  boot.loader.systemd-boot.enable = true;
  networking.hostName = "myhost";
  time.timeZone = "America/New_York";

  users.users.alice = {
    isNormalUser = true;
    extraGroups = [ "wheel" ];
  };

  environment.systemPackages = with pkgs; [
    vim git firefox
  ];

  services.openssh.enable = true;
}
```

# SYNOPSIS

**/etc/nixos/configuration.nix**

# COMMON OPTIONS

**boot.loader.systemd-boot.enable**
> 启用 systemd-boot 引导加载程序。

**networking.hostName**
> 设置系统主机名。

**time.timeZone**
> 设置系统时区。

**users.users.<name>**
> 定义用户账户。

**environment.systemPackages**
> 系统级软件包列表。

**services.<name>.enable**
> 启用系统服务。

**programs.<name>.enable**
> 启用系统程序。

**nixpkgs.config.allowUnfree**
> 允许专有软件包。

# DESCRIPTION

**configuration.nix** 是 NixOS（一个基于 Nix 软件包管理器构建的 Linux 发行版）的主系统配置文件。它以声明式方式定义整个系统状态：已安装的软件包、启用的服务、用户账户和系统设置。

该文件使用 Nix 表达式语言描述系统配置。更改通过 **nixos-rebuild** 以原子方式应用，它会构建一个新的系统代（generation），可立即激活或在下次启动时激活。

NixOS 将以前的配置保存为多代快照，可以轻松回滚到任意先前状态。这种方式确保了可复现的系统配置，能够纳入版本控制并共享。

# CAVEATS

语法错误会阻止系统重建；请始终先用 **nixos-rebuild test** 测试。Nix 语言有学习曲线。某些专有软件需要显式设置 allowUnfree。大型配置变更可能需要可观的下载和构建时间。

# HISTORY

NixOS 由 **Eelco Dolstra** 基于其关于 Nix 软件包管理器的博士研究创建，首个版本发布于 **2003** 年。声明式配置模型在当时具有革命性——将系统配置视为能产生可复现结果的代码。在重视可复现性的 DevOps 和开发环境中，NixOS 日渐流行。

# SEE ALSO

[nixos-rebuild](/man/nixos-rebuild)(8), [nix-env](/man/nix-env)(1), [nix](/man/nix)(1), [home-manager](/man/home-manager)(1)

# RESOURCES

```[Source code](https://github.com/NixOS/nixpkgs)```

```[Homepage](https://nixos.org)```

```[Documentation](https://nixos.org/manual/nixos/stable/)```

<!-- verified: 2026-06-23 -->
