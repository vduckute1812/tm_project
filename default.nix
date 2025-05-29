{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "django-dev";

  buildInputs = [
    pkgs.python311Packages.python
    pkgs.python311Packages.pip
    pkgs.python311Packages.django
    pkgs.python311Packages.django-environ
    pkgs.python311Packages.mysqlclient
  ];
}