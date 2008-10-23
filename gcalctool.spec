Summary:	GNOME calculator
Summary(pl.UTF-8):	Kalkulator dla GNOME
Name:		gcalctool
Version:	5.24.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Math
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gcalctool/5.24/%{name}-%{version}.tar.bz2
# Source0-md5:	39c4ecdf60d250dbaac1c2c253aab653
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gcalctool is a simple calculator that performs a variety of functions.

%description -l pl.UTF-8
gcalctool jest prostym kalkulatorem spełniającym wiele funkcji.

%prep
%setup -q

%build
%{__gnome_doc_common}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf --all-name

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
%attr(755,root,root) %{_bindir}/gcalctool
%attr(755,root,root) %{_bindir}/gnome-calculator
%{_sysconfdir}/gconf/schemas/gcalctool.schemas
%{_desktopdir}/gcalctool.desktop
%{_datadir}/gcalctool
%{_mandir}/man1/gcalctool.1*
