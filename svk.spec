
%include	/usr/lib/rpm/macros.perl

Summary:	SVK - a decentralized version control system
Summary(pl.UTF-8):	SVK - zdecentralizowany system kontroli wersji
Name:		svk
Version:	2.0.0
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Version Control
Source0:	http://download.bestpractical.com/pub/svk/SVK-v%{version}.tar.gz
# Source0-md5:	37ff4acde9f9a0f987bde48b32616ab3
URL:		http://svk.bestpractical.com/
BuildRequires:	perl-Algorithm-Annotate
BuildRequires:	perl-Algorithm-Diff >= 1.1902
BuildRequires:	perl-App-CLI
BuildRequires:	perl-Class-Autouse >= 1.15
BuildRequires:	perl-Class-Data-Inheritable >= 0.04
BuildRequires:	perl-Clone
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Data-Hierarchy >= 0.17
BuildRequires:	perl-File-BaseDir
BuildRequires:	perl-File-MimeInfo
BuildRequires:	perl(File::Spec) >= 3.19
BuildRequires:	perl-File-Temp >= 0.17
BuildRequires:	perl-File-Type
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-IO-Digest
BuildRequires:	perl-IO-Pager
BuildRequires:	perl-List-MoreUtils >= 0.17
BuildRequires:	perl-Locale-Maketext-Lexicon >= 1:0.62
BuildRequires:	perl-Locale-Maketext-Simple >= 0.16
BuildRequires:	perl-PathTools >= 3.18
BuildRequires:	perl-Path-Class >= 0.16
BuildRequires:	perl-PerlIO-eol >= 0.13
BuildRequires:	perl-PerlIO-via-dynamic >= 0.11
BuildRequires:	perl-PerlIO-via-symlink
BuildRequires:	perl-Pod-Escapes
BuildRequires:	perl-Pod-Simple
BuildRequires:	perl-Regexp-Shellish
BuildRequires:	perl-SVN-Mirror >= 0.66
BuildRequires:	perl-SVN-Simple >= 0.27
BuildRequires:	perl-Text-Diff
BuildRequires:	perl-TimeDate
BuildRequires:	perl-UNIVERSAL-require >= 0.10
BuildRequires:	perl-YAML >= 0.36
BuildRequires:	perl-YAML-Syck >= 0.64
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	perl-subversion >= 1.0.3
BuildRequires:	perl-version >= 0.68
#BuildRequires:	resolving-builders-blocking
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(SVK::.*)'

%description
svk is a decentralized version control system. While Subversion (svn)
aims to take over the CVS user base, svk attempts to take over the
user base of the other version control systems, including people who
have already switched to another version control system, as well as
people who have not yet started using a version control system. It is
written in Perl and uses Subversion's underlying filesystem.

%description -l pl.UTF-8
svk to zdecentralizowany system kontroli wersji. O ile celem
Subversion (svn) jest przejęcie użytkowników CVS, svk próbuje przejąć
użytkowników innych systemów kontroli wersji, włączając ludzi którzy
już przenieśli się na inny system kontroli wersji, a także ludzi,
którzy jeszcze nie zaczęli używać systemu kontroli wersji. Jest
napisany w Perlu i używa systemu plików Subversion.

%package -n perl-SVK
Summary:	SVK Perl modules
Summary(pl.UTF-8):	Moduły Perla SVK
Group:		Development/Languages/Perl

%description -n perl-SVK
SVK Perl modules.

%description -n perl-SVK -l pl.UTF-8
Moduły Perla SVK.

%prep
%setup -q -n SVK-v%{version}

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
%{_mandir}/man1/*

%files -n perl-SVK
%defattr(644,root,root,755)
%{perl_vendorlib}/SVK
%{perl_vendorlib}/SVK.pm
%{_mandir}/man3/*
