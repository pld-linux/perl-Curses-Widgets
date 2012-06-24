#
# Conditional build:
# _with_demo - perform "make test" (it IS just demo!)
%include	/usr/lib/rpm/macros.perl
%define		pdir	Curses
%define		pnam	Widgets
Summary:	Curses::Widgets Perl module
Summary(cs):	Modul Curses::Widgets pro Perl
Summary(da):	Perlmodul Curses::Widgets
Summary(de):	Curses::Widgets Perl Modul
Summary(es):	M�dulo de Perl Curses::Widgets
Summary(fr):	Module Perl Curses::Widgets
Summary(it):	Modulo di Perl Curses::Widgets
Summary(ja):	Curses::Widgets Perl �⥸�塼��
Summary(ko):	Curses::Widgets �� ����
Summary(no):	Perlmodul Curses::Widgets
Summary(pl):	Modu� Perla Curses::Widgets
Summary(pt):	M�dulo de Perl Curses::Widgets
Summary(pt_BR):	M�dulo Perl Curses::Widgets
Summary(ru):	������ ��� Perl Curses::Widgets
Summary(sv):	Curses::Widgets Perlmodul
Summary(uk):	������ ��� Perl Curses::Widgets
Summary(zh_CN):	Curses::Widgets Perl ģ��
Name:		perl-Curses-Widgets
Version:	1.997
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-56
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Curses
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
High level access to basic Curses widgets and related functions.

%description -l pl
Modu� ten udost�pnia kontrolki bazuj�ce na bibliotece Curses.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{?_with_demo:%{__make} test}

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
