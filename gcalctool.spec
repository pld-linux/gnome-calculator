Summary:	GNOME calculator
Summary(pl.UTF-8):	Kalkulator dla GNOME
Name:		gcalctool
Version:	5.20.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Math
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gcalctool/5.20/%{name}-%{version}.tar.bz2
# Source0-md5:	fefe44a52465eae39c5bf9a9669a0aa6
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.19.1
BuildRequires:	atk-devel >= 1:1.20.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.11.2
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
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
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_desktopdir}/*.desktop
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/gcalctool/gcalctool-C.omf
%lang(bg) %{_omf_dest_dir}/gcalctool/gcalctool-bg.omf
%lang(de) %{_omf_dest_dir}/gcalctool/gcalctool-de.omf
%lang(es) %{_omf_dest_dir}/gcalctool/gcalctool-es.omf
%lang(fr) %{_omf_dest_dir}/gcalctool/gcalctool-fr.omf
%lang(it) %{_omf_dest_dir}/gcalctool/gcalctool-it.omf
%lang(ja) %{_omf_dest_dir}/gcalctool/gcalctool-ja.omf
%lang(ko) %{_omf_dest_dir}/gcalctool/gcalctool-ko.omf
%lang(oc) %{_omf_dest_dir}/gcalctool/gcalctool-oc.omf
%lang(pt_BR) %{_omf_dest_dir}/gcalctool/gcalctool-pt_BR.omf
%lang(sv) %{_omf_dest_dir}/gcalctool/gcalctool-sv.omf
%lang(zh_CN) %{_omf_dest_dir}/gcalctool/gcalctool-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/gcalctool/gcalctool-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/gcalctool/gcalctool-zh_TW.omf
%{_mandir}/man1/*
