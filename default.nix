{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "django-dev";

  buildInputs = [
    pkgs.python311
    pkgs.pkg-config
    pkgs.mariadb
    pkgs.python311Packages.python
    pkgs.python311Packages.pip
    pkgs.python311Packages.mysqlclient
  ];
}