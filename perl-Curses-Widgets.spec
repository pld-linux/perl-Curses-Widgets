#
# Conditional build:
%bcond_with	demo	# perform "make test" (it IS just demo!)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Curses
%define	pnam	Widgets
Summary:	Curses::Widgets - base widget class for use with the Curses::Application framework
Summary(pl):	Curses::Widgets - podstawowa klasa kontrolek do wykorzystania w szkielecie Curses::Application
Name:		perl-Curses-Widgets
Version:	1.997
Release:	3
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	142b14bb761f579f98b4266405f06f8a
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_demo:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README
%{perl_vendorlib}/Curses/Widgets.pm
%{perl_vendorlib}/Curses/Widgets
%{_mandir}/man3/*
