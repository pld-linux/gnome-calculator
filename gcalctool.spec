Summary:	GNOME calculator
Summary(pl):	Kalkulator dla GNOME
Name:		gcalctool
Version:	5.8.20
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	http://ftp.gnome.org/pub/gnome/sources/gcalctool/5.8/%{name}-%{version}.tar.bz2
# Source0-md5:	c6324ba4d3a50f9605229c0ba601e6b3
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	atk-devel >= 1:1.12.1
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35
BuildRequires:	libgnomeui-devel >= 2.15.90
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2 >= 2.14.0
Requires(post,postun):	scrollkeeper
Requires:	libgnomeui >= 2.15.90
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gcalctool is a simple calculator that performs a variety of functions.

%description -l pl
gcalctool jest prostym kalkulatorem spe³niaj±cym wiele funkcji.

%prep
%setup -q
%patch0 -p0

%build
%{__gnome_doc_common}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/tk

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
%{_sysconfdir}/gconf/schemas/gcalctool.schemas
%{_desktopdir}/*
%{_omf_dest_dir}/%{name}
%{_mandir}/man1/*
