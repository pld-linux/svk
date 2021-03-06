Summary:	SVK - a decentralized version control system
Summary(pl.UTF-8):	SVK - zdecentralizowany system kontroli wersji
Name:		svk
Version:	2.2.3
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Version Control
# Check updates from CPAN: http://search.cpan.org/~clkao/SVK-v2.2.3/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/SVK-v%{version}.tar.gz
# Source0-md5:	86ad8796345400b7b0338dab7a4ca977
URL:		http://svk.bestpractical.com/
BuildRequires:	perl(File::Spec) >= 3.19
BuildRequires:	perl-Algorithm-Annotate
BuildRequires:	perl-Algorithm-Diff >= 1.1902
BuildRequires:	perl-App-CLI
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Class-Autouse >= 1.15
BuildRequires:	perl-Class-Data-Inheritable >= 0.04
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Data-Hierarchy >= 0.17
BuildRequires:	perl-File-Temp >= 0.17
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-IO-Digest
BuildRequires:	perl-IO-Pager
BuildRequires:	perl-List-MoreUtils >= 0.17
BuildRequires:	perl-Locale-Maketext-Lexicon >= 1:0.62
BuildRequires:	perl-Locale-Maketext-Simple >= 0.16
BuildRequires:	perl-Log-Log4perl >= 1.10
BuildRequires:	perl-Path-Class >= 0.16
BuildRequires:	perl-PathTools >= 3.18
BuildRequires:	perl-PerlIO-eol >= 0.13
BuildRequires:	perl-PerlIO-gzip
BuildRequires:	perl-PerlIO-via-Bzip2
BuildRequires:	perl-PerlIO-via-dynamic >= 0.11
BuildRequires:	perl-PerlIO-via-symlink
BuildRequires:	perl-Pod-Escapes
BuildRequires:	perl-Pod-Simple
BuildRequires:	perl-SVN-Dump >= 0.04
BuildRequires:	perl-SVN-Mirror >= 0.66
BuildRequires:	perl-SVN-Simple >= 0.27
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Time-Progress
BuildRequires:	perl-UNIVERSAL-require >= 0.10
BuildRequires:	perl-YAML-Syck >= 0.64
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	perl-subversion >= 1.0.3
BuildRequires:	perl-version >= 0.68
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-App-CLI
Requires:	perl-Class-Accessor
Requires:	perl-Class-Data-Inheritable
Requires:	perl-SVK = %{version}-%{release}
Requires:	perl-Term-ReadKey
Requires:	perl-Time-Progress
Suggests:	perl-SVN-Mirror
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(SVK::.*)

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

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/SVK/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/svk
%{_mandir}/man1/svk.1p*

%files -n perl-SVK
%defattr(644,root,root,755)
%{perl_vendorlib}/SVK
%{perl_vendorlib}/SVK.pm
%{_mandir}/man3/SVK*.3pm*
