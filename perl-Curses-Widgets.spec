#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Curses
%define	pnam	Widgets
Summary:	Curses::Widgets perl module
Summary(pl):	Modu³ perla Curses::Widgets
Name:		perl-%{pdir}-%{pnam}
Version:	1.992
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-56
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Curses
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
High level access to basic Curses widgets and related functions.

%description -l pl
Modu³ ten udostêpnia kontrolki bazuj±ce na bibliotece Curses.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README
%{perl_sitelib}/Curses/Widgets.pm
%{perl_sitelib}/Curses/Widgets
%{_mandir}/man3/*
