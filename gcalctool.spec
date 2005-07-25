Summary:	GNOME calculator
Summary(pl):	Kalkulator dla GNOME
Name:		gcalctool
Version:	5.6.25
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	http://ftp.gnome.org/pub/gnome/sources/gcalctool/5.6/%{name}-%{version}.tar.bz2
# Source0-md5:	d32b69af8f533339c1d75963a053b59f
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	atk-devel >= 1:1.9.1
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gcalctool is a simple calculator that performs a variety of functions.

%description -l pl
gcalctool jest prostym kalkulatorem spe³niaj±cym wiele funkcji.

%prep
%setup -q
%patch0 -p0

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gcalctool.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall gcalctool.schemas

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README TODO gcalctoolrc
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_desktopdir}/*
%{_omf_dest_dir}/%{name}
%{_mandir}/man1/*
