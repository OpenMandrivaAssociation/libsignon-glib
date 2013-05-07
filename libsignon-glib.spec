%define major 1
%define libname %mklibname signon-glib %major
%define girname %mklibname signon-glib-gir 1.0
%define develname %mklibname -d signon-glib

Name:		libsignon-glib
Version:	1.8
Release:	1
Group:		System/Libraries
Summary:	Authorization and authentication management for glib
License:	LGPLv2
URL:		http://code.google.com/p/accounts-sso/
Source0:	http://accounts-sso.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(check) >= 0.9.4
BuildRequires:	pkgconfig(gio-2.0) >= 2.30
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.26
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90
BuildRequires:	pkgconfig(signond) >= 8.40
BuildRequires:	python-gi >= 2.90
BuildRequires:	gobject-introspection-devel
BuildRequires:	xsltproc

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
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	pkgconfig(dbus-glib-1)

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n python-%{name}
Summary:	Python binding for %{name}
Group:		Development/Python

%description -n python-%{name}
Python binding for %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
make

%install
%makeinstall_std

rm -fr %{buildroot}%{_libdir}/*.la %{buildroot}%{_prefix}/doc

%files -n %{libname}
%doc COPYING AUTHORS
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{girname}
%{_libdir}/girepository-1.0/Signon-1.0.typelib

%files -n %{develname}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/gir-1.0/Signon-1.0.gir
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/vala/vapi/*

%files -n python-%{name}
%py_platsitedir/gi/overrides/Signon.*
