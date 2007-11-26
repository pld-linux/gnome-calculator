Summary:	GNOME calculator
Summary(pl.UTF-8):	Kalkulator dla GNOME
Name:		gcalctool
Version:	5.20.2
Release:	2
License:	GPL v2
Group:		X11/Applications/Math
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gcalctool/5.20/%{name}-%{version}.tar.bz2
# Source0-md5:	bcde10b8029d3a513183e8aac9506c1f
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	atk-devel >= 1:1.20.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
# support for --with-omf in find-lang.sh
BuildRequires:	rpm-build >= 4.4.9-10
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

sed -i -e s#sr\@Latn#sr\@latin# po/LINGUAS
mv -f po/sr\@{Latn,latin}.po

%build
%{__gnome_doc_common}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
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
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/gnome-calculator
%{_sysconfdir}/gconf/schemas/gcalctool.schemas
%{_desktopdir}/*.desktop
%{_mandir}/man1/*.1*
