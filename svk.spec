# TODO:
# - split into svk and perl-svk package
#
%include	/usr/lib/rpm/macros.perl
Summary:	http://svk.elixus.org/Irssi is a IRC client
Name:		svk
Version:	0.14
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Version Control
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/SVK-%{version}.tar.gz
# Source0-md5:	630025c5a2928c28e5b3b934e4d968c6
URL:		http://svk.elixus.org/
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	perl-subversion >= 1.0.3
BuildRequires:	perl-Algorithm-Annotate
BuildRequires:	perl-Text-Diff
BuildRequires:	perl-Algorithm-Diff
BuildRequires:	perl-YAML
BuildRequires:	perl-Regexp-Shellish
BuildRequires:	perl-Data-Hierarchy >= 0.17
BuildRequires:	perl-Clone
BuildRequires:	perl-Pod-Escapes
BuildRequires:	perl-Pod-Simple
BuildRequires:	perl-PerlIO-via-dynamic >= 0.2
BuildRequires:	perl-SVN-Simple
BuildRequires:	perl-Locale-Maketext-Lexicon
BuildRequires:	perl-Locale-Maketext-Simple
BuildRequires:	perl-SVN-Mirror
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
svk is a decentralized version control system. While Subversion (svn)
aims to take over the CVS user base, svk attempts to take over the
user base of the other version control systems, including people who
have already switched to another version control system, as well as
people who have not yet started using a version control system. It is
written in Perl and uses Subversion's underlying filesystem.

%prep
%setup -q -n SVK-%{version}

%build
%{__perl} Makefile.PL \
        INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[13]/*
%{perl_vendorlib}/SVK
%{perl_vendorlib}/SVK.pm
