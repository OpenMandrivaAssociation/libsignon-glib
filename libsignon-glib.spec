%define api	1.0
%define Werror_cflags %nil
%define major	2
%define libname	%mklibname signon-glib %{major}
%define girname	%mklibname signon-glib-gir %{api}
%define devname	%mklibname -d signon-glib
%define debug_package %nil

Summary:	Authorization and authentication management for glib
Name:		libsignon-glib
Version:	2.1
Release:	2
Group:		System/Libraries
License:	LGPLv2
Url:		http://code.google.com/p/accounts-sso/
Source0:	http://accounts-sso.googlecode.com/files/%{name}-%{version}.tar.gz
# the shared dbus interfaces are maintained in a separate git submodule
%define ifaces  signon-dbus-specification
%define icommit 67487954653006ebd0743188342df65342dc8f9b
Source1:       https://gitlab.com/accounts-sso/%{ifaces}/-/archive/%{icommit}/%{ifaces}-%{icommit}.tar.gz

BuildRequires:	python-gi >= 2.90
BuildRequires:  meson
BuildRequires:	xsltproc
BuildRequires:	gtk-doc
BuildRequires:  vala
BuildRequires:  xsltproc
BuildRequires:	pkgconfig(check) >= 0.9.4
BuildRequires:	pkgconfig(gio-2.0) >= 2.30
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.26
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90
BuildRequires:	pkgconfig(signond)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(pygobject)

%description
libsignon-glib provides authorization and authentication management for GLib
applications.

%package -n %{libname}
Group:		System/Libraries
Summary:	Accounts and SSO (Single Sign-On) framework

%description -n %{libname}
libsignon-glib provides authorization and authentication management for GLib
applications.

%package -n %{girname}
Group:		System/Libraries
Summary:	GObject Introspection interface description for %{name}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n python-%{name}
Summary:	Python binding for %{name}
Group:		Development/Python

%description -n python-%{name}
Python binding for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

# initialise git submodule manually
pushd libsignon-glib/interfaces
tar -xzf %{SOURCE1}
mv %{ifaces}-%{icommit}/* ./
rmdir %{ifaces}-%{icommit}
popd


%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%doc AUTHORS README.md NEWS
%license COPYING
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{girname}
%{_libdir}/girepository-1.0/Signon-2.0.typelib

%files -n %{devname}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/
%{_datadir}/gir-1.0/Signon-2.0.gir
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/vala/vapi/*

%files -n python-%{name}
%{python_sitearch}/gi/overrides/Signon.*
%{python_sitearch}/gi/overrides/__pycache__/*

