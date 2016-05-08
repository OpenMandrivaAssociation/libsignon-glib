%define api	1.0
%define Werror_cflags %nil
%define major	1
%define libname	%mklibname signon-glib %{major}
%define girname	%mklibname signon-glib-gir %{api}
%define devname	%mklibname -d signon-glib
%define debug_package %nil

Summary:	Authorization and authentication management for glib
Name:		libsignon-glib
Version:	1.12
Release:	1
Group:		System/Libraries
License:	LGPLv2
Url:		http://code.google.com/p/accounts-sso/
Source0:	http://accounts-sso.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	python-gi >= 2.90
BuildRequires:	xsltproc
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(check) >= 0.9.4
BuildRequires:	pkgconfig(gio-2.0) >= 2.30
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.26
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90
BuildRequires:	pkgconfig(signond) >= 8.40

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
%setup -qn %{name}-%{version}-11033f3e12b73064d9ff2df9ae8e2d3c1883f76e

%build
%setup_compile_flags
sed -i 's!-Werror!!g' libsignon-glib/Makefile.am
./autogen.sh
%configure
make

%install
%makeinstall_std
rm -fr %{buildroot}%{_prefix}/doc
rm -fr %{buildroot}%{py_platsitedir}/gi/overrides/__pycache__
%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Signon-%{api}.typelib

%files -n %{devname}
%doc COPYING AUTHORS
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/gir-1.0/Signon-%{api}.gir
%{_datadir}/vala/vapi/*

%files -n python-%{name}
%py_platsitedir/gi/overrides/Signon.*

