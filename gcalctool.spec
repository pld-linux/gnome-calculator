Summary:	GNOME calculator
Summary(pl.UTF-8):	Kalkulator dla GNOME
Name:		gcalctool
Version:	5.32.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Math
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gcalctool/5.32/%{name}-%{version}.tar.bz2
# Source0-md5:	3f56976752dc990b4fb9e5d60e9a04eb
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	docbook-dtd412-xml
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	scrollkeeper
Requires:	dconf
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gcalctool is a simple calculator that performs a variety of functions.

%description -l pl.UTF-8
gcalctool jest prostym kalkulatorem spełniającym wiele funkcji.

%prep
%setup -q

sed -i -e 's/^en@shaw//' po/LINGUAS
rm -f po/en@shaw.po

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
	--disable-scrollkeeper \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
glib-compile-schemas %{_datadir}/glib-2.0/schemas

%postun
%scrollkeeper_update_postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gcalccmd
%attr(755,root,root) %{_bindir}/gcalctool
%attr(755,root,root) %{_bindir}/gnome-calculator
%{_desktopdir}/gcalctool.desktop
%{_datadir}/gcalctool
%{_datadir}/glib-2.0/schemas/org.gnome.gcalctool.gschema.xml
%{_mandir}/man1/gcalctool.1*
