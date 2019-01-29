%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	Integrated LaTeX Environment for the GNOME desktop
Name:		latexila
Version:	3.27.1
Release:	1
Group:		Publishing
License:	GPLv3+
URL:		http://projects.gnome.org/latexila/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	vala
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(gee-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)

Requires:	hicolor-icon-theme
Requires:	gsettings-desktop-schemas
Requires:	rubber

%description
LaTeXila is an Integrated LaTeX Environment for GNOME. The main features are:
  * Configurable buttons to compile, convert and view a document in one click
  * LaTeX commands auto-completion
  * Symbol tables (Greek letters, arrows, ...)
  * File browser integrated
  * Template managing
  * Menus with the most commonly used LaTeX commands
  * Easy projects management

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING README NEWS HACKING
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/%{name}.1.*

